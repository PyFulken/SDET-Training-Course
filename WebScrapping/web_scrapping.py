import requests
import json
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
mon_urls = {}
for row in mon_list_rows:
    if 'Zorah Magdaros' in mon_list or 'zorah' in mon_urls:
            break

    for img in row.findAll("img", alt=True):
        mon_list.append(img["alt"])
        image = img["src"]
        with open(f"SDET Training Course/WebScrapping/Icons/{img['alt']}.png","wb+") as f:
            f.write(requests.get(image).content)
            f.close()


    for link in row.findAll("a", {"class": "d-block"}):
        if "monsters" in link["href"]:
            child_res = requests.get(link["href"])
            child_soup = BeautifulSoup(child_res.content, "html.parser")
            description = child_soup.find("div", {"class": "col-sm-6"})
            strip_description = description.text.strip("\n")
            strip_description = strip_description.strip()
            mon_urls[f'{link["href"]}'] = strip_description

with open(f"SDET Training Course/WebScrapping/monster_desc.json","w") as f:
            json.dump(mon_urls, f)
            f.close()
            

with open(f"SDET Training Course/WebScrapping/monster_links.txt","w") as f:
            f.write(mon_urls)
            f.close()

#   Elements can also be found by their string value that is shown:

known_string = soup.findAll("a", string="Provisions")
its_link = known_string["href"]