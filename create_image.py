# importing module 
import cv2
import numpy

# creating First Image
img1=numpy.zeros((200,350,3))
img1[:100][:100]=[0,255,255]
cv2.imshow('img1',img1)
cv2.waitKey()
cv2.destroyAllWindows()

# creating Second Image
img2=numpy.zeros((200,350,3))
img2[:100][:100]=[0,0,255]
cv2.imshow('img2',img2)
cv2.waitKey()
cv2.destroyAllWindows()

# creating final image
final_img=numpy.vstack((a,b))
cv2.imshow('final_img',final_img)
cv2.waitKey()
cv2.destroyAllWindows()
