import requests
import string
from bs4 import BeautifulSoup

upper_cases = string.ascii_uppercase
names = []


for i in upper_cases:
    print(i)
    data = requests.get(f"https://www.hp-lexicon.org/character/?letter={i}")
    content = data.content
    soup = BeautifulSoup(content, 'html.parser')
    for i in soup.select('span[itemprop="headline"]'):
        word = i.get_text().lower()
        if word.startswith("mr."):
            word = word[3:]
        elif word.startswith("mrs."):
            word = word[4:]
        elif word.startswith("ms."):
            word = word[3:]
        elif word.startswith("miss"):
            word = word[4:]
        word = word.strip()
        word = word.replace(" ", "")
        if len(word) < 15:
            names.append(word)

print(names)
print()
for i in names:
    print(i)
    # print(pp)



