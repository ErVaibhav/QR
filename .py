import qrcode
from PIL import Image
In = input("Input content for QR code ")
Name = input("Choose QR code File Name")
image = qrcode.make(In)
type(image)
image.save(f"{Name}.png")
print(f"Name = {Name}.png")
image = Image.open(f'{Name}.png')
image.show()
