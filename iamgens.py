from PIL import Image, ImageDraw

img = Image.new("RGB", (300,300), "yellow")
desenho = ImageDraw.Draw(img)
desenho.line((50,50,250,250), fill= 'blue', width= 5)
retangulo = ImageDraw.Draw(img)
retangulo.rectangle((100,60,200,150), outline='red', width=6)
circulo = ImageDraw.Draw(img)
circulo.ellipse((20,20,50,50), fill='black', outline='green', width=3)
img.show()