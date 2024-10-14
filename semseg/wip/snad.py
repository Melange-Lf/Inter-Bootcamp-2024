import cv2
import numpy as np

# test = cv2.imread("C:/Users/hp/Documents/code/Py/actual/Ai/inter_boot_2024/semseg/dataset/interboot/train/201/frame0029_leftImg8bit.jpg")
test = cv2.imread("C:/Users/hp/Documents/code/Py/actual/Ai/inter_boot_2024/semseg/dataset/interboot/labels/201/frame0029_gtFine_labelColors.png")
testnp = np.array(test)
print(testnp.shape)
