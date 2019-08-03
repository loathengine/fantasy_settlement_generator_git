import xml.etree.ElementTree as ET
import random

random.seed(random.randint(1, 100000))

def parse_xml_element(xml_file, element, attribute):
    """Takes a file and an element name and returns a list of every instance of that element."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    xml_list = []
    for e in root.iter(element):
        xml_list.append(e.get(attribute))
    return xml_list


def weighted_element_xml(xml_file, element1, element2):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    weighted_list = []
    i=0

    for e1 in root.iter(element1):
        e1_name = e1.get('name')
        for e2 in e1.iter(element2):
            name = e2.get('name')
            weight = e2.get('weight')
            i = int(weight)
            while i > 0:
                weighted_list.append(name)
                i -= 1
    return random.choice(weighted_list)

def parse_xml_shop():
    tree = ET.parse('data/industry.xml')
    root = tree.getroot()
    xml_list = []

    for r in root.iter('RAW'):
        raw = r.get('name')
        for shop in r.iter('SHOP'):
            name_weight = []
            name = shop.get('name')
            weight = shop.get('weight')
            name_weight.append(raw)
            name_weight.append(name)
            name_weight.append(weight)
            xml_list.append(name_weight)
    return xml_list


settlement_name = "Testberg"
settlement_population = random.randint(5, 5000)
settlement_density = random.randint(1, 6)
settlement_wealth = random.randint(1, 6)
settlement_age = random.randint(1, 6)
settlement_structures = ((settlement_population << 1) // settlement_density) >> 1
settlement_shops_num = (settlement_population // 150)
primary_biome = weighted_element_xml('data/biome.xml', 'ENV', 'BIOME')
primary_topology = weighted_element_xml('data/biome.xml', 'BIOME', 'TOPOGRAPHY')
industry_raw = weighted_element_xml('data/industry.xml', 'IND', 'RAW')



def get_settlement_shops(ssn=settlement_shops_num, ir=industry_raw, xml_shop=parse_xml_shop()):
    length = len(xml_shop)
    shop_list = []
    shop_results = ""
    shop_dict = {}
    i = 0
    x = 0
    while x < ssn:
        x += 1
        for shop in xml_shop:
            if shop[0] == ir:
                i = int(shop[2])
            while i > 0:
                shop_list.append(shop[1])
                i -= 1
        shop_results = random.choice(shop_list)
        if shop_results in shop_dict:
            shop_dict[shop_results] += 1
        else:
            shop_dict[shop_results] = 1
    return shop_dict


settlement_shops = get_settlement_shops()

print("settlement_name - " + settlement_name)
print("settlement_population - " + str(settlement_population))
print("settlement_density - " + str(settlement_density))
print("settlement_wealth - " + str(settlement_wealth))
print("settlement_age - " + str(settlement_age))
print("settlement_structures - " + str(settlement_structures))
print("primary_biome - " + primary_biome)
print("primary_topology - " + primary_topology)
print("industry_raw - " + industry_raw)
print("settlement_shops_num - " + str(settlement_shops_num))

print('     Shop Type -- Number')
print('     -------------------')
for x,y in settlement_shops.items():
    print('     ' + x + " " + str(y))

