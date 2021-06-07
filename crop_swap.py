# importing module
import cv2

# reading first image
img1=cv2.imread("img1.jpg")
cv2.imshow('img1',img1)
cv2.waitKey()
cv2.destroyAllWindows()

# reading second image
img2=cv2.imread("image_2.jpg")
cv2.imshow('h',img2)
cv2.waitKey()
cv2.destroyAllWindows()

# cropping some part of first image
img1_crop=img1[40:140,25:130]
cv2.imshow('img1_crop',img1_crop)
cv2.waitKey()
cv2.destroyAllWindows()

# cropping some part of second image
img2_crop=img2[30:130,30:140]
cv2.imshow('img2_crop',img2_crop)
cv2.waitKey()
cv2.destroyAllWindows()

# Again reading image
img1=cv2.imread("img1.jpg")
img2=cv2.imread("image_2.jpg")

# swapping cropped part of first image to second image
img2[40:140,25:130]=img1_crop
cv2.imshow('h',img2)
cv2.waitKey()
cv2.destroyAllWindows()

# swapping cropped part of second image to first image
img1[30:130,30:140]=img2_crop
cv2.imshow('h',img1)
cv2.waitKey()
cv2.destroyAllWindows()
