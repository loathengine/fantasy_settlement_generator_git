with open('./data/primary_biome.txt') as b:
    biome = b.read().splitlines()

with open('./data/primary_topography.txt') as t:
    topo = t.read().splitlines()

with open('./data/industry_raw.txt') as r:
    raw = r.read().splitlines()

with open('./data/industry_crafts.txt') as s:
    shop = s.read().splitlines()


print('<?xml version="1.0" encoding="UTF-8"?>')
print('<ENV>')
for b in biome:
    print('    <BIOME name="' + b + '" weight="3" >')
    for t in topo:
        print('        <TOPOGRAPHY name="' + t + '" weight="3" >')
        for r in raw:
            print('            <RAW name="' + r + '" weight="3" />')
        print('        </TOPOGRAPHY>')
    print('    </BIOME>')
print('</ENV>')
