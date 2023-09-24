import cv2

img = cv2.imread('C:/Users/Khaled/Documents/CV Course/1/Computer-Vision-with-Python/DATA/00-puppy.jpg')

w_ratio = 0.5
h_ratio = 0.5
new_img = cv2.resize(img,(0,0),img,w_ratio,h_ratio)

while True:
    cv2.imshow('Puppy',new_img)
    
    # wait for at least 1 ms and pressed the ESC button
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()