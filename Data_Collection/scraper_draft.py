from lxml import html, etree
import requests


def att_scraper(address):
    options = []
    return options


def spectrum_scraper(address):
    options = []
    return options


def viasat_scraper(address):
    link = "https://buy.viasat.com/static/media/MaterialCommunityIcons.a7629910.ttf"
    parameters = {}
    r = requests.get(link, data = parameters)
    print(r.text)

    options = []
    return options


def earthlink_scraper(address):
    provider = "EarthLink"
    cost = "Call Company For Cost"
    link = f'https://results.earthlink.com/?address={address}'

    # Get webpage content
    html_string = requests.get(link).content
    # Convert string into element tree object
    element_html = html.fromstring(html_string)
    html_element_tree = etree.ElementTree(element_html)

    # Create a list of tags for options
    options_list = html_element_tree.xpath(
        "//div[@class='productContainer listings']")

    # Get options
    options = []
    for element in options_list:
        tree = etree.ElementTree(element)
        name = ""
        rate = str(tree.xpath("//div[@class='listingSpeed']/span[@class='listingSpeedMbps']")[0].text)
        speed = str(tree.xpath("//div[@class='listingSpeed']/div[@class='speed']")[0].text) + (" " + rate if rate != "None" else "")
        options.append((provider, speed, cost))

    return options


def format_adr(address):
    return address


def main():
    address = "3806 Schiller Ave, Cleveland, OH, 44144"
    address = format_adr(address)

    available = []

    available.extend(att_scraper(address))
    available.extend(spectrum_scraper(address))
    available.extend(viasat_scraper(address))
    available.extend(earthlink_scraper(address))

    for element in available:
        print(element)


if __name__ == "__main__":
    main()
