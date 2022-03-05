import bs4
import requests

url = "https://zlib.net/"
resp = requests.get(url)


page = resp.content
soup = bs4.BeautifulSoup(page, 'html.parser')

print(soup.tr.next.next)
print(soup.find('tr'))