
import random

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

random.seed( 12345 )

settlement_name = "Testberg"
settlement_population = random.randint(5, 5000)
settlement_density = random.randint(1, 6)
settlement_wealth = random.randint(1, 6)
settlement_age = random.randint(1,6)
settlement_structures = ((settlement_population << 1) // (settlement_density)) >> 1

def primary_biome(lpb = list_primary_biome):
    return random.choice(lpb)

def primary_topology(lpt = list_primary_topology):
    return random.choice(lpt)

def industry_raw(lir = list_industry_raw, sp = settlement_population, sw = settlement_wealth):
    return random.choice(lir)

def industry_crafts(lir = list_industry_raw, lic = list_industry_crafts, sp = settlement_population, sw = settlement_wealth):
    return random.choice(lic)

def industry_services(lis = list_industry_services,lir = list_industry_raw, lic = list_industry_crafts, sp = settlement_population, sw = settlement_wealth):
    return random.choice(lis)

print("settlement_name - " + settlement_name)
print("settlement_population - " + str(settlement_population))
print("settlement_density - " + str(settlement_density))
print("settlement_wealth - " + str(settlement_wealth))
print("settlement_age - " + str(settlement_age))
print("settlement_structures - " + str(settlement_structures))
print("industry_raw - " + industry_raw())
print("industry_crafts - " + industry_crafts())
print("industry_crafts - " + industry_services())

print("\n" + settlement_name + " is a " + primary_topology() + " settlement located in the greater " + primary_biome() + " area."
      "  The " + industry_raw() + " industry supports the local " + industry_crafts() + ".  With a population of "
      + str(settlement_population) + " there are about " + str(settlement_structures) + " structures in town.")
