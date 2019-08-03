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




def parse_xml_topography():
    tree = ET.parse('data/biome.xml')
    root = tree.getroot()
    xml_list = []

    for b in root.iter('BIOME'):
        biome = b.get('name')
        for topo in b.iter('TOPOGRAPHY'):
            name_weight = []
            name = topo.get('name')
            weight = topo.get('weight')
            name_weight.append(biome)
            name_weight.append(name)
            name_weight.append(weight)
            xml_list.append(name_weight)
    return xml_list


def parse_xml_raw():
    tree = ET.parse('data/industry.xml')
    root = tree.getroot()
    xml_list = []
    for raw in root.iter('RAW'):
        xml_list.append(raw.get('name'))
    return xml_list


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
primary_biome = random.choice(parse_xml_element('data/biome.xml', 'BIOME', 'name'))


def get_primary_topology(pb=primary_biome, xml_topo=parse_xml_topography()):
    length = len(xml_topo)
    topo_list = []
    for topo in xml_topo:
        if topo[0] == pb:
            i = int(topo[2])
            while i > 0:
                topo_list.append(topo[1])
                i -= 1
    return random.choice(topo_list)


primary_topology = get_primary_topology()


def get_industry_raw(ir=parse_xml_raw()):
    return random.choice(ir)


industry_raw = get_industry_raw()


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

print(parse_xml_topography())
print(get_primary_topology())

