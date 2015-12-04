from PIL import Image

def Change_resolution(filepath,resolution):
    image=Image.open(filepath)
    x,y=image.size
    
    changex=float(x)/resolution[0]
    changey=float(y)/resolution[1]

    if changex>1 or changey>1:
        change=changex  if changex > changey else changey
        image.resize((int(x/change),int(y/change))).save('resolution.jpg')    

if __name__=='__main__':
    Change_resolution('1.JPG',(1136, 640))
