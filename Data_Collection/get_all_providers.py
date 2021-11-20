from lxml import html, etree
import requests

zip_codes = [44101, 44102, 44103, 44104, 44105, 44106, 44107, 44108, 44109, 44110, 44111, 44112, 44113, 44114,
             44115, 44117, 44119, 44120, 44121, 44122, 44125, 44127, 44128, 44129, 44130, 44134, 44135, 44142, 44144]


def main():
    providers = []
    for code in zip_codes:
        link = f"https://www.highspeedinternet.com/oh/cleveland?zip={code}"

        # Get webpage content
        html_string = requests.get(link).content
        # Convert string into element tree object
        element_html = html.fromstring(html_string)
        html_element_tree = etree.ElementTree(element_html)

        # Create a list of tags for options
        options_list = html_element_tree.xpath(
            "//div[@class='row collapse provider-card provider-card--item main-card margin-bottom ']")

        # Get all new providers
        for option in options_list:
            if option.attrib["data-brand"] not in providers:
                providers.append(option.attrib["data-brand"])

    print(providers)


if __name__ == "__main__":
    main()
