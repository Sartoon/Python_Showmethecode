#Python3下，目前没有官方提供的PIL，调用PIL采用以下方式
from PIL import Image,ImageDraw, ImageFont, ImageFilter
#设置文本
text="7"
#打开图片
im =Image.open('icon.png')
#打开画笔
dr=ImageDraw.Draw(im)
print(type(dr))
#设置字体
font=ImageFont.truetype('slicker.ttf',34)

dr.text((im.size[0]*0.85,im.size[1]*0.05),text,font=font,fill="#ff0000")

im.show()
im.save('result.jpg')
