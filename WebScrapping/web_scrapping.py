import requests
from bs4 import BeautifulSoup

#Get the HTML
html_res = requests.get("https://mhworld.kiranico.com/") #HTML is stored in res.content

#Parse the HTML:           V got HTML     V method of parsing
soup = BeautifulSoup(html_res.content, "html.parser")


#Finding stuff:
#                            V tag        V Dict with indentity argument
mon_list_table = soup.findAll("table", {"class": "table table-sm"})
mon_list_rows = soup.findAll("tr")
mon_list = []
for row in mon_list_rows:
    if 'Zorah Magdaros' in mon_list:
            break
    for img in row.findAll("img", alt=True):
        mon_list.append(img["alt"])
        image = img["src"]
        with open(f"SDET Training Course/WebScrapping/Icons/{img['alt']}.png","wb+") as f:
            f.write(requests.get(image).content)
            f.close()

print(mon_list)