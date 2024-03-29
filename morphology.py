import numpy as np
from itertools import product
from datetime import datetime


def dilation (img, sel):
    height, width = img.shape
    height_sel, width_sel = sel.shape
    result = np.zeros((height, width), dtype=np.uint8)
    
    # Gets the offset value to use and get the neighbors, increments 1 if the height or width is odd
    offset_height = height_sel // 2
    offset_height_aux = offset_height
    if (height_sel % 2 == 1):
        offset_height_aux += 1

    offset_width = width_sel // 2
    offset_width_aux = offset_width
    if (width_sel % 2 == 1):
        offset_width_aux += 1

    # Iterate in the img array and checks for the positions of the sel
    for i in range (offset_height, height - offset_height):
        for j in range (offset_width, width- offset_width):
            neighborhood = img[i - offset_height: i + offset_height_aux, j - offset_width: j + offset_width_aux]
            dilated_value = np.max(neighborhood * sel)
            result[i,j] = dilated_value

    print(f"Dilation completed successfully at {datetime.now()}")
    return result

def erosion (img, sel):
    height, width = img.shape
    height_sel, width_sel = sel.shape
    result = np.zeros((height, width), dtype=np.uint8)

    # Gets the offset value to use and get the neighbors, increments 1 if the height or width is odd
    offset_height = height_sel // 2
    offset_height_aux = offset_height
    if (height_sel % 2 == 1):
        offset_height_aux += 1

    offset_width = width_sel // 2
    offset_width_aux = offset_width
    if (width_sel % 2 == 1):
        offset_width_aux += 1

    # Iterate in the img array and checks for the positions of the sel
    for i in range (offset_height, height - offset_height):
        for j in range (offset_width, width - offset_width):
            neighborhood = img[i - offset_height: i+ offset_height_aux, j - offset_width: j + offset_width_aux]
            eroded_value = np.min(neighborhood * sel)
            result[i,j] = eroded_value

    print(f"Erosion completed successfully at {datetime.now()}")
    return result

def opening(img, sel):
    result = erosion(img, sel)
    result = dilation(result, sel)
    return result

def closing(img, sel):
    result = dilation(img, sel)
    result = erosion(result, sel)
    return result
