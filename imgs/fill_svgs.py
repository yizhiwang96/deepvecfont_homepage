dirs = ['font_35_raw', 'font_57_raw', 'font_35_57_3_raw', 'font_35_57_5_raw', 'font_35_57_7_raw']
for dir_name in dirs:
    for char_id in range(52):
        svg = open(dir_name + '/syn/' + "%02d"%char_id + '.svg', 'r').read()
        svg = svg.replace('fill="none" stroke="black" stroke-width="0.3"', 'stroke-width="1.0" fill="rgb(0, 0, 0)" opacity="1.0"')
        fout =  open(dir_name + '/syn/' + "%02d"%char_id + '.svg', 'w')
        fout.write(svg)

