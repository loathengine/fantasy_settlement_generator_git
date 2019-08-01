import xml.etree.ElementTree as ET
import random

random.seed(12345)


def parse_xml_biome():
    tree = ET.parse('data/biome.xml')
    root = tree.getroot()
    xml_list = []
    for biome in root.iter('BIOME'):
        xml_list.append(biome.get('name'))
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


def parse_xml_craft():
    tree = ET.parse('data/industry.xml')
    root = tree.getroot()
    xml_list = []

    for r in root.iter('RAW'):
        raw = r.get('name')
        for craft in r.iter('CRAFT'):
            name_weight = []
            name = craft.get('name')
            weight = craft.get('weight')
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
primary_biome = random.choice(parse_xml_biome())


def get_primary_topology(pb=primary_biome, xml_topo=parse_xml_topography()):
    length=len(xml_topo)
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


def get_settlement_shops(ssn=settlement_shops_num):
    length=len(xml_topo)
    topo_list = []
    for topo in xml_topo:
        if topo[0] == pb:
            i = int(topo[2])
            while i > 0:
                topo_list.append(topo[1])
                i -= 1
    return random.choice(topo_list)


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

print(parse_xml_raw())
