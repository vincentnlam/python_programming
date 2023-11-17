import qrcode
img = qrcode.make('https://vincentnlam.github.io/')
type(img)  # qrcode.image.pil.PilImage
img.save("vincent.png")

img = qrcode.make('https://www.eurovian.com/')
type(img)  # qrcode.image.pil.PilImage
img.save("eurovian.png")

