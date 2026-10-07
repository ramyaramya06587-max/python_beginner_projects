import qrcode
github_url = "https://github.com/ramyaramya06587-max"
qr=qrcode.make(github_url)
qr.save("github_qr.png")
print("QR code created successfully")