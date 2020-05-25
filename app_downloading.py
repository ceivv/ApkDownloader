from selenium import webdriver 
from bs4 import BeautifulSoup
import requests
 
apk = input('give apk name : ')
url = 'https://m.apkpure.com/search?q='+apk
page = requests.get(url)
 
# Getting the webpage, creating a Response object.
response = requests.get(url)
 
# Extracting the source code of the page.
data = response.text
 
# Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'lxml')
 
#searching by class
tags = soup.find_all(class_="dd")
 
# Extracting URLs from the attribute href in the <a> tags.
mylist=[]
for tag in tags:
   mylist.append(str(tag.get('href')))
print(mylist)
newurl='https://apkpure.com'+mylist[0]
print(newurl)
#downloading
br=webdriver.Firefox()
br.get(newurl)
link=br.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/dl/dd/div[5]/a[1]')
link.click()

