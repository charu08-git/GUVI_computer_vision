import cv2
import matplotlib.pyplot as plt
img=cv2.imread("image.jpeg")
print(img.shape)
cv2.rectangle(img,(120,120,),(500,500),(255,0,0),10)
cv2.line(img,(100,100),(1000,1500),(0,255,0),3)
resize=cv2.resize(img,(1400,1400))
plt.imshow(cv2.cvtColor(resize,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()