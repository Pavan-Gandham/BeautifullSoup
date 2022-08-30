from bs4 import BeautifulSoup
import requests
import pandas as pa
url = requests.get('https://www.ncbi.nlm.nih.gov/protein/?term=keratin')
soup = BeautifulSoup(url.text,'html5lib')
names = []
numberOfProtiens = []
number = []

beautiful = soup.find_all(class_='rslt')
for name in beautiful:
    names.append(name.a.get_text())


gang = soup.find_all(class_='supp')
for num in gang:
    numberOfProtiens.append(num.p.get_text())


accisionNumber = soup.find_all(class_='resc')
for acc in accisionNumber:
   number.append(acc.find('dd').get_text())


data = {'Name':names,'Number of Protiens':numberOfProtiens,'Accision Number':number}
d = pa.DataFrame(data)
print(d)

 