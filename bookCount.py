import requests
from bs4 import BeautifulSoup

class web(object):
	
	def __init__(self):
		pass

	def make_request(self, url):
		return requests.get(url)


class navigationListCrawler(web):
	
	def __init__(self):
		super().__init__()
		self.li_links = []

	def append_vlaue(self, value):
		self.li_links.append(value)

	def extract_li_links(self, base_ul_tag):
		inner_ul = base_ul_tag.find('ul', class_='mm-spn--open')
		i = 0
		for li in inner_ul.find_all('li', class_="has-submenu"):
			print(li)
			i += 1
			print("--------------------------------------------------------------------------------")
		print(i)


'''
structure

li links = 
[
	li-href = 
	[
		li_href = 
		[
			li_href,
			li_href,
		],

		li_href = 
		[
			li_href,
			li_href,
		],

		li_href,
		li_href
	],

	li-href = 
	[
		li_href,
		li_href,
		li_href,
	],

	li-href,
	li-href,
	li-href,
]
'''
	



if __name__ == '__main__':
	requ_maker = web()
	scraper = navigationListCrawler()

	target_website = 'https://www.paytakhteketab.com/'
	resp = requ_maker.make_request(target_website)

	soup = BeautifulSoup(resp.content, 'html.parser')
	menu_tag = soup.find('nav', {'id': 'menu'})

	scraper.extract_li_links(menu_tag)
	# token = 'hello'
	# no_longer_at_risk = soup.find('ul', class_="mm-spn--open").find_next('ul').find_all('li')
	# print(no_longer_at_risk)