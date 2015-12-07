from bs4 import BeautifulSoup

def find_the_link(filepath):
    links = []
    with open(filepath,'rb') as f:
        text = f.read()
        bs =BeautifulSoup(text,"html.parser")
        for i in bs.find_all('a'):
            links.append(i['href'])
    return links

if __name__ == '__main__':
    link =find_the_link('V2EX.html')
    link=set(link)
    for i in link:
        print(i)

