# To create QR Code
import pyqrcode
import png

str1 = "Athira"
url = pyqrcode.create(str1) # To create QR Code
url.svg("testqrcode.svg",scale=8) # To get QR Code as svg format

url.png("testqrcode.png",scale=8) # To get QR Code as png format