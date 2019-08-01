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


settlement_name = "Testberg"
settlement_population = random.randint(5, 5000)
settlement_density = random.randint(1, 6)
settlement_wealth = random.randint(1, 6)
settlement_age = random.randint(1, 6)
settlement_structures = ((settlement_population << 1) // settlement_density) >> 1
settlement_shops = (settlement_population // 150)
primary_biome = random.choice(parse_xml_biome())


def get_primary_topology(pb=primary_biome, xml_topo=parse_xml_topography()):
    length=len(xml_topo)
    for topo in xml_topo:
        if topo[0] == pb:
            print(pb)


    i = 0
    while i < length:
        print(xml_topo[i])
        i += 1

    return "ERROR40020"


primary_topology = get_primary_topology()


def get_industry_raw(pt=primary_topology, sp=settlement_population, sw=settlement_wealth):
    if pt == 'coastal':
        weighted_random_industry_raw = ['mining'] * 1 + ['farming'] * 1 + ['ranching'] * 1 + ['forestry'] * 1 + [
            'fishing'] * 999 + ['foraging'] * 1
        return random.choice(weighted_random_industry_raw)
    elif pt == 'river':
        weighted_random_industry_raw = ['mining'] * 1 + ['farming'] * 4 + ['ranching'] * 4 + ['forestry'] * 1 + [
            'fishing'] * 4 + ['foraging'] * 1
        return random.choice(weighted_random_industry_raw)
    elif pt == 'flat lands':
        weighted_random_industry_raw = ['mining'] * 1 + ['farming'] * 6 + ['ranching'] * 6 + ['forestry'] * 1 + [
            'fishing'] * 1 + ['foraging'] * 1
        return random.choice(weighted_random_industry_raw)
    elif pt == 'foot hills':
        weighted_random_industry_raw = ['mining'] * 1 + ['farming'] * 2 + ['ranching'] * 6 + ['forestry'] * 1 + [
            'fishing'] * 1 + ['foraging'] * 1
        return random.choice(weighted_random_industry_raw)
    elif pt == 'plateau':
        weighted_random_industry_raw = ['mining'] * 2 + ['farming'] * 1 + ['ranching'] * 1 + ['forestry'] * 4 + [
            'fishing'] * 2 + ['foraging'] * 1
        return random.choice(weighted_random_industry_raw)
    elif pt == 'mountain':
        weighted_random_industry_raw = ['mining'] * 6 + ['farming'] * 1 + ['ranching'] * 1 + ['forestry'] * 6 + [
            'fishing'] * 2 + ['foraging'] * 2
        return random.choice(weighted_random_industry_raw)
    else:
        return "ERROR40030"


industry_raw = get_industry_raw()


def get_industry_crafts(pt=primary_topology, ir=industry_raw, lic=None, sp=settlement_population, sw=settlement_wealth):
    if pt == 'coastal':
        weighted_random_industry_crafts = ['smith'] * 1 + ['tanner'] * 1 + ['weaver'] * 1 + ['mason'] * 1 + [
            'carpenter'] * 999 + ['butcher/salt packer'] * 1
        return random.choice(weighted_random_industry_crafts)
    elif pt == 'river':
        weighted_random_industry_crafts = ['smith'] * 1 + ['tanner'] * 1 + ['weaver'] * 1 + ['mason'] * 1 + [
            'carpenter'] * 999 + ['butcher/salt packer'] * 1
        return random.choice(weighted_random_industry_crafts)
    else:
        return "ERROR400040"


industry_crafts = get_industry_crafts()


def get_industry_services(lir=industry_raw, lic=industry_crafts, sp=settlement_population, sw=settlement_wealth):
    return "ERROR400050"


industry_services = get_industry_services()

print("settlement_name - " + settlement_name)
print("settlement_population - " + str(settlement_population))
print("settlement_density - " + str(settlement_density))
print("settlement_wealth - " + str(settlement_wealth))
print("settlement_age - " + str(settlement_age))
print("settlement_structures - " + str(settlement_structures))
print("settlement_shops - " + str(settlement_shops))
print("primary_biome - " + primary_biome)
print("primary_topology - " + primary_topology)
print("industry_raw - " + industry_raw)
print("industry_crafts - " + industry_crafts)
print("industry_services - " + industry_services)

print("\n\n" + str(parse_xml_topography()))
