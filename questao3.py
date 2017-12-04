import requests
from bs4 import BeautifulSoup

def download(url, num_retries=2):
	# print('Downloading:', url)
	page = None
	try:
		response = requests.get(url)
		page = response.text
	except requests.exceptions.RequestException as e:
		print('Download error:', e.reason)
	return page
	# testing...

url = 'http://www.pi.gov.br'
html = download(url)
soup = BeautifulSoup(html, 'html.parser')
div_noticias = soup.find(attrs={'class':'thumbnails_container'})
noticias = div_noticias.find_all(attrs={'class':'post_text'})

print(len(noticias))
print("//////////////////////////////////////")
for noticia in noticias:
	titulo = noticia.find('h4')
	a = noticia.find('a')
	print(titulo.text)
	link = url+a.get('href')
	print(link)
	html_materia = download(link)
	soup_materia = BeautifulSoup(html_materia, 'html.parser')
	tags = soup_materia.find_all(attrs={'class':'btn-tags'})

	for tag in tags:
		print(tag.text)

