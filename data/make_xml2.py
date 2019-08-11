import csv

def import_csv(file):

    with open(file) as csvfile:
        reader = csv.DictReader(csvfile,delimiter=",")
        return (list(reader))


size_label = import_csv('size_label.txt')
primary_biome = import_csv('primary_biome.txt')
primary_topography = import_csv('primary_topography.txt')
industry_raw = import_csv('industry_raw.txt')
industry_crafts = import_csv('industry_crafts.txt')
industry_services = import_csv('industry_services.txt')
settlement_government = import_csv('settlement_government.txt')
settlement_trait = import_csv('settlement_trait.txt')


print('<?xml version="1.0" encoding="UTF-8"?>')
print('<UNIVERSE>')
print('  <STATS>')
for s_l in size_label:
   print('    <LABEL name="' + str(s_l['key']) + '" ceiling="' + str(s_l['weight']) + '" />')

def write_xml
    print('<?xml version="1.0" encoding="UTF-8"?>', file=file)
    print('<UNIVERSE>', file=file)
    print('  <STATS>', file=file)
    for s_l in size_label:
        print('    <LABEL name="' + str(s_l['key']) + '" ceiling="' + str(s_l['weight']) + '" />', file=file)
    for s_g in settlement_government:
        print('    <GOVERNMENT name="' + s_g + '" weight="3" />', file=file)
    for s_t in settlement_trait:
        print('    <TRAIT name="' + s_t + '" weight="3" />', file=file)
    print('  </STATS>', file=file)
    print('  <ENV>', file=file)
    for p_b in primary_biome:
        print('    <BIOME name="' + p_b + '" weight="3" >', file=file)
        for p_t in primary_topography:
            print('    <TOPOGRAPHY name="' + p_t + '" weight="3" >', file=file)
            for r_i in industry_raw:
                print('      <RAW name="' + r_i + '" weight="3" >', file=file)
                for i_c in industry_crafts:
                    print('        <SHOP name="' + i_c + '" weight="3" />', file=file)
                for i_s in industry_services:
                    print('        <SHOP name="' + i_s + '" weight="3" />', file=file)
                print('      </RAW>', file=file)
            print('    </TOPOGRAPHY>', file=file)
        print('    </BIOME>', file=file)
    print('  </ENV>', file=file)
    print('  <IND>', file=file)
    print('  </IND>', file=file)
    print('</UNIVERSE>', file=file)


with open("monolith.xml", "w") as m:
    write_xml(m)