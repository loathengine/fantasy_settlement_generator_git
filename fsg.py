#TODO:add functionality
# figure out race stuff
# shop number and quality
# government and guards
# religion and stuff
# tavern generator
# npc generator

import xml.etree.ElementTree as ET
import random

random.seed(random.randint(100, 100000))
#random.seed(86753099)


def parse_xml_element(xml_file, element, attribute):
    """Takes a file and an element name and returns a list of every unique instance of that element."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    xml_list = []
    for e in root.iter(element):
        xml_list.append(e.get(attribute))
    xml_set = set(xml_list)
    unique_xml_list = list(xml_set)
    return unique_xml_list


def weighted_element_xml(xml_file, element_root):
    """Takes a file and an element name and returns a weighted random result"""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    weighted_list = []
    for e in root.findall(element_root):
        name = e.get('name')
        weight = e.get('weight')
        i = int(weight)
        while i > 0:
            weighted_list.append(name)
            i -= 1
    return random.choice(weighted_list)


def get_settlement_shops(ssn):
    ssn = 1 + ssn // 5
    shop_dict = {}
    x = 0
    while x < ssn:
        x += 1
        shop_results = weighted_element_xml('data/monolith.xml', "./ENV/BIOME/TOPOGRAPHY/RAW/[@name='" + industry_raw + "']/*")
        if shop_results in shop_dict:
            shop_dict[shop_results] += 1
        else:
            shop_dict[shop_results] = 1
    return shop_dict


def get_settlement_label(xml_file, element_root, settlement_population):
    # TODO: Need to sort data before doing the size checks
    tree = ET.parse(xml_file)
    root = tree.getroot()
    settlement_label = ""
    for e in root.findall(element_root):
        name = e.get('name')
        ceiling = e.get('ceiling')
        i = int(ceiling)
        if i < settlement_population:
            settlement_label = name
    return settlement_label


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
primary_topography = weighted_element_xml('data/monolith.xml', "./ENV/BIOME[@name='" + primary_biome + "']/*")
industry_raw = weighted_element_xml('data/monolith.xml', "./ENV/BIOME/TOPOGRAPHY[@name='" + primary_topography + "']/*")
settlement_shops = get_settlement_shops(settlement_shops_num)

print("# " + settlement_name)
print("\n")
print("<div class='wide'>")
print("<img src='https://i.imgur.com/iMA7lg9.png' style='width:700px' />")
print("</div>")
print("\n")
print("### Background")
print("Add background flavor.")
print("\n")
print("## Settlement Features")
print(settlement_name + " is a " + settlement_label + " located in the " + primary_topography + " region of the areas "
      + "greater " + primary_biome + ".  The settlement seems to be " + settlement_age + ".  " + settlement_name +
      " and the local surroundings are under the control of the " + settlement_government + ".  "  )
print("#### Demographics")
print("___")
print("- **Name: **" + settlement_name)
print("- **Population: **" + str(settlement_population))
print("- **Number by race: ** Human 100% ")
print("- **Size: **" + settlement_label)
print("- **Wealth: **" + str(settlement_wealth))
print("- **Age: **" + str(settlement_age))
print("- **Alignment: **" + str(settlement_alignment))
print("- **Government Type: **" + settlement_government)
print("- **Settlement Trait: **" + settlement_trait)
print("\n")
print("#### Industry and Economy")
print("___")
print("- **Primary Raw Materials: **" + industry_raw)
print("- **Number Of Structures: **" + str(settlement_structures))
print("- **Number Of Shops: **" + str(settlement_shops_num))
print("- **Shops of Note: **")
for x,y in settlement_shops.items():
    print(x + ",")
print("\n")
print("#### Food and Hospitality")
print("___")
print("- **Available Inns: **" + str(settlement_inn_num))
print("- **Operating Taverns: **" + str(settlement_tavern_num))
print("\n")
print("### Districts")
print("1. Receb's Yards - This area contains the spiritual grounds of Areksul.  Named after the bishop Receb whom for decades tirelessly spent his fortune turning the area into a beautiful place for all to worship.  A true Omnist.  'Receb the Purifier' was found dead having choked to death ravenously feasting on the entrails of children.  The remains of thousands where found in his personal home.  No one quite knows where the children came from because the number would be unsupportable by even a large city.  The lanes are lined with husks of worship much like a row of rotten teeth in the mandible of a long dead carnivore.  New and old are indistinguishable.  Sometimes you can here the trumpets of a seeker finding their faith.  No many local residents enter this area.")
print("2. Wodogrenk Point - Contains a barracks and large parade grounds.  While well maintained the barracks is minimally staffed by ordinary road guard.")
print("3. Clottiam West - Is quit old and houses not only the mayors house but also a few inns and taverns along with other businesses.  The building are quite ancient but well maintain and actually quite cozy.")
print("4. Five Bowls - The west gate is where most of the trade occurs.  To the north is a shared square where a small but seeming perpetual farmers market exists.  This district seem to support not just the locals but also the tradesmen and travelers on road from the capital.")
print("\n")
print("### Notable Inns/Taverns")
print("## Carpenter's Cup")
print("#####  Location")
print("In a Clottiam West ward, near an outcrop of rune-carved stone.")
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

