def read_pbm(file_path):
    with open(file_path) as f:
        data = [x for x in f if not x.startswith('#')]
        largura, altura = data[1].split()
        # for i in range(altura):
        #     for j in range(largura):


    # dimensions = map(int,data.pop(0).split())
    # arr = []
    # col_number = 0
    # for c in data.pop(0):
    #     if(col_number > dimensions[0]):
    #         col_number = 0 
    return int(largura), int(altura)