from lxml import html, etree
import requests
import os
import io
import pyodbc


def main():

    # Connect to SQL Server
    connection = pyodbc.connect("DRIVER={SQL Server};SERVER=DESKTOP-DLRRFPE;Trusted_connection=yes;")
    connection.autocommit = True
    # Create database
    cursor = connection.cursor()
    cursor.execute("IF DB_ID('STATE_OF_THE_UNION_ADDRESSES') IS NULL CREATE DATABASE STATE_OF_THE_UNION_ADDRESSES;")
    cursor.execute("USE STATE_OF_THE_UNION_ADDRESSES;")
    # Create table
    cursor.execute("IF OBJECT_ID('dbo.ADDRESS_TABLE') IS NOT NULL DROP TABLE dbo.ADDRESS_TABLE;")
    cursor.execute("CREATE TABLE dbo.ADDRESS_TABLE ("
                   "NAME_OF_PRESIDENT VARCHAR(30), "
                   "DATE_OF_UNION_ADDRESS DATE, "
                   "LINK_TO_ADDRESS VARCHAR(150), "
                   "TEXT_OF_ADDRESS NVARCHAR(MAX), "
                   "FILE_PATH VARCHAR(150)"
                   ");")

    # Create directory to store text files for addresses
    os.mkdir("Address Files")

    # Get page content as string
    url = "https://www.infoplease.com/primary-sources/government/presidential-speeches/state-union-addresses"
    html_string = requests.get(url).content
    # Convert string into element tree object
    element_html = html.fromstring(html_string)
    html_element_tree = etree.ElementTree(element_html)

    # Create a list of tags for addresses
    addresses = html_element_tree.xpath("//dl/dt/span[@class='article']/a")

    # Get data from each element in addresses and insert into SQL table
    for element in addresses:
        # Extract data
        tag_text = element.text.replace(")", "").split("(")
        name = tag_text[0]
        date = tag_text[1].replace(')', '').strip()
        for suffix in ('rd', 'th', 'nd', 'st'):
            date = date.replace(suffix, "")

        link = "https://www.infoplease.com/primary-sources/government/presidential-speeches/state-union-address-"\
                         + name.replace(".", "").replace(" ", "-") + date.replace(",", "").replace(" ", "-")
        alternate_link = "https://www.infoplease.com/" + element.attrib['href']
        # Convert page content element tree object
        try:
            text_page = html.fromstring(requests.get(link).content)
            text_etree = etree.ElementTree(text_page)

            speech_paragraphs = text_etree.xpath("//div[@class='article']/p")

            # Make sure speech text is found
            assert speech_paragraphs, "Link 1 invalid"

            # Concatenate paragraphs
            speech_text = ""
            for paragraph in speech_paragraphs:
                speech_text = speech_text + paragraph.text
                
        except:
            try:
                link = alternate_link
                text_page = html.fromstring(requests.get(alternate_link).content)
                text_etree = etree.ElementTree(text_page)

                speech_paragraphs = text_etree.xpath("//div[@class='article']/p")

                # Make sure speech text is found
                assert speech_paragraphs, "Link 2 invalid"

                # Concatenate paragraphs
                speech_text = ""
                for paragraph in speech_paragraphs:
                    speech_text = speech_text + paragraph.text

            except:
                link = "NO LINK FOUND"
                speech_text = "NO SPEECH FOUND"
        
        # Create file adn write address text to it
        file = io.open("Address Files/" + element.text + ".txt", "w", encoding="utf-8")
        file.write(speech_text)
        file.close()

        # Get filepath
        file_path = os.getcwd() + "\\Address Files\\" + element.text + ".txt"

        # Insert tuple into SQL table
        speech_text = speech_text.replace("'", "''")
        cursor.execute("INSERT INTO ADDRESS_TABLE VALUES('"+name+"', '"+date+"', '"+link+"', '"+speech_text+"', '"+file_path+"');")

        print(name + "\t" + date)


main()
