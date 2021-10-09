
fontid = '41'
input_dir = './font_' + fontid + '_raw'
out_dir= fontid + '_/' 
#out_dir= 'gt_animation/'
for data_split in {'syn', 'gt'}:

    for idx in range(0,52):
        svg_f = open(input_dir + "%02d"%(idx) + '.svg')
        svg_c = svg_f.read()
        #print(svg_c)
        if 'fill="currentColor"/>' in svg_c:
            #print('here')
            svg_c = svg_c.replace('fill="currentColor"/>','fill="none" stroke="black" stroke-width="0.3"></path>')
        d = svg_c.split('path d=')[1]
        d = 'd=' + d
        d = d.split('</path>')[0]
        #print(d)
        #input()
        #input()
        fout = open(out_dir + fontid + '_%02d'%(idx) + '.svg', 'w')
        #fout.write()
        
        fout.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="50px" height="50px" viewBox="0 0 24 24">' + '\n')
        fout.write('<style type="text/css">' + '\n')
        fout.write('.path {' + '\n')
        fout.write('\t\t' + 'stroke-dasharray: 100;' + '\n')
        fout.write('\t\t' + 'animation: dash 30s linear infinite;' + '\n')
        fout.write('}' + '\n')

        fout.write('@keyframes dash {' + '\n')
        fout.write('\t' + 'to {' + '\n')
        fout.write('\t\t' + 'stroke-dashoffset: 1000;' + '\n')
        fout.write('\t' + '}' + '\n')
        fout.write('}' + '\n')
        fout.write('</style>' + '\n')
        fout.write('<path class="path" ')
        fout.write(d + '\n')
        fout.write('</path>' + '\n')
        fout.write('</svg>' + '\n')
        
        fout.close()
