from lxml import html, etree
import requests

zip_codes = [44101, 44102, 44103, 44104, 44105, 44106, 44107, 44108, 44109, 44110, 44111, 44112, 44113, 44114,
             44115, 44117, 44119, 44120, 44121, 44122, 44125, 44127, 44128, 44129, 44130, 44134, 44135, 44142, 44144]

provider_functs = {
                'Viasat': viasat, 
                'HughesNet': hughesnet,
                'Ooma': ooma, 
                'T-Mobile': tmobile, 
                'AT&T Wireless': att, 
                'Verizon Wireless': verizon,
                'AT&T': att, 
                'EarthLink': earthling,
                'Spectrum': spectrum, 
                'WOW!': wow, 
                'Cox Communications': cox
            }


def main():
    f = open("data.json", "w")
    f.write("{\n")
    for code in zip_codes:
        link = f"https://www.highspeedinternet.com/oh/cleveland?zip={code}"
        f.write(f'"{code}": ' + "{\n")

        # Create a list of tags for options
        options_list = html_element_tree.xpath(
            "//div[@class='row collapse provider-card provider-card--item  margin-bottom '] | //div[@class='row collapse provider-card provider-card--item main-card margin-bottom ']")

        for option in options_list:
            provider_name = providers.append(option.attrib["data-brand"])
            f.write(f'"{provider_name}": [\n')
            link = option.
            f.write(provider_functs[provider_name(link)])
            f.write("]\n,")

        f.write("},\n")

    f.write("}")


if __name__ == "__main__":
    main()
