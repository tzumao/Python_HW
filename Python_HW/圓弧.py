import cv2
import numpy as np

# 讀取圖片
img = cv2.imread('Turkey.jpg')

# 定義月亮外圓的參數
outer_center = (300, 200)  # 圓心位置
outer_axes = (120, 120)    # 橢圓的長軸與短軸
outer_angle = 0            # 旋轉角度

# 定義月亮內圓的參數
inner_center = (340, 200)  # 圓心位置
inner_axes = (80, 80)      # 橢圓的長軸與短軸
inner_angle = 0            # 旋轉角度

# 在圖片上畫月亮外圓
cv2.ellipse(img, outer_center, outer_axes, outer_angle, 0, 360, (0, 255, 255), 3)

# 在圖片上畫月亮內圓
cv2.ellipse(img, inner_center, inner_axes, inner_angle, 0, 360, (0, 255, 255), 3)

# 顯示結果
cv2.imwrite('moon_outlined.jpg', img)  # 儲存結果

