import os

file_name = 'index_template.html'

fp = file('index_template.html')
lines = []
for line in fp:
    lines.append(line)
fp.close()

LINE = -1
for i,line in enumerate(lines):
    if '<body>' in line: 
        LINE = i+1
        break

prefix0 = '      <div class="link-class"><a href="./articles/html/'
prefix1 = '">'
prefix2 = '</a></div>\n'

files_name = os.listdir('articles/html')
files_html = []
for f_name in files_name:
    if os.path.splitext(f_name)[1]=='.html':
        files_html.append(f_name)
for f_html in files_html:
    lines.insert(LINE, prefix0+f_html+prefix1+f_html[:-5]+prefix2)

s = ''.join(lines)
fp = file('index.html', 'w')
fp.write(s)
fp.close()
