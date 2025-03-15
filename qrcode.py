import qrcode
img = qrcode.make("https://www.instagram.com/iam_meghana_m_raj/")
img.save("my_instagram.jpg")