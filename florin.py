from bs4 import BeautifulSoup
import requests
import re
import folium
import webbrowser
import geopy
from geopy.geocoders import Nominatim

# URL - preluare informatii
# pagina - trimite cerere de incarcare catre URL
# pagina_text - descarca informatia din pagina si o salveaza in variabile
# soup - incarca informatia din pagina intr-un mod parsabil
URL="https://www.colterm.ro/8-intreruperi?start="
pagina=requests.get(URL)
pagina_text=pagina.text
soup=BeautifulSoup(pagina_text,"html.parser")
info = []
hours = []
streets = []
data = []

for i in range(4,8,4):
    URL_REPEAT = URL + str(i)
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


# curatare caractere ilegale
counter = 0
for street in streets:
    strada = street.split(',')
    for element in strada:
        temp = element.replace("\xa0","")
        temp = temp + ", Timisoara"
        data.append(temp)
print(data)
print(hours)
m = folium.Map(location=[45.750969, 21.226200], zoom_start=13)

geolocator = Nominatim(user_agent="stelian.vad@gmail.com")

for i in range(len(data)):
    location = geolocator.geocode(data[i])

    if location == None:
        #nu a fost gasita locatia, tratare eroare
        pass
    else:
        x = location.latitude
        y = location.longitude
        folium.Marker(location=[x, y], popup=data[i], icon=folium.Icon(color='red', icon='remove-sign')).add_to(m)


m.save('index.html')

webbrowser.open('http://localhost:63342/exercitii/index.html')  # open in new tab