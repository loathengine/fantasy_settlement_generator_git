
import random
random.seed( 12345 )

with open('data/primary_biome.txt') as file:
    list_primary_biome = file.read().splitlines()

with open('data/primary_topology.txt') as file:
    list_primary_topology = file.read().splitlines()

with open('data/industry_raw.txt') as file:
    list_industry_raw = file.read().splitlines()

with open('data/industry_crafts.txt') as file:
    list_industry_crafts = file.read().splitlines()

with open('data/industry_services.txt') as file:
    list_industry_services = file.read().splitlines()

settlement_name = "Testberg"
settlement_population = random.randint(5, 5000)
settlement_density = random.randint(1, 6)
settlement_wealth = random.randint(1, 6)
settlement_age = random.randint(1, 6)
settlement_structures = ((settlement_population << 1) // (settlement_density)) >> 1

def get_primary_biome(lpb = list_primary_biome):
    return random.choice(lpb)
primary_biome = get_primary_biome()

def get_primary_topology(lpt = list_primary_topology, pb = primary_biome):
    if pb == 'temperate deciduous forest':
        weighted_random_primary_topology = ['coastal'] * 1 + ['river'] * 1 + ['flat lands'] * 1 + ['foot hills'] * 1 + ['plateau'] * 1 + ['mountain'] * 1
        return random.choice(weighted_random_primary_topology)
    elif pb == 'temperate rain forest':
        weighted_random_primary_topology = ['coastal'] * 1 + ['river'] * 3 + ['flat lands'] * 1 + ['foot hills'] * 2 + ['plateau'] * 2 + ['mountain'] * 2
        return random.choice(weighted_random_primary_topology)
    elif pb == 'tropical rain forest':
        weighted_random_primary_topology = ['coastal'] * 3 + ['river'] * 3 + ['flat lands'] * 1 + ['foot hills'] * 1 + ['plateau'] * 1 + ['mountain'] * 4
        return random.choice(weighted_random_primary_topology)
    elif pb == 'tropical seasonal forest':
        weighted_random_primary_topology = ['coastal'] * 3 + ['river'] * 3 + ['flat lands'] * 1 + ['foot hills'] * 2 + ['plateau'] * 2 + ['mountain'] * 2
        return random.choice(weighted_random_primary_topology)
    elif pb == 'grassland':
        weighted_random_primary_topology = ['coastal'] * 3 + ['river'] * 3 + ['flat lands'] * 4 + ['foot hills'] * 3 + ['plateau'] * 1 + ['mountain'] * 1
        return random.choice(weighted_random_primary_topology)
    elif pb == 'savanna':
        weighted_random_primary_topology = ['coastal'] * 3 + ['river'] * 3 + ['flat lands'] * 4 + ['foot hills'] * 2 + ['plateau'] * 2 + ['mountain'] * 2
        return random.choice(weighted_random_primary_topology)
    elif pb == 'taiga':
        weighted_random_primary_topology = ['coastal'] * 3 + ['river'] * 3 + ['flat lands'] * 1 + ['foot hills'] * 2 + ['plateau'] * 2 + ['mountain'] * 2
        return random.choice(weighted_random_primary_topology)
    elif pb == 'cold desert':
        weighted_random_primary_topology = ['coastal'] * 1 + ['river'] * 1 + ['flat lands'] * 1 + ['foot hills'] * 4 + ['plateau'] * 4 + ['mountain'] * 4
        return random.choice(weighted_random_primary_topology)
    elif pb == 'hot desert':
        weighted_random_primary_topology = ['coastal'] * 3 + ['river'] * 3 + ['flat lands'] * 4 + ['foot hills'] * 1 + ['plateau'] * 4 + ['mountain'] * 1
        return random.choice(weighted_random_primary_topology)
    elif pb == 'tundra':
        weighted_random_primary_topology = ['coastal'] * 1 + ['river'] * 1 + ['flat lands'] * 1 + ['foot hills'] * 2 + ['plateau'] * 2 + ['mountain'] * 2
        return random.choice(weighted_random_primary_topology)
    elif pb == 'glacier':
        weighted_random_primary_topology = ['coastal'] * 3 + ['river'] * 3 + ['flat lands'] * 1 + ['foot hills'] * 2 + ['plateau'] * 2 + ['mountain'] * 2
        return random.choice(weighted_random_primary_topology)
    else:
        return "ERROR40020"
primary_topology = get_primary_topology()

def get_industry_raw(pt = primary_topology, lir = list_industry_raw, sp = settlement_population, sw = settlement_wealth):
    if pt == 'coastal':
        weighted_random_industry_raw = ['mining'] * 1 + ['farming'] * 1 + ['ranching'] * 1 + ['forestry'] * 1 + ['fishing'] * 999 + ['foraging'] * 1
        return random.choice(weighted_random_industry_raw)
    elif pt =='river':
        weighted_random_industry_raw = ['mining'] * 1 + ['farming'] * 4 + ['ranching'] * 4 + ['forestry'] * 1 + ['fishing'] * 4 + ['foraging'] * 1
        return random.choice(weighted_random_industry_raw)
    elif pt =='flat lands':
        weighted_random_industry_raw = ['mining'] * 1 + ['farming'] * 6 + ['ranching'] * 6 + ['forestry'] * 1 + ['fishing'] * 1 + ['foraging'] * 1
        return random.choice(weighted_random_industry_raw)
    elif pt =='foot hills':
        weighted_random_industry_raw = ['mining'] * 1 + ['farming'] * 2 + ['ranching'] * 6 + ['forestry'] * 1 + ['fishing'] * 1 + ['foraging'] * 1
        return random.choice(weighted_random_industry_raw)
    elif pt =='plateau':
        weighted_random_industry_raw = ['mining'] * 2 + ['farming'] * 1 + ['ranching'] * 1 + ['forestry'] * 4 + ['fishing'] * 2 + ['foraging'] * 1
        return random.choice(weighted_random_industry_raw)
    elif pt =='mountain':
        weighted_random_industry_raw = ['mining'] * 6 + ['farming'] * 1 + ['ranching'] * 1 + ['forestry'] * 6 + ['fishing'] * 2 + ['foraging'] * 2
        return random.choice(weighted_random_industry_raw)
    else:
        return "ERROR40030"
industry_raw = get_industry_raw()

def get_industry_crafts(lir = industry_raw, lic = list_industry_crafts, sp = settlement_population, sw = settlement_wealth):
    return random.choice(lic)
industry_crafts = get_industry_crafts()

def get_industry_services(lis = list_industry_services,lir = industry_raw, lic = industry_crafts, sp = settlement_population, sw = settlement_wealth):
    return random.choice(lis)
industry_services = get_industry_services()

print("settlement_name - " + settlement_name)
print("settlement_population - " + str(settlement_population))
print("settlement_density - " + str(settlement_density))
print("settlement_wealth - " + str(settlement_wealth))
print("settlement_age - " + str(settlement_age))
print("settlement_structures - " + str(settlement_structures))
print("primary_biome - " + primary_biome)
print("primary_topology - " + primary_topology)
print("industry_raw - " + industry_raw)
print("industry_crafts - " + industry_crafts)
print("industry_services - " + industry_services)

print("\n" + settlement_name + " is a " + primary_topology + " settlement located in the greater " + primary_biome + " area."
      "  The primary industry in the area is " + industry_raw + "." + "industry supports the local " + industry_crafts + ".  With a population of "
      + str(settlement_population) + " there are about " + str(settlement_structures) + " structures in town.")
