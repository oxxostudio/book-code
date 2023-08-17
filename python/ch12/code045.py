# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import ImageColorMask, SolidFillColorMask, RadialGradiantColorMask, SquareGradiantColorMask, VerticalGradiantColorMask, HorizontalGradiantColorMask

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data('https://steam.oxxostudio.tw')
qr.make(fit=True)

img1 = qr.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask((255,255,255),(255,0,0)), module_drawer=RoundedModuleDrawer())
img2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask((255,255,255),(255,0,0),(0,0,255)), module_drawer=RoundedModuleDrawer())
img3 = qr.make_image(image_factory=StyledPilImage, color_mask=SquareGradiantColorMask((255,255,255),(255,0,0),(0,0,255)), module_drawer=RoundedModuleDrawer())
img4 = qr.make_image(image_factory=StyledPilImage, color_mask=VerticalGradiantColorMask((255,255,255),(255,0,0),(0,0,255)), module_drawer=RoundedModuleDrawer())
img5 = qr.make_image(image_factory=StyledPilImage, color_mask=HorizontalGradiantColorMask((255,255,255),(255,0,0),(0,0,255)), module_drawer=RoundedModuleDrawer())
img6 = qr.make_image(image_factory=StyledPilImage, color_mask=ImageColorMask((255,255,255),'mona.jpg'), module_drawer=RoundedModuleDrawer())

img1.save('qrcode1.png')
img2.save('qrcode2.png')
img3.save('qrcode3.png')
img4.save('qrcode4.png')
img5.save('qrcode5.png')

