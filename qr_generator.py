import qrcode
import qrcodeT
import os

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

os.system("cls||clear")

print("  .d88b.  888b.  .d88b          8            .d88b              ")
print(" 8P  Y8   8  .8  8P    .d8b.  .d88  .d88b    8P www  .d88b 8d8b. ")
print(" 8b wd8   8wwK'  8b    8' .8  8  8  8.dP'    8b  d8 8.dP' 8P Y8 ")
print(" `Y88Pw   8  Yb  `Y88P `Y8P'  `Y88  `Y88P    `Y88P' `Y88P 8   8 ")

print()

datatoadd = input("Introduce the data/page/etc you want to add the QR: " )

qr.add_data(datatoadd)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

qrcodeT.qrcodeT(datatoadd)

save = input("Do you want to save the QR? (y/n): ")
if save == "y":
    filename = input("Introduce the filename: ")
    route = input("Introduce the route where you want to save the QR: ")

    img.save(route+"/"+filename + ".png")
else:
    print("QR not saved")