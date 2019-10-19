#TODO:add functionality
# shop number and quality
# government and guards
# religion and stuff
# name generator
# tavern generator
# npc generator

import xml.etree.ElementTree as ET
import random
import string

random.seed(random.randint(100, 100000))


# random.seed(86753099)


def weighted_element_xml(xml_file, element_root):
    """Takes a file and an element name and returns a weighted random result"""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    weighted_list = []
    for e in root.findall(element_root):
        name = e.get('name')
        weight = e.get('weight')
        description = e.get('desc')
        i = int(weight)
        while i > 0:
            weighted_list.append([name, weight, description])
            i -= 1
    return random.choice(weighted_list)


def xml_element_dict_all(xml_file, element_root):
    """Takes a file and an element name and returns a dict of every unique instance of that element."""
    """Format: key, [weight, description]"""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    xml_dict = {}
    for e in root.findall(element_root):
        name = e.get('name')
        weight = e.get('weight')
        description = e.get('desc')
        xml_dict[name] = [weight, description]
    return xml_dict


def xml_element_dict_count(xml_file, element_root, count):
    """Takes a file and an element name and a count and returns a unique dict of size count of that element."""
    dictionary = {}
    while count > 0:
        results = weighted_element_xml(xml_file, element_root)
        if results[0] not in dictionary:
            dictionary[results[0]] = [results[1], results[2]]
            count -= 1
    return dictionary


def xml_element_list_unique(xml_file, element, attribute):
    """Takes a file and an element name and returns a list of every unique instance of that element."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    xml_list = []
    for e in root.iter(element):
        xml_list.append(e.get(attribute))
    xml_set = set(xml_list)
    unique_xml_list = list(xml_set)
    return unique_xml_list


def xml_element_list_unique_count(xml_file, element, attribute, count):
    """Takes a file and an element name and returns a unique list of or size count for that element."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    xml_list = []
    for e in root.iter(element):
        xml_list.append(e.get(attribute))
    xml_set = set(xml_list)
    unique_xml_list = list(xml_set)
    return random.sample(unique_xml_list, count)


def get_settlement_shops(xml_file, element_root, ssn):
    ssn = 1 + ssn // 5
    shop_dict = {}
    while ssn > 0:
        ssn -= 1
        shop_results = weighted_element_xml(xml_file, element_root)
        if shop_results[0] in shop_dict:
            shop_dict[shop_results[0]] += 1
        else:
            shop_dict[shop_results[0]] = 1
    return shop_dict


def get_settlement_label(xml_file, element_root, settlement_pop):
    # TODO: Need to sort data before doing the size checks
    tree = ET.parse(xml_file)
    root = tree.getroot()
    settlement_list = ""
    for e in root.findall(element_root):
        name = e.get('name')
        ceiling = e.get('ceiling')
        i = int(ceiling)
        if i < settlement_pop:
            settlement_list = name
    return settlement_list


def npc_generator():
    return "Bob"


def get_settlement_tavern(t_n, t_l):
    # TODO: Name=settlement_tavern_name, Location=district_info, Description, Innkeeper, Menu, Patrons
    xml_dict = {}
    for name in t_n:
        tavern_name = name
        tavern_location = random.choice(list(t_l))
        tavern_description = weighted_element_xml('data/monolith.xml', "./STATS/TAVERN_DESC")
        tavern_innkeeper = npc_generator()
        tavern_menu = list(xml_element_dict_count('data/monolith.xml', "./STATS/TAVERN_MENU", 5))
        xml_dict[tavern_name] = [tavern_location, tavern_description[0], tavern_innkeeper, tavern_menu[0],
                                 tavern_menu[1], tavern_menu[2], tavern_menu[3], tavern_menu[4]]
    return xml_dict


settlement_name = str(weighted_element_xml('data/monolith.xml', "./STATS/SIGN")[0])
settlement_population = random.randint(300, 5000)
settlement_label = get_settlement_label('data/monolith.xml', "./STATS/LABEL", settlement_population)
settlement_density = random.randint(1, 10)
settlement_wealth = random.randint(1, 6)
settlement_age = weighted_element_xml('data/monolith.xml', "./STATS/AGE")
settlement_alignment = random.randint(1, 6)
settlement_government = weighted_element_xml('data/monolith.xml', "./STATS/GOVERNMENT")
settlement_trait = weighted_element_xml('data/monolith.xml', "./STATS/TRAIT")
settlement_wards = 6 + (settlement_population // settlement_density) // 100
settlement_shops_num = 1 + (settlement_population // 150)

primary_biome = weighted_element_xml('data/monolith.xml', "./ENV/*")
primary_topography = weighted_element_xml('data/monolith.xml', "./ENV/BIOME[@name='" + primary_biome[0] + "']/*")
industry_raw = weighted_element_xml('data/monolith.xml',
                                    "./ENV/BIOME/TOPOGRAPHY[@name='" + primary_topography[0] + "']/*")
settlement_shops = get_settlement_shops('data/monolith.xml',
                                        "./ENV/BIOME/TOPOGRAPHY/RAW/[@name='" + industry_raw[0] + "']/*",
                                        settlement_shops_num)

settlement_races = xml_element_dict_all('data/monolith.xml', "./STATS/RACE")
district_number = random.randint(3, 9)
district_info = xml_element_dict_count('data/monolith.xml', "./STATS/DISTRICT", district_number)

settlement_tavern_num = (2 + settlement_population // 3000)
settlement_tavern_names = xml_element_dict_count('data/monolith.xml', "./STATS/TAVERN_NAME", settlement_tavern_num)
settlement_taverns = get_settlement_tavern(settlement_tavern_names, district_info)

print("# " + settlement_name)
print("\n")
print("<div class='wide'>")
print("<img src='https://i.imgur.com/TXNeTYQ.png' style='width:700px' />")
print("</div>")
print("\n")
print("### Background")
print("Add background flavor.")
print("\n")
print("\page")
print("\n")
print("## Settlement Features")
print(
    settlement_name + " is a " + settlement_label + " located in the " + primary_topography[0] + " region of the areas "
    + "greater " + primary_biome[0] + ".  The settlement seems to be " + settlement_age[0] + ".  " + settlement_name +
    " and the local surroundings are under the control of " + settlement_government[0] + ".")
print("\n")
print("#### Demographics")
print("___")
print("- **Name: **" + settlement_name)
print("- **Population: **" + str(settlement_population))
print("- **Number by race: **")
for x, y in settlement_races.items():
    print(string.capwords(x) + " " + y[0] + "%,")
print("- **Size: **" + string.capwords(settlement_label))
print("- **Wealth: **" + str(settlement_wealth))
print("- **Age: **" + string.capwords(settlement_age[0]))
print("- **Alignment: **" + str(settlement_alignment))
print("- **Government Type: **" + string.capwords(settlement_government[0]) + " - " + settlement_government[2])
print("- **Settlement Trait: **" + settlement_trait[0])
print("- **Number Of Wards: **" + str(settlement_wards))
print("- **Number of Districts: ** " + str(district_number) )
print("\n")
print("#### Industry and Economy")
print("___")
print("- **Primary Raw Materials: **" + string.capwords(industry_raw[0]))
print("- **Number Of Shops: **" + str(settlement_shops_num))
print("- **Shops of Note: **")
for x in settlement_shops.keys():
    if x == list(settlement_shops.keys())[-1]:
        print(x + ".")
    else:
        print(x + ",")
print("- **Number Of Inns/Taverns: **" + str(settlement_tavern_num))
print("- **Inns/Taverns of Note: **")
for x in settlement_tavern_names.keys():
    if x == list(settlement_tavern_names.keys())[-1]:
        print(x + ".")
    else:
        print(x + ",")
print("\n")

print("### Districts")
for x, y in district_info.items():
    print("##### " + x)
    print(y[1])
print("\n")

for x, y in settlement_taverns.items():
    print("## " + x)
    print("#####  Location")
    print(y[0])
    print("##### Description")
    print(y[1])
    print("##### Innkeeper")
    print(y[2])
    print("##### Menu")
    print("* " + y[3])
    print("* " + y[4])
    print("* " + y[5])
    print("* " + y[6])
    print("* " + y[7])
    print("\n")