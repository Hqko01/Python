import requests
from bs4 import BeautifulSoup

URL = "https://github.com/Hqko01"
viewURL = "https://camo.githubusercontent.com/886523aa432882579ea24bbcf8ba1cc86bb9873dfd371f08980b4ad3aa337fbe/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d68716b6f3031267374796c653d666f722d7468652d626164676526636f6c6f723d646331343363"

view = requests.get(viewURL)
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

nameSoup = soup.find("span", class_="p-nickname vcard-username d-block").get_text().strip()
viewSoup = BeautifulSoup(view.content, "html.parser").title.get_text()

print(nameSoup)
print(viewSoup)