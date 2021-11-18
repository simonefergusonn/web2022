import qrcode
from random import randint
import pyqrcode 


color = (randint(0,255), randint(0,255), randint(0,255))

img = qrcode.make("https://www.instagram.com/p/CVysi3clWoh/")

qr = qrcode.QRCode( 
     version= 5,
     box_size = 10,
     border = 3
 )

qr.add_data('https://www.instagram.com/p/CVysi3clWoh/')
qr.make(fit=True)

img = qr.make_image(fill_color = (color), back_color = "white")
img.save("instagram.png")

url = pyqrcode.create('https://www.instagram.com/p/CVysi3clWoh/')
print(url)


