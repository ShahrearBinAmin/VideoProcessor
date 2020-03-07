import cv2
import numpy as np

img=cv2.imread('./images/messi5.jpg')

print(img)
print(img.shape)
print(img[:].shape)

while True:
    #cv2.imshow("Messi", img)
    ball= img[280:340,330:390]
    img[273:333,100:160]=ball

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()