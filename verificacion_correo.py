import imaplib
import re
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('@gmail.com', '')

mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.

result, data = mail.search(None, "ALL")

ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest

result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
# print(type(data))
# for i in data:
#   print(i)
raw_email = data[0][1] # here's the body, which is raw text of the whole email
# including headers and alternate payloads
# print(raw_email)
from bs4 import BeautifulSoup
soup = BeautifulSoup(raw_email, "html.parser")

for i in soup.find_all("body"):
  print(i.text)
for i in soup.find_all("subject"):
  print(i.text)
# links = soup.findAll('a')
# print(links)
# print("***************\nLINKS")
# urls = []
# for link in links:  
#   urls.append(link.get('href'))
# print(urls)
# print(urls[1])















