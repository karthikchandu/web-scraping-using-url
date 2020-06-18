from bs4 import BeautifulSoup
import requests

url = input("Enter a while to extract the line from: ")

r = requests.get(url)

data = r.text

soup = BeautifulSoup(data,"html.parser")

list =''

for link in soup.find_all('a'):
	list +=link.get('href')+ '\n' 

print(list)
