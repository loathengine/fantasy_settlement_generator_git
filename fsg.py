#TODO:add functionality
# shop number and quality
# government and guards
# religion and stuff
# name generator
# tavern generator
# npc generator

import xml.etree.ElementTree as ET
import random

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
    """Takes a file and an element name and a count and returns a unigue dict of size count of that element."""
    dictionary = {}
    x = 0
    while x < count:
        results = weighted_element_xml(xml_file, element_root)
        if results[0] not in dictionary:
            dictionary[results[0]] = [results[1], results[2]]
            x += 1
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


def get_settlement_shops(xml_file, element_root, ssn):
    ssn = 1 + ssn // 5
    shop_dict = {}
    x = 0
    while x < ssn:
        x += 1
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


settlement_name = "Testberg"
settlement_population = random.randint(20, 50000)
settlement_label = get_settlement_label('data/monolith.xml', "./STATS/LABEL", settlement_population)
settlement_density = random.randint(3, 6)
settlement_wealth = random.randint(1, 6)
settlement_age = weighted_element_xml('data/monolith.xml', "./STATS/AGE")
settlement_alignment = random.randint(1, 6)
settlement_government = weighted_element_xml('data/monolith.xml', "./STATS/GOVERNMENT")
settlement_trait = weighted_element_xml('data/monolith.xml', "./STATS/TRAIT")
settlement_structures = ((settlement_population << 1) // settlement_density) >> 1
settlement_shops_num = 1 + (settlement_population // 150)
settlement_inn_num = (settlement_population // 1500)
settlement_tavern_num = (settlement_population // 1000)
primary_biome = weighted_element_xml('data/monolith.xml', "./ENV/*")
primary_topography = weighted_element_xml('data/monolith.xml', "./ENV/BIOME[@name='" + primary_biome[0] + "']/*")
industry_raw = weighted_element_xml('data/monolith.xml',
                                    "./ENV/BIOME/TOPOGRAPHY[@name='" + primary_topography[0] + "']/*")
settlement_shops = get_settlement_shops('data/monolith.xml',
                                        "./ENV/BIOME/TOPOGRAPHY/RAW/[@name='" + industry_raw[0] + "']/*",
                                        settlement_shops_num)
settlement_races = xml_element_dict_all('data/monolith.xml', "./STATS/RACE")
district_number = random.randint(1, 6)
district_info = xml_element_dict_count('data/monolith.xml', "./STATS/DISTRICT", district_number)

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
    " and the local surroundings are under the control of " + settlement_government[0] + ".  ")
print("#### Demographics")
print("___")
print("- **Name: **" + settlement_name)
print("- **Population: **" + str(settlement_population))
print("- **Number by race: **")
for x, y in settlement_races.items():
    print(x + " " + y[0] + "%,")
print("- **Size: **" + settlement_label)
print("- **Wealth: **" + str(settlement_wealth))
print("- **Age: **" + str(settlement_age[0]))
print("- **Alignment: **" + str(settlement_alignment))
print("- **Government Type: **" + settlement_government[0])
print("- **Settlement Trait: **" + settlement_trait[0])
print("\n")
print("#### Industry and Economy")
print("___")
print("- **Primary Raw Materials: **" + industry_raw[0])
print("- **Number Of Structures: **" + str(settlement_structures))
print("- **Number Of Shops: **" + str(settlement_shops_num))
print("- **Shops of Note: **")
for x, y in settlement_shops.items():
    print(x + ",")
print("\n")
print("#### Food and Hospitality")
print("___")
print("- **Available Inns: **" + str(settlement_inn_num))
print("- **Operating Taverns: **" + str(settlement_tavern_num))
print("\n")
print("### Districts")
for x, y in district_info.items():
    print("##### " + x)
    print(y[1])
print("\n")
print("### Notable Inns/Taverns")
print("## Carpenter's Cup")
print("#####  Location")
print("In The Star ward, near an outcrop of rune-carved stone.")
print("##### Description")
print("The inn is a simple wooden shack, with several shuttered windows. Several battered shields hang on the walls. Accomodations consist of a few small rooms with straw mats and straw mats near the hearth.")
print("##### Innkeeper")
print("The innkeeper is a tall male human named Monder.")
print("##### Menu")
print("* Boiled Eggs and Dried Leek, Tankard of Stout (10 cp)")
print("* Roasted Mutton and Dried Turnip, Tankard of Mead (10 cp)")
print("* Stewed Onions, Mug of Cider (5 cp)")
print("* Stewed Lentils, Mug of Cider (3 cp)")
print("* Roasted Cabbage, Mug of Stout (4 cp)")
print("* Stewed Lentils, Mug of Perry (4 cp)")
print("* Pottage, Mug of Perry (4 cp)")