import codecs
import webbrowser
import requests
from bs4 import BeautifulSoup

URL = "https://github.com/Hqko01/Python"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

nameSoup = soup.find("div", class_="Box md js-code-block-container js-code-nav-container js-tagsearch-file Box--responsive").findAll("a")


temp = []
for i in range(2, len(nameSoup)):
  temp.append(nameSoup[i].attrs['href'])


a = 'hakan'
f = open('PyForWeb.html', 'w')

html_template = """ <div>""", temp ,""" </div>"""

f.write(html_template)

f.close()

file = codecs.open('PyForWeb.html', 'r', "utf-8")

print(file.read())