from bs4 import BeautifulSoup
import lxml
with open('C:\\Users\\MR.G\\Desktop\\1.html','r') as wb_data:
	Soup = BeautifulSoup(wb_data,'lxml')
	title = Soup.select('mynav10 > span')
	foot = Soup.select('footer > dl > dd')
	print(foot)

#ctl00_welcome
#mynav10 > span
	
#footer > dl > dd
