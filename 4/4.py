import re

def counter(string):
    words=re.findall(r'[a-zA-Z]+(\'[a-zA-Z]+|\b)',string)
    amount=len(words)
    return str(amount)

def file_read(filename):
    with open(filename,'r')as fp:
        article=fp.read()
        return article

if __name__=='__main__':
    string =file_read('lidgren.txt')
    result=counter(string)
    print('There are '+result+' words in this article.')
    
