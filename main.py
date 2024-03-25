# Run erode in the image
# With the result dilate it
# Split array in many parts and create threads to process each one
# Remove asgray from the function since all the P1 will be only black and white
import numpy as np
import read_pbm
import morphology

def main():
    print("Bem-vindo ao PBM_WordDetector!")
    width, height, img = read_pbm.read_pbm("./assets/lorem_s12_c02_noise.pbm")
    result = morphology._dilation(img, True, 1, np.ones((100, 1), dtype=np.int64))
    final_result = morphology._erosion(result, True, 1, np.ones((100, 1), dtype=np.int64))
    data = [[str(item) for item in row] for row in final_result]
    with open('./results.pbm', 'w') as file:
        file.write('P1\n')
        file.write('# CREATOR: GIMP PNM Filter Version 1.1\n')
        file.write(f'{width} {height}\n')
        print("Header generated successfully")
        for row in data:
            file.write(''.join(row) + '\n')
        print("File results.pbm generated successfully!")

if __name__ == "__main__":
    main()


# lorem_s12_c02_espacos, linhas = 102, palavras = 476
