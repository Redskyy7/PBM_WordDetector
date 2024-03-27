# Run erosion in the image
# With the result dilate it
# Split array in many parts and create threads to process each one
# Remove asgray from the function since all the P1 will be only black and white

import numpy as np
import read_pbm
import morphology
from datetime import datetime
from multiprocessing import Pool, cpu_count

def process_part(part):
    # Apply dilation to the part
    # part = morphology._dilation(part, True, np.ones((100, 1), dtype=np.uint8))
    # print(f"Dilation completed successfully at {datetime.now()} on thread {part}")
    part = morphology._opening(part, True, np.ones((3, 3), dtype=np.uint8))
    print(f"Opening completed successfully at {datetime.now()}")
    return part
    # return morphology._erosion(part, True, np.ones((100, 1), dtype=np.uint8))

def revert_img_pixels(img, width, height):
    for i in range(height - 1):
        for j in range(width - 1):
            img[i][j] = ~img[i][j]
    return img

def main():
    print("PBM_WordDetector!")
    print(f"Started at {datetime.now()}")
    width, height, img = read_pbm.read_pbm("./assets/lorem_s12_c02_noise.pbm")
    print(f"PBM file readed successfully at {datetime.now()}")
    # result = morphology._dilation(img, True, 1, np.ones((50, 1), dtype=np.uint8))

    threads_amount = cpu_count()
    part_height = height // threads_amount
    remainder = height % threads_amount
    start_row = 0

    parts = []

    # Split the image array into many parts
    for i in range(threads_amount):
        end_row = start_row + part_height + (1 if i < remainder else 0 )
        part = img[start_row:end_row]
        parts.append(part)
        start_row = end_row
    
    with Pool(threads_amount) as pool:
        results = pool.map(process_part, parts)
        pool.close()
        pool.join()

    final_result = np.vstack(results)
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
