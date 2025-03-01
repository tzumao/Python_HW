import cv2
import numpy as np
img = cv2.imread('cat.bmp')
img = cv2.resize(img,(0,0),fx=0.3,fy=0.3)
print(img.shape)
newImg=img.copy()
blocksize = 10
for i in range(0, img.shape[0], blocksize):  # 行的切片起點
    for j in range(0, img.shape[1], blocksize):  # 列的切片起點
        start_r = i
        end_r = min(i + blocksize, img.shape[0])  # 確保不超過影像邊界
        start_c = j
        end_c = min(j + blocksize, img.shape[1])  # 確保不超過影像邊界

        sub_block = img[start_r:end_r, start_c:end_c]  # 切片提取一個區塊
        mean_value = np.mean(sub_block, axis=(0, 1))  # 計算區塊的 RGB 平均值
        newImg[start_r:end_r, start_c:end_c] = mean_value.astype(np.uint8)  # 用平均值填充區塊
cv2.imshow('test',newImg)
print(newImg.shape)
cv2.waitKey(0)
