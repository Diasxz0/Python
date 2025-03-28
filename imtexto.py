from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (250,250), "White")
desenhe = ImageDraw.Draw(img)

try:
    fonte = ImageFont.truetype('arial.ttf', 24)
except: 
    fonte = ImageFont.load_default()

desenhe.text((50,50), "Ola, Mundo", fill='black', font=fonte)
img.show()