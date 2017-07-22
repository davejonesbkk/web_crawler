
#Get website url
#Crawler function
	#inits the crawl
	#makes a thread for each page being crawled
	#tracks pages that have been crawled already
#Threading function
	#create queues
#Crawled data function
	#stores & handles all data from crawled pages

from bs4 import BeautifulSoup
import requests, argparse, pprint

all_links = []
ok_links = []
problem_links = []


def check_response():

	print 'Checking URL responses'

	for al in all_links:

		li = requests.get(al)
		if li.status_code == 200:
			ok_links.append(al)
		else:
			problem_links.append(al)




def get_data():
	parser = argparse.ArgumentParser()
	parser.add_argument('website_url', help='Enter the full url of your website')
	args = parser.parse_args()

	user_url = args.website_url

	crawler(user_url)


def crawler(user_url):

	r = requests.get(user_url)
	print 'Fetching ', user_url, '. Returns: ', r.status_code

	soup = BeautifulSoup(r.text, 'html.parser')

	for l in soup.find_all('a'):
		all_links.append(l.get('href'))

	for al in all_links:
		if al[0:3] != 'http':
			all_links.remove(al)

	pp = pprint.PrettyPrinter()
	pp.pprint(all_links)

	funcs = check_response()

	try:

		funcs()
			
	except Exception:
		print 'Error, stopping'

	print problem_links


if __name__ == '__main__':
	get_data()


