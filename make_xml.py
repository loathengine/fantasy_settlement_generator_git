with open('./data/primary_biome.txt') as b:
    biome = b.read().splitlines()

with open('./data/primary_topography.txt') as t:
    topo = t.read().splitlines()

with open('./data/industry_raw.txt') as r:
    raw = r.read().splitlines()

with open('./data/industry_crafts.txt') as cs:
    craft_shop = cs.read().splitlines()

with open('./data/industry_services.txt') as ss:
    service_shop = ss.read().splitlines()


print('<?xml version="1.0" encoding="UTF-8"?>')
print('<UNIVERSE>')
print('  <ENV>')
for b in biome:
    print('    <BIOME name="' + b + '" weight="3" >')
    for t in topo:
        print('      <TOPOGRAPHY name="' + t + '" weight="3" />')
    print('    </BIOME>')
print('  </ENV>')

print('  <IND>')
for t in topo:
    print('    <TOPOGRAPHY name="' + t + '" weight="3" >')
    for r in raw:
        print('      <RAW name="' + r + '" weight="3" >')
        for cs in craft_shop:
            print('        <SHOP name="' + cs + '" weight="3" />')
        for ss in service_shop:
            print('        <SHOP name="' + ss + '" weight="3" />')
        print('      </RAW>')
    print('    </TOPOGRAPHY>')
print('  </IND>')
print('</UNIVERSE>')



