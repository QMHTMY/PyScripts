#!/usr/bin/python3
# 转换图片为灰度图

from PIL import Image

# 模式L”为灰色图像，它的每个像素用8个bit表示，
# 0表示黑，255表示白，其他数字表示不同的灰度。
# Img.save("xxxx.png")

img = Image.open('xxxx.png')
Img = img.convert('L')

# 自定义灰度界限，大于这个值为黑色，小于这个值为白色
threshold = 190
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

# 图片二值化并保存
img = Img.point(table, '1')
img.save("xiaohuib.png")
