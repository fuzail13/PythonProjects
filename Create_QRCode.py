import qrcode
from PIL import Image


qr = qrcode.QRCode(version=1,
                   box_size=10,border=4,)
qr.add_data("https://fuzail13.github.io/portfolio/")
qr.make(fit=True)
img = qr.make_image(fill_color="black",back_color="lightgreen")
img.save("FuzailKhan.png")