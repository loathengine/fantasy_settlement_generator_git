import csv

def import_csv(file):

    with open(file) as csvfile:
        reader = csv.DictReader(csvfile,delimiter=",", restval=3)
        return (list(reader))


size_label = import_csv('data/size_label.txt')
primary_biome = import_csv('data/primary_biome.txt')
primary_topography = import_csv('data/primary_topography.txt')
industry_raw = import_csv('data/industry_raw.txt')
industry_crafts = import_csv('data/industry_crafts.txt')
industry_services = import_csv('data/industry_services.txt')
settlement_government = import_csv('data/settlement_government.txt')
settlement_trait = import_csv('data/settlement_trait.txt')
race_percentage = import_csv('data/race_percentage.txt')

def write_xml(file):
    print('<?xml version="1.0" encoding="UTF-8"?>', file=file)
    print('<UNIVERSE>', file=file)
    print('  <STATS>', file=file)
    for r_p in race_percentage:
        print('    <RACE name="' + str(r_p['key']) + '" ceiling="' + str(r_p['weight']) + '" />', file=file)
    for s_l in size_label:
        print('    <LABEL name="' + str(s_l['key']) + '" ceiling="' + str(s_l['weight']) + '" />', file=file)
    for s_g in settlement_government:
        print('    <GOVERNMENT name="' + str(s_g['key']) + '" weight="3" />', file=file)
    for s_t in settlement_trait:
        print('    <TRAIT name="' + str(s_t['key']) + '" weight="3" />', file=file)
    print('  </STATS>', file=file)
    print('  <ENV>', file=file)
    for p_b in primary_biome:
        print('    <BIOME name="' + str(p_b['key']) + '" weight="3" >', file=file)
        for p_t in primary_topography:
            print('    <TOPOGRAPHY name="' + str(p_t['key']) + '" weight="3" >', file=file)
            for r_i in industry_raw:
                print('      <RAW name="' + str(r_i['key']) + '" weight="3" >', file=file)
                for i_c in industry_crafts:
                    print('        <SHOP name="' + str(i_c['key']) + '" weight="3" />', file=file)
                for i_s in industry_services:
                    print('        <SHOP name="' + str(i_s['key']) + '" weight="3" />', file=file)
                print('      </RAW>', file=file)
            print('    </TOPOGRAPHY>', file=file)
        print('    </BIOME>', file=file)
    print('  </ENV>', file=file)
    print('  <IND>', file=file)
    print('  </IND>', file=file)
    print('</UNIVERSE>', file=file)


with open("data/monolith.xml", "w") as m:
    write_xml(m)