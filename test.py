'''
@Author: your name
@Date: 2020-05-29 00:45:19
@LastEditTime: 2020-05-29 01:01:52
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \-Insgram-\test.py
'''
import requests
from bs4 import BeautifulSoup

content = requests.get('http://www.qiushibaike.com').content
soup = BeautifulSoup(content, 'html.parser')

for div in soup.find_all('div', {'class': 'content'}):
    print(div.text.strip())


def demo_string():
    stra = 'hello world'
    print(stra.capitalize())


if __name__ == "__main__":
    print('hello world')
    demo_string()
