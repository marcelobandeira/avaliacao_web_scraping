import requests
from bs4 import BeautifulSoup
import sys


def download(url, num_retries=2):
	page = None
	try:
		response = requests.get(url)
		page = response.text
	except requests.exceptions.RequestException as e:
		print('Download error:', e.reason)
	return page
	# testing...

def get_page(url):
	html = download(url)
	soup = BeautifulSoup(html, 'html.parser')
	trs = soup.find_all('tr')
	for i in range(2, len(trs)):
		td = trs[i].find_all('td')
		if td[5].text == sys.argv[1]:
			print(td[1].text)
			print(td[2].text)

get_page('http://www.portaldatransparencia.gov.br/cnep/?pagina=1')
get_page('http://www.portaldatransparencia.gov.br/cnep/?pagina=2')

