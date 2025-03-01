import cv2
import numpy
cv2.namedWindow('a')
img=cv2.imread('Canada.jpg')
arr = numpy.array([
    [600,57],
    [552,138],
    [508,121],
    [525,255],
    [460,192],
    [450,228],
    [375,214],
    [396,293],
    [367,311],
    [483,411],
    [473,450],
    [592,434],
    [590,561],
    [609,561],
    [608,434],
    [726,450],
    [716,411],
    [834,311],
    [803,293],
    [823,214],
    [751,228],
    [738,192],
    [673,255],
    [691,121],
    [646,138]
], numpy.int32)
cv2.polylines(img,[arr],True,(255,0,0),3)
cv2.imshow('test',img)
cv2.imwrite('test.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
