import cv2
# sudo apt-get install python-opencv
imgName = "output.tiff"
kernel_size = (5, 5)
sigma = 1.5

img = cv2.imread(imgName)
img = cv2.GaussianBlur(img, kernel_size, sigma)
new_imgName = "New_" + str(kernel_size[0]) + "_" + str(sigma) + "_" + imgName
print 'new_imgName', new_imgName
cv2.imwrite(new_imgName, img)