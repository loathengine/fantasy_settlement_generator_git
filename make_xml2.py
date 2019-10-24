import csv

def import_csv(file):

    with open(file) as csvfile:
        reader = csv.DictReader(csvfile,delimiter="|", restval=3)
        return (list(reader))


size_label = import_csv('data/size_label.txt')
primary_biome = import_csv('data/primary_biome.txt')
primary_topography = import_csv('data/primary_topography.txt')
industry_raw = import_csv('data/industry_raw.txt')
industry_shop = import_csv('data/industry_shop.txt')
industry_services = import_csv('data/industry_services.txt')
settlement_sign = import_csv('data/settlement_sign.txt')
settlement_government = import_csv('data/settlement_government.txt')
settlement_trait = import_csv('data/settlement_trait.txt')
race_percentage = import_csv('data/race_percentage.txt')
settle_age = import_csv('data/settlement_age.txt')
district_names = import_csv('data/district_names.txt')
district_trait = import_csv('data/district_trait.txt')
tavern_names = import_csv('data/tavern_names.txt')
tavern_description = import_csv('data/tavern_description.txt')
tavern_menu = import_csv('data/tavern_menu.txt')

def write_xml(file):
    print('<?xml version="1.0" encoding="UTF-8"?>', file=file)
    print('<UNIVERSE>', file=file)
    print('  <ENV name="DEFAULT" weight="3" desc="The default environment for your universe." >', file=file)
    for p_b in primary_biome:
        print('    <BIOME name="' + str(p_b['key']) + '" weight="' + str(p_b['weight']) + '" desc="' + str(p_b['desc']) + '" >', file=file)
        for p_t in primary_topography:
            print('      <TOPOGRAPHY name="' + str(p_t['key']) + '" weight="' + str(p_t['weight']) + '" desc="' + str(p_t['desc']) + '" >', file=file)
            for r_i in industry_raw:
                print('        <RAW name="' + str(r_i['key']) + '" weight="' + str(r_i['weight']) + '" desc="' + str(r_i['desc']) + '" >', file=file)
                for s_s in settlement_sign:
                    print('          <SIGN name="' + str(s_s['key']) + '" weight="' + str(s_s['weight']) + '" desc="' + str(s_s['desc']) + '" />', file=file)
                for i_s in industry_shop:
                    print('          <SHOP name="' + str(i_s['key']) + '" weight="' + str(i_s['weight']) + '" desc="' + str(i_s['desc']) + '" />', file=file)
                for d_n in district_names:
                    print('          <DISTRICT name="' + str(d_n['key']) + '" weight="' + str(d_n['weight']) + '" desc="' + str(d_n['desc']) + '" />', file=file)
                print('        </RAW>', file=file)
            print('      </TOPOGRAPHY>', file=file)
        print('    </BIOME>', file=file)
    print('  </ENV>', file=file)

    print('  <STATS>', file=file)
    for r_p in race_percentage:
        print('    <RACE name="' + str(r_p['key']) + '" weight="' + str(r_p['weight']) + '" desc="' + str(r_p['desc']) + '" />', file=file)
    for s_a in settle_age:
        print('    <AGE name="' + str(s_a['key']) + '" weight="' + str(s_a['weight']) + '" desc="' + str(s_a['desc']) + '" />', file=file)
    for s_g in settlement_government:
        print('    <GOVERNMENT name="' + str(s_g['key']) + '" weight="' + str(s_g['weight']) + '" desc="' + str(s_g['desc']) + '" />', file=file)
    for s_t in settlement_trait:
        print('    <TRAIT name="' + str(s_t['key']) + '" weight="' + str(s_t['weight']) + '" desc="' + str(s_t['desc']) + '" />', file=file)
    for d_t in district_trait:
        print('    <DISTRICT_TRAIT name="' + str(d_t['key']) + '" weight="' + str(d_t['weight']) + '" desc="' + str(d_t['desc']) + '" />', file=file)
    for t_m in tavern_menu:
        print('    <TAVERN_MENU name="' + str(t_m['key']) + '" weight="' + str(t_m['weight']) + '" desc="' + str(t_m['desc']) + '" />', file=file)
    for t_d in tavern_description:
        print('    <TAVERN_DESC name="' + str(t_d['key']) + '" weight="' + str(t_d['weight']) + '" desc="' + str(t_d['desc']) + '" />', file=file)
    for t_n in tavern_names:
        print('    <TAVERN_NAME name="' + str(t_n['key']) + '" weight="' + str(t_n['weight']) + '" desc="' + str(t_n['desc']) + '" />', file=file)
    for s_l in size_label:
        print('    <LABEL name="' + str(s_l['key']) + '" ceiling="' + str(s_l['weight']) + '" desc="' + str(s_l['desc']) + '" />', file=file)
    print('  </STATS>', file=file)

    print('  <IND>', file=file)
    print('  </IND>', file=file)

    print('</UNIVERSE>', file=file)

with open("data/monolith.xml", "w") as m:
    write_xml(m)
