#importing bs4 for get link the site 
from bs4 import BeautifulSoup 
import requests

#Create the object BeautifulSoup
url = 'https://qz.com/africa/latest/'
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

#getting tags html
#titlePage = soup.find('div', class_= '_4c830').text
#print(titlePage)

title = soup.find('div', class_= '_835db c8e6d').find('ul', class_ = 'be480').text
print(title)

#news = soup.find('span', class_= '_57b5c').text
#print(news)

#theme = soup.find('div', class_= 'cb22a _06e51').text
#print(theme)

link = soup.find("div").find('a', class_= '_733af', href=True)
print(link['href'])

#create elements
all_elements = soup.find_all('')

for elements in all_elements:
	#titlePage = elements.text
	title	  = elements.find('ul', class_ = '_3fac2.f40b3')
	#news	  = elements.text
	#theme    = elements.text
	link 	  = elements.find('a', class_= '_733af', href=True)

	#print(f'titlePage: {TitlePage}')
	print(f'title: {Title}')
	#print(f'news: {News}')
	#print(f'theme: {Theme}')
	print(f'link: {Link}')
	print('-'*40)


