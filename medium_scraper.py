import re
import requests
import urllib
from bs4 import BeautifulSoup
#result = requests.get("/Users/dphamnyghonca/Downloads/medium.html")
#page = result.content
#soup = BeautifulSoup(page)

soup = BeautifulSoup(open("july.html"))


# get links


#get titles and content for each

#def is_post(href):
#	return href and re.compile("photo").search(href) and not re.compile("#").search(href)


def is_article(href):
	return href and re.compile("source=reading_list").search(href)

links = []

for link in soup.find_all('a',href=is_article,class_="link"):
	links.append(link.get('href'))

links = set(links)


title_file = open('medium_titles.txt', 'a')
content_file = open('medium_content.txt','a')


for link in links:
	if link.startswith("https://medium.com/"):
		print(link)
		result = requests.get(link)
		page = result.content
		soup = BeautifulSoup(page)
		title_file.write((soup.find('h3').getText()).encode('utf-8') + "\n")
		for paragraph in soup.find_all("p"):
			content_file.write((paragraph.getText()).encode('utf-8') + "\n")

title_file.close()
content_file.close()
























# link_array = []

# ids = []

# content = ""

# title_file = open('titles.txt', 'a')
# content_file = open('content.txt','a')

# title_file.write((soup.find('h1').getText()).encode('utf-8') + "\n")

# for paragraph in soup.find_all("p", class_="story-body-text story-content"):
# 	#content += urllib.decode(paragraph.getText()) + "\n"
# 	#content += paragraph.getText() + "\n"
# 	content_file.write((paragraph.getText()).encode('utf-8') + "\n")


# title_file.close()
# content_file.close()


