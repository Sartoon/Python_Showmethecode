"""
Python 3.3
0008:一个HTML文件，找出里面的正文。
"""

import urllib.request

from bs4 import BeautifulSoup


def show_content(url, content_tag, content_tag_class):
    content = urllib.request.urlopen(url)
    """print(content)"""
    soup = BeautifulSoup(content,"html.parser")
    for tag in  soup.find_all(content_tag, content_tag_class):
        print (tag.text)


if __name__ == '__main__':
    show_content('http://v2ex.com/t/157721#reply10', 'div', 'topic_content')
