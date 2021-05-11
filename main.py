from bs4 import BeautifulSoup
import requests
links = ["https://www.colterm.ro/8-intreruperi","https://www.colterm.ro/8-intreruperi?start=36"]
URL="https://www.colterm.ro/8-intreruperi"
pagina=requests.get(URL)
pagina_text=pagina.text
soup=BeautifulSoup(pagina_text,"html.parser")
print(soup)
name = []
for a in soup.findAll('h2'):
    print(a)
    name.append(a.find('a'))
print(name)
for i in range(4,40,4):
    URL="https://www.colterm.ro/8-intreruperi?start=" +str(i)
    pagina=requests.get(URL)
    pagina_text=pagina.text
    soup=BeautifulSoup(pagina_text,"html.parser")
    print(soup)
    for a in soup.findAll('h2'):
        print(a)
        name.append(a.find('a'))
print(name)




