# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import VerticalBarsDrawer,RoundedModuleDrawer,HorizontalBarsDrawer,SquareModuleDrawer,GappedSquareModuleDrawer,CircleModuleDrawer

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data('https://steam.oxxostudio.tw')
qr.make(fit=True)

img1 = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer())
img2 = qr.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer())
img3 = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer())
img4 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img5 = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer())
img6 = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer())
img1.save('qrcode1.png')
img2.save('qrcode2.png')
img3.save('qrcode3.png')
img4.save('qrcode4.png')
img5.save('qrcode5.png')
img6.save('qrcode6.png')

