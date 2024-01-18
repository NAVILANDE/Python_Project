# import qrcode as qr

# img=qr.make("https://www.linkedin.com/in/vaishnavi-lande-0349aa250")
# img.save("vaishnavi_lande_Linkdin.png")


# advance QR genration

import qrcode
from PIL import Image
from qrcode import constants


qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("https://www.linkedin.com/in/vaishnavi-lande-0349aa250")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="yellow")
img.save("my_linkdinQR.png")