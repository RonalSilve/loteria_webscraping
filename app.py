from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from urllib.request import Request, urlopen

loterias_name = ["loto pool", "pega mas", "quiniela pale",
            "loteria real", "loteria nacional",
            "loteria nacional ganamas"]
url="https://leidsa.com/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')
page_soup = soup(webpage,"html.parser")
loto = page_soup.find(attrs = {'class':'table-sin-borde text-center'})

numeros = loto.findAll(attrs = {'class':'numeros-ganadores'})
print("Los numeros ganadores del loto leysa son:\n")
for i in range (6):
    print (numeros[i].text, end=" ")
  
print("\n\nLos numeros ganadores del kino leysa son:")
for j in range(4):
    kino = page_soup.findAll(attrs = {'class':'table-sin-borde text-center super-kino-tv'})
    numeros = kino[j].findAll(attrs = {'class':'numeros-ganadores-loterias'})
    print ("")
    for i in range (6):
        if j == 3 and i>1:
            pass
        else:
            print (numeros[i].text, end=" ")
            
for j in range(1,7):
    loteria = page_soup.findAll(attrs = {'class':'panel-body numeros-sorteos'})
    numeros = loteria[j].findAll(attrs = {'class':'numeros-ganadores-loterias'})
    print ("\n")
    print (loterias_name[j-1])
    for i in range (3):
        if j == 1:
            for n in range (5):
                print (numeros[n].text, end=" ")
            break
        else:
            print (numeros[i].text, end=" ")
input()
