# Run erosion in the image
# With the result dilate it
# Split array in many parts and create threads to process each one
# Remove asgray from the function since all the P1 will be only black and white

import numpy as np
import read_pbm
import morphology
import cv2
from datetime import datetime
from multiprocessing import Pool, cpu_count

def process_part(part):
    # Apply dilation to the part
    # part = morphology.dilation(part, np.ones((2, 2), dtype=np.uint8))

    # print(f"Opening completed successfully at {datetime.now()}")
    return part

def revert_img_pixels(img, width, height):
    for i in range(height - 1):
        for j in range(width - 1):
            if (img[i][j] == 0):
                img[i][j] = 1
            else:
                img[i][j] = 0
    return img

def main():
    print("PBM_WordDetector!")
    print(f"Started at {datetime.now()}")
    width, height, img = read_pbm.read_pbm("./assets/lorem_s12_c02_noise.pbm")
    # final_result = cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8), iterations=1)
    final_result = cv2.dilate(final_result, np.ones((1, 100), np.uint8), iterations=1)
    # final_result = cv2.erode(final_result, np.ones((5, 5), np.uint8), iterations=1)
    # final_result = cv2.erode(final_result, np.ones((4, 4), np.uint8), iterations=1)
    # final_result = cv2.erode(final_result, np.ones((3, 3), np.uint8), iterations=1)
    # final_result = morphology.erosion(img, np.ones((100, 1), dtype=np.uint8))
    # final_result = morphology.dilation(img, np.ones((100, 1), np.uint8))
    # result = cv2.erode(img, np.ones((2,2), np.uint8), iterations=1)
    # final_result = cv2.dilate(result, np.ones((2,2), np.uint8), iterations=1)
    # threads_amount = cpu_count()
    # part_height = height // threads_amount
    # remainder = height % threads_amount
    # start_row = 0

    # parts = []

    # # Split the image array into many parts
    # for i in range(threads_amount):
    #     end_row = start_row + part_height + (1 if i < remainder else 0 )
    #     part = img[start_row:end_row]
    #     parts.append(part)
    #     start_row = end_row
    
    # with Pool(threads_amount) as pool:
    #     results = pool.map(process_part, parts)
    #     pool.close()
    #     pool.join()
    #     print("Pool finished")
    # print("Starting result")
    # final_result = np.vstack(results)
    # final_result = revert_img_pixels(final_result, width, height)

    # print(f"Dilation completed successfully at {datetime.now()}")
    # final_result = morphology._erosion(final_result, True, np.ones((50, 1), dtype=np.uint8))
    # print(f"Erosion completed successfully at {datetime.now()}")
    data = [[str(item) for item in x] for x in final_result]
    with open('./results.pbm', 'w') as file:
        file.write('P1\n')
        file.write('# CREATOR: GIMP PNM Filter Version 1.1\n')
        file.write(f'{width} {height}\n')
        print("Header generated successfully")
        for row in data:
            file.write(''.join(row) + '\n')
        print(f"File results.pbm generated successfully! at {datetime.now()}")
        

if __name__ == "__main__":
    main()


# lorem_s12_c02_espacos, linhas = 102, palavras = 476
