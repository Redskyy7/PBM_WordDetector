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
    
    neighborhood_views = np.lib.stride_tricks.sliding_window_view(img, (height_sel, width_sel))

    # Compute dilated values for each neighborhood
    dilated_values = np.max(neighborhood_views * sel, axis=(2, 3))

    # Assign dilated values to result array
    result[height_sel-1:height, width_sel-1:width] = dilated_values
    
    # print(f"Dilation completed successfully at {datetime.now()}")
    # return result.astype(np.uint8)

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
    neighborhood_views = np.lib.stride_tricks.sliding_window_view(img, (height_sel, width_sel))
    # Compute eroded values for each neighborhood
    eroded_values = np.min(neighborhood_views * sel, axis=(2, 3))

    # Assign eroded values to result array
    result[height_sel-1:height, width_sel-1:width] = eroded_values

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
