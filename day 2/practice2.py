import cv2
import matplotlib.pyplot as plt
img=cv2.imread("image2.jpeg")
(h,w)=img.shape[:2]
print(img.shape)
cv2.rectangle(img,(50,50),(100,100),(0,255,0),2)
cv2.line(img,(150,150),(100,100),(255,0,0),10)
RM=cv2.getRotationMatrix2D((w//2,h//2),45,1)
rotated=cv2.warpAffine(img,RM,(w,h))
plt.imshow(cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB))
plt.show()