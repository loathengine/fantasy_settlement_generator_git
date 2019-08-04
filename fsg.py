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
    xml_set = set(xml_list)
    unique_xml_list = list(xml_set)
    return unique_xml_list


def weighted_element_xml(xml_file, element_root):
    #print('xml file - ' + xml_file)
    tree = ET.parse(xml_file)
    root = tree.getroot()
    weighted_list = []
    print(element_root)
    for e in root.findall(element_root):
        print(e)
        #print('    e - ' + str(e.get('name')))
        name = e.get('name')
        #print('    name - ' + name)
        weight = e.get('weight')
        #print('    weight - ' + weight)
        i = int(weight)
        while i > 0:
            #print('        adding ' + name + ' to list')
            weighted_list.append(name)
            i -= 1
    return random.choice(weighted_list)

def get_settlement_shops(ssn, ir, xml_shop):
    print('ir is - ' + ir)
    length = len(xml_shop)
    shop_list = []
    shop_results = ""
    shop_dict = {}
    i = 0
    x = length
    while x < ssn:
        x += 1
        print('xml_shop is - ' + str(xml_shop))
        for shop in xml_shop:
            print(shop)
            print(ir)
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


settlement_name = "Testberg"
settlement_population = random.randint(100, 5000)
settlement_density = random.randint(1, 6)
settlement_wealth = random.randint(1, 6)
settlement_age = random.randint(1, 6)
settlement_structures = ((settlement_population << 1) // settlement_density) >> 1
settlement_shops_num = (settlement_population // 150)
settlement_shops_list = (parse_xml_element('data/biome.xml', 'SHOP', 'name'))
primary_biome = weighted_element_xml('data/biome.xml', "./BIOME/*")
#primary_topology = weighted_element_xml('data/biome.xml', "./BIOME[@name=" + primary_biome + "]/*")
#industry_raw = weighted_element_xml('data/biome.xml', "./BIOME[@name=" + primary_biome + "]/TOPOGRAPHY[@name=" + primary_topology + "]/*")
# settlement_shops = get_settlement_shops(settlement_shops_num, industry_raw, settlement_shops_list)

# print("settlement_name - " + settlement_name)
# print("settlement_population - " + str(settlement_population))
# print("settlement_density - " + str(settlement_density))
# print("settlement_wealth - " + str(settlement_wealth))
# print("settlement_age - " + str(settlement_age))
# print("settlement_structures - " + str(settlement_structures))
# print("primary_biome - " + primary_biome)
# print("primary_topology - " + primary_topology)
# print("industry_raw - " + industry_raw)
# print("settlement_shops_num - " + str(settlement_shops_num))
# print("settlement_shop_list - " + str(settlement_shops_list))
# print('     Shop Type -- Number')
# print('     -------------------')

# for x,y in settlement_shops.items():
#    print('     ' + x + " " + str(y))

i = 0
while i < 10:
    i += 1
#    print(weighted_element_xml('data/biome.xml', "./BIOME[@name='tundra']/TOPOGRAPHY[@name='coastal']/*"))
print(primary_biome)
