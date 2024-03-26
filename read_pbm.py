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
                    width = int(dimensions[0])
                    height = int(dimensions[1])
                    break

            image = np.zeros((height, width), dtype=bool)

            for i in range(height-1):
                for j in range(width-1):
                    temp = f.read(1)
                    if (temp != '\n'):
                        pixel_value = int(temp)
                        image[i][j] = pixel_value
            
            return width, height, image

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return None
    except Exception as e:
        print("An error occurred: ", e)
        return None
    # print(imagem)

# lorem_s12_c02_espacos, linhas = 102, palavras = 476
