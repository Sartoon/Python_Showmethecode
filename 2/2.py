import random
import pickle
def create_num(num,long):
    str="qwertyuiop[]asdfghjkl;'zxcvbnm,./1234567890-=\!@#$%^&*()_+|"
    b=[]
    for i in range(num):
        a=''
        for j in range(long):
            a+=random.choice(str)

        b.append(a)
   
        for i in range(len(b)):
            print(b[i])
        with open('Activation_code.txt','wb') as mysavedata:    
            pickle.dump(b,mysavedata)

def load_num():
    
    with open('Activation_code.txt','rb') as mysavedata:
           b=pickle.load(mysavedata)

    for i in range(len(b)):
         print(b[i])
        
if __name__=='__main__':
    create_num(100,10)
    load_num()
