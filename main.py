# import Opencv library
import cv2
import os
import numpy as np

path_file = input("Enter convert images folder: ")
save_to_path = input("Enter what save you path: ")
data_item_name = input("Enter your data item name: ")
max_number_of_item = input("Enter max item number: ")

img = cv2.imread(f"{path_file}/{data_item_name}1.jpg", cv2.IMREAD_COLOR)

data_item_len = len(data_item_name)

# get range file
slice1 = slice(data_item_len, 6)  # 1 - 9
slice2 = slice(data_item_len, 7)  # 10 - 99

# change size reduce %30
scale_percent = 80

width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# define the color range
# lower boundary RED color range values; Hue (0 - 10)
lower1 = np.array([0, 100, 20])
upper1 = np.array([10, 255, 255])

# upper boundary RED color range values; Hue (160 - 180)
lower2 = np.array([160, 100, 20])
upper2 = np.array([179, 255, 255])

# loop
x = 1

max_number_of_item = int(max_number_of_item)
while x <= max_number_of_item:
    if max_number_of_item < 10:
        file_name = os.path.basename(f"./datas/blood{x}.jpg")
        print(file_name[slice1])
        img = cv2.imread(f"{path_file}/blood{x}.jpg", cv2.IMREAD_COLOR)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        hsv_img1 = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
        lower_mask = cv2.inRange(hsv_img1, lower1, upper1)
        upper_mask = cv2.inRange(hsv_img1, lower2, upper2)
        full_mask = lower_mask + upper_mask
        color_img1 = cv2.bitwise_and(resized, resized, mask=full_mask)

        cants = cv2.findContours(full_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cants = cants[0] if len(cants) == 2 else cants[1]
        for cant in cants:
            cv2.drawContours(color_img1, [cant], -1, (36, 255, 12), 1)

        cv2.imwrite(f"{save_to_path}/blood{x}.jpg", color_img1)

        x += 1
    elif max_number_of_item >= 10:
        file_name = os.path.basename(f"./datas/blood{x}.jpg")
        print(file_name[slice2])
        img = cv2.imread(f"{path_file}/blood{x}.jpg", cv2.IMREAD_COLOR)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        hsv_img1 = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
        lower_mask = cv2.inRange(hsv_img1, lower1, upper1)
        upper_mask = cv2.inRange(hsv_img1, lower2, upper2)
        full_mask = lower_mask + upper_mask
        color_img1 = cv2.bitwise_and(resized, resized, mask=full_mask)

        cants = cv2.findContours(full_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cants = cants[0] if len(cants) == 2 else cants[1]
        for cant in cants:
            cv2.drawContours(color_img1, [cant], -1, (36, 255, 12), 1)

        cv2.imwrite(f"{save_to_path}/blood{x}.jpg", color_img1)

        x += 1
