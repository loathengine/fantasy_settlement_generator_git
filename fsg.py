import xml.etree.ElementTree as ET
import random

random.seed(random.randint(1, 100000))


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
    #print('xml file - ' + xml_file)
    tree = ET.parse(xml_file)
    root = tree.getroot()
    weighted_list = []
    #print(element_root)
    for e in root.findall(element_root):
        #print(e)
        #print('    e - ' + str(e.get('name')))
        name = e.get('name')
        #print('    name - ' + name)
        weight = e.get('weight')
        #print('    weight - ' + weight)
        i = int(weight)
        while i > 0:
            #print('        adding ' + name + ' to list, weight - ' + str(i))
            weighted_list.append(name)
            i -= 1
    return random.choice(weighted_list)

def get_settlement_shops(ssn, xml_shop):
    shop_results = ""
    shop_dict = {}
    x = 0
    while x < ssn:
        x += 1
        shop_results = random.choice(xml_shop)
        if shop_results in shop_dict:
            shop_dict[shop_results] += 1
        else:
            shop_dict[shop_results] = 1
    return shop_dict

def get_settlement_label(xml_file, element_root, settlement_population):
    """Need to sort data before doing the size checks"""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    settlement_label = ""
    for e in root.findall(element_root):
        name = e.get('name')
        ceiling = e.get('ceiling')
        i = int(ceiling)
        if i >= settlement_population:
            settlement_label = name
    return settlement_label


settlement_name = "Testberg"
settlement_population = random.randint(100, 5000)
settlement_label = get_settlement_label('data/monolith.xml', "./STATS/LABEL", settlement_population)
settlement_density = random.randint(3, 6)
settlement_wealth = random.randint(1, 6)
settlement_age = random.randint(1, 6)
settlement_alignment = random.randint(1, 6)
settlement_government = weighted_element_xml('data/monolith.xml', "./STATS/GOVERNMENT")
settlement_trait = weighted_element_xml('data/monolith.xml', "./STATS/TRAIT")
settlement_structures = ((settlement_population << 1) // settlement_density) >> 1
settlement_shops_num = (settlement_population // 150)
settlement_shops_list = (parse_xml_element('data/monolith.xml', 'SHOP', 'name'))
primary_biome = weighted_element_xml('data/monolith.xml', "./ENV/*")
primary_topography = weighted_element_xml('data/monolith.xml', "./ENV/BIOME[@name='" + primary_biome + "']/*")
industry_raw = weighted_element_xml('data/monolith.xml', "./ENV/BIOME/TOPOGRAPHY[@name='" + primary_topography + "']/*")
settlement_shops = get_settlement_shops(settlement_shops_num, settlement_shops_list)

print("settlement_name - " + settlement_name)
print("settlement_population - " + str(settlement_population))
print("settlement_label - " + settlement_label)
print("settlement_wealth - " + str(settlement_wealth))
print("settlement_age - " + str(settlement_age))
print("settlement_alignment - " + str(settlement_alignment))
print("settlement_government - " + settlement_government)
print("settlement_trait - " + settlement_trait)
print("settlement_structures - " + str(settlement_structures))
print("primary_biome - " + primary_biome)
print("primary_topography - " + primary_topography)
print("industry_raw - " + industry_raw)
print("settlement_shops_num - " + str(settlement_shops_num))
print("settlement_shop_list - " + str(settlement_shops_list))
print('     Shop Type -- Number')
print('     -------------------')
for x,y in settlement_shops.items():
    print('     ' + x + " -- " + str(y))

