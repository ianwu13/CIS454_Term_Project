from lxml import html, etree
import requests

zip_codes = [44101, 44102, 44103, 44104, 44105, 44106, 44107, 44108, 44109, 44110, 44111, 44112, 44113, 44114,
             44115, 44117, 44119, 44120, 44121, 44122, 44125, 44127, 44128, 44129, 44130, 44134, 44135, 44142, 44144]


def viasat(zip):
    link = "https://www.viasatspecials.com/lp/internet?clientId=1596336467.1637439482&kbid=88467&utm_source=highspeedinternet.com&utm_medium=affiliate&clreqid=7932a863-34a1-4ecd-af0e-9611daaa61b3&state=oh&city=cleveland&zip=44111"
    
    names = ["Unlimited Bronze 12", "Unlimited Silver 12", "Unlimited Gold 12"]
    speeds = ["Up to 12 Mbps (35GB High Speed Data)", "Up to 12 Mbps (45GB High Speed Data)", "Up to 12 Mbps (65GB High Speed Data)"]
    prices = ["$69.99/mo", "$99.99/mo", "$149.99/mo"]

    out_string = ""
    for plan in range(3):
        plan_string = '{ "plan_name": '
        plan_name = names[plan]
        plan_string += f'"{plan_name}","speed": '
        speed = speeds[plan]
        plan_string += f'"{speed}","price": '
        price = prices[plan]
        out_string += plan_string + f'"{price}"' + "},"
    return out_string[:-1]


def hughesnet(zip):
    link = "https://www.hughesnet.com/?campaignid=249598CLRef&mid_code=249598CLRef&phone_number=844-406-1664&utm_campaign=CLRef&utm_medium=referral&utm_source=referral&site_url=www.hughesnet.com"
    # Get webpage content
    html_string = requests.get(link).content
    # Convert string into element tree object
    element_html = html.fromstring(html_string)
    html_element_tree = etree.ElementTree(element_html)
    plan_string = '{ "plan_name": '
    plan_name = "HughesNet Recommended"
    plan_string += f'"{plan_name}","speed": '
    speed = "25 Mbps"
    plan_string += f'"{speed}","price": '
    price = "$49.99/mo."
    plan_string += f'"{price}"' + "},"
    return plan_string[:-1]


def att(zip):
    link = "https://www.att.com/internet/fiber/?source=EPDxATFIB0000000L&dclid=CPfh6JWdqPQCFQa4lQIdipAMlw"
    # Get webpage content
    html_string = requests.get(link).content
    # Convert string into element tree object
    element_html = html.fromstring(html_string)
    html_element_tree = etree.ElementTree(element_html)

    # Get available plans
    plans_list = html_element_tree.xpath("//div[@class='pad-l-xs pad-r-xs pad-b-xs pad-t-xs rel']")

    out_string = ""
    for plan in plans_list:
        tree = etree.ElementTree(plan)
        plan_string = '{ "plan_name": '
        plan_name = "AT&T FIBER"
        plan_string += f'"{plan_name}","speed": '
        speed = tree.xpath("//p[@class='mar-b-xxxs font-medium color-ui-black type-md    ']")[0].text
        plan_string += f'"{speed}","price": '
        price = tree.xpath("//span[@class='type-xl font-medium']")[0].text_content() + "/mo."
        out_string += plan_string + f'"{price}"' + "},"
    return out_string[:-1]


def earthlink(zip):
    link = "https://higherspeed.earthlink.com/?dclid=CKy4qZedqPQCFcm8lQIdB6cMTg"
    # Get webpage content
    html_string = requests.get(link).content
    # Convert string into element tree object
    element_html = html.fromstring(html_string)
    html_element_tree = etree.ElementTree(element_html)

    # Get available plans
    plans_list = html_element_tree.xpath("//div[@class='upper-sec']")
    
    out_string = ""
    for plan in plans_list:
        tree = etree.ElementTree(plan)
        plan_string = '{ "plan_name": '
        plan_name = tree.xpath("//h2")[0].text_content()
        plan_string += f'"{plan_name}","speed": '
        speed = tree.xpath("//p")[0].text_content().replace("  ", "").replace("\n", "")
        plan_string += f'"{speed}","price": '
        price = "Call 844-592-4610 for pricing"
        out_string += plan_string + f'"{price}"' + "},"
    return out_string[:-1]


def spectrum(zip):
    link = f"https://www.cabletv.com/spectrum/internet-lp/?pid=HSI&clientId=1596336467.1637439482&kbid=88467&utm_source=highspeedinternet.com&utm_medium=affiliate&priority=366&clreqid=7932a863-34a1-4ecd-af0e-9611daaa61b3&state=oh&city=cleveland&zip={zip}"
    # Get webpage content
    html_string = requests.get(link).content
    # Convert string into element tree object
    element_html = html.fromstring(html_string)
    html_element_tree = etree.ElementTree(element_html)

    # Get available plans
    plans_list = html_element_tree.xpath("//div[@class='package-card__wrapper']")
    
    out_string = ""
    for plan in plans_list:
        tree = etree.ElementTree(plan)
        plan_string = '{ "plan_name": '
        plan_name = tree.xpath("//h2[@class='package-name']")[0].text
        plan_string += f'"{plan_name}","speed": '
        speed = "Download speeds up to 200 Mbps (Additional features may vary)"
        plan_string += f'"{speed}", "price": '
        price = tree.xpath("//div[@class='price-area__price']")[0].text_content().replace("\n", "").replace(" ", "").split("for")[0]
        out_string += plan_string + f'"{price}"' + "},"
    return out_string[:-1]


def wow(zip):
    link = f"https://wow-specials.com/?leadsourcecode=HSIWOWXCACE&apikey=prod-fHodqqPPl9i7nRsBeYdSQ%3D%3D&tfn=877-639-4643&clientId=1596336467.1637439482&kbid=88467&utm_source=highspeedinternet.com&utm_medium=affiliate&clreqid=7932a863-34a1-4ecd-af0e-9611daaa61b3&state=oh&city=cleveland&zip={zip}"
    # Get webpage content
    html_string = requests.get(link).content
    # Convert string into element tree object
    element_html = html.fromstring(html_string)
    html_element_tree = etree.ElementTree(element_html)

    plan_string = '{ "plan_name": '
    plan_string += '"High Speed Internet","speed": '
    plan_string += '"Up to 200 Mbps","price": '
    plan_string += '"$39.99 pre month"' + "}"
    return plan_string


def cox(zip):
    link = "https://www.cox.com/residential/internet.html?sc_id=clearlink_aff_z_z&dclid=CInUxeWcqPQCFZ-5lQIdpcoMgQ"
    # Get webpage content
    html_string = requests.get(link).content
    # Convert string into element tree object
    element_html = html.fromstring(html_string)
    html_element_tree = etree.ElementTree(element_html)

    # Get available plans
    plans_list = html_element_tree.xpath("//div[@id='spartanInternetLandingOfferList']")
    
    out_string = ""
    for plan in plans_list:
        tree = etree.ElementTree(plan)
        plan_string = '{ "plan_name": '
        plan_name = tree.xpath("//span[@class='fx-font-size-16px']")[0].text
        plan_string += f'"{plan_name}","speed": '
        speed = ""
        if plan_name == "Gigablast":
            speed = "940 Mbps"
        else:
            speed = plan_name.split(" ")[1]
        plan_string += f'"{speed}","price": '
        plan_name = tree.xpath("//span[@class='fx-font-size-32px price']")[0].text
        out_string += plan_string + f'"{price}"' + "},"
    return out_string[:-1]


provider_functs = {
    'Viasat': viasat,
    'HughesNet': hughesnet,
    'AT&T': att,
    'EarthLink': earthlink,
    'Spectrum': spectrum,
    'WOW!': wow,
    'Cox Communications': cox
}


def main():
    f = open("data.json", "w")
    f.write("{")
    for code in zip_codes:
        link = f"https://www.highspeedinternet.com/oh/cleveland?zip={code}"
        f.write(f'"{code}": ' + "{")

        # Get webpage content
        html_string = requests.get(link).content
        # Convert string into element tree object
        element_html = html.fromstring(html_string)
        html_element_tree = etree.ElementTree(element_html)
        # Create a list of tags for options
        options_list = html_element_tree.xpath("//div[@class='tabs-panel is-active']/div[@class='row collapse provider-card provider-card--item main-card margin-bottom ']")

        for i in range(len(options_list)-1):
            provider_name = options_list[i].attrib["data-brand"]
            f.write(f'"{provider_name}": [')
            tree = etree.ElementTree(options_list[i])
            link = tree.xpath("//a[@class='button large']")[0].attrib["href"]
            f.write(provider_functs[provider_name](code))
            f.write("],")
        provider_name = options_list[len(options_list)-1].attrib["data-brand"]
        f.write(f'"{provider_name}": [')
        tree = etree.ElementTree(options_list[i])
        link = tree.xpath("//a[@class='button large']")[0].attrib["href"]
        f.write(provider_functs[provider_name](code))
        f.write("]")

        f.write('},')

    f.write('"null": {}}')


if __name__ == "__main__":
    main()
