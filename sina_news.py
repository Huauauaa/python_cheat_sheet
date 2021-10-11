import requests
import csv


# https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
from bs4 import BeautifulSoup


url = 'https://news.sina.com.cn/'

response = requests.get(url)
response.encoding = 'UTF-8'

# print(response.text)

soup = BeautifulSoup(response.text, features='html.parser')

# print(soup.title.string)
# print(soup.title)
# print(soup.title.parent.name)
# print(soup.p)
print(soup.find_all('a')[0].get('href'))


def main():
    csv_fp = open("output.csv", "w", encoding='utf-8', newline='')
    writer = csv.writer(csv_fp)
    writer.writerows([{item.get('href')} for item in soup.find_all('a')])


if __name__ == '__main__':
    main()
