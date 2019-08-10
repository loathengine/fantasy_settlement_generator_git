import csv

def write_xml(file):
    with open('./data/primary_biome.txt') as pb:
        primary_biome = pb.read().splitlines()

    with open('./data/primary_topography.txt') as pt:
        primary_topography = pt.read().splitlines()

    with open('./data/industry_raw.txt') as ir:
        industry_raw = ir.read().splitlines()

    with open('./data/industry_crafts.txt') as ic:
        industry_crafts = ic.read().splitlines()

    with open('./data/industry_services.txt') as inds:
        industry_services = inds.read().splitlines()

    with open('./data/size_label.txt') as sl:
        size_label = sl.read().splitlines()


    print('<?xml version="1.0" encoding="UTF-8"?>', file=file)
    print('<UNIVERSE>', file=file)

    print('  <STATS>', file=file)
    for s_l in size_label:
        print('    <LABEL name="' + s_l + '" ceiling="3" >', file=file)
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


with open("data/monolith.xml", "w") as m:
    write_xml(m)
