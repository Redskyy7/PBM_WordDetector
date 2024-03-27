import numpy as np

def read_pbm(file_path):
    """Reads a Portable Bitmap (PBM) file and extracts the dimensions and pixel values of the binary image."""
    try:
        with open(file_path) as f:
            magic_number = f.readline().strip()
            if magic_number != "P1":
                print("Error: Invalid PBM file format")
                return None
            
            while (True):
                temp = f.readline()
                if temp.startswith('#'):
                    continue
                else:
                    dimensions = temp.split()
                    rows_amount = int(dimensions[0])
                    columns_amount = int(dimensions[1])
                    break
            
            # Reading pixels array and only going to next row after having completed fully the 
            image = np.zeros((columns_amount, rows_amount), dtype=int)
            i, j = 0, 0
            while True:
                char = f.read(1)
                if not char:
                    break
                elif char in ['0', '1']:
                    image[i][j] = int(char)
                    j+= 1
                    if j == rows_amount:
                        j = 0
                        i += 1
                        if i == columns_amount:
                            break
                elif char == '\n':
                    continue
                else:
                    print("Error: Invalid character in PBM file")
            
            # return width, height, image
        return rows_amount, columns_amount, image

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return None
    except Exception as e:
        print("An error occurred: ", e)
        return None
    # print(imagem)

# lorem_s12_c02_espacos, linhas = 102, palavras = 476
