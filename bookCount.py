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





















def display_li_links_resault(final_nested_li_links):

	def return_top_level_item(dedicated_level_of_links): # links that are in same level of being nested
		if not isinstance(dedicated_level_of_links, list):
			a_link = dedicated_level_of_links
			print(a_link)
			return a_link

		list(map(return_top_level_item, dedicated_level_of_links))

	flatted_list = []
	flatted_list = list(map(return_top_level_item, final_nested_li_links))
	
	
	
if __name__ == '__main__':

	# base variables
	target_website = 'https://www.paytakhteketab.com/'
	final_li_links = []

	# initial instance_vars
	navScraper = navigationListCrawler()
	
	# execute
	# final_li_links = navScraper.extract_li_links(target_website) # returns some structure like:
	
	final_li_links = [ 	# imagine each level of list as li tag and each number as category_link  		
		[ 		
			[	
				'<3>', 
				'<3>'
			], 
			[
				'<3>',
				'<3>'
			], 
			[
				'<3>', 
				'<3>'
			], 

			'<2>',
			'<2>'
		],

		[
			[
				'<3>', 
				'<3>'
			],
			[
				'<3>',
				'<3>'
			]
		],

		[ 
			'<2>',
			'<2>',
			'<2>' 
		],  

		'<1>', 
		'<1>',  
		'<1>', 
		'<1>'  
	]
	
	display_li_links_resault(final_li_links)
	
