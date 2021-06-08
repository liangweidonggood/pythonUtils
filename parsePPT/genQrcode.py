import qrcode

qr = qrcode.QRCode(
    version=3,  # 二维码大小，用1~40之间的整数来设置。最小的version=1，是一个21x21的矩阵。
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 二维码的纠错范围
    box_size=20,  # 每一个点中的像素个数
    border=1,  # 二维码距图像外围边框距离，默认为4
)
qr.add_data("http://sunsgallery.cn/#/detail?id=330")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")  # QR的背景和绘画颜色
# 生成二维码
# img = qrcode.make(data="http://sunsgallery.cn/#/detail?id=330")
# 将二维码保存为图片
with open("test1.png", "wb") as f:
    img.save(f)
