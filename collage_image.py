# importing module
import cv2
import numpy

# reading first image
img1=cv2.imread("monk.jpg")
img1_ed=img1[:183,:275]
cv2.imshow('h',img1_ed)
cv2.waitKey()
cv2.destroyAllWindows()

#reading second imgae 
img2=cv2.imread("pand.jpg")
cv2.imshow('h',img2)
cv2.waitKey()
cv2.destroyAllWindows()

# stacking image for making collage
collage=numpy.hstack((img1_ed,img2))
cv2.imshow('h',collage)
cv2.waitKey()
cv2.destroyAllWindows()
