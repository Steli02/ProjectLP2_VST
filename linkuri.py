from bs4 import BeautifulSoup
import requests
import re

URL="https://www.colterm.ro/8-intreruperi"
link_intreg= ["https://www.colterm.ro/"]
pagina=requests.get(URL)
pagina_text=pagina.text
soup=BeautifulSoup(pagina_text,"html.parser")
info = []
hours = []
streets = []

for a in soup.findAll("div", class_="leading-0"):
    info.append(a.find('p'))
for a in soup.findAll("div", class_="span4"):
    info.append(a.find('p'))
for b in info:
    m = re.search('\d+-\d+',str(b))
    hours.append(m.group(0))
for c in info:
    text = str(c)
    for i in range(len(text)):
        if text[i]==':':
            pozx = i
        if text[i]=='<' and text[i+1] == 'b' and text[i+2] == 'r':
            pozy = i
            break
    streets.append(text[pozx+2:pozy-1])


for i in range(4,40,4):
    URL="https://www.colterm.ro/8-intreruperi?start=" + str(i)
    pagina = requests.get(URL)
    pagina_text = pagina.text
    soup = BeautifulSoup(pagina_text, "html.parser")

    for a in soup.findAll("div", class_="leading-0"):
        info.append(a.find('p'))
    for a in soup.findAll("div", class_="span4"):
        info.append(a.find('p'))
    for b in info:
        m = re.search('\d+-\d+', str(b))
        if m != None:
            hours.append(m.group(0))
    for c in info:
        text = str(c)
        for i in range(len(text)):
            if text[i] == ':':
                pozx = i
            if text[i] == '<' and text[i + 1] == 'b' and text[i + 2] == 'r':
                pozy = i
                break
        streets.append(text[pozx + 2:pozy - 1])

print(hours)
print(streets)


