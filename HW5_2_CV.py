import numpy as np
import cv2
from urllib.request import urlopen

def nothing(x):
    pass

req = urlopen('https://dobrovserdce.ru/images/2022/11/02/kot%20Fedya_large.jpeg')
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img_hong = cv2.imdecode(arr, -1)
img = np.asarray(cv2.resize(cv2.cvtColor(img_hong, cv2.COLOR_BGR2GRAY),(int(img_hong.shape[1] * 0.5), int(img_hong.shape[0] * 0.5))))
cv2.namedWindow('Laplacian')
cv2.createTrackbar('ksize','Laplacian',0,30,nothing)
while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    ks = cv2.getTrackbarPos('ksize','Laplacian')
    if ks%2 ==0:
        ks = ks+1
    laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize = ks)
    cv2.imshow('Laplacian', laplacian)
cv2.destroyAllWindows()