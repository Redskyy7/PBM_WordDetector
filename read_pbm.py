def read_pbm(file_path):
    with open(file_path) as f:
        data = [x for x in f if not x.startswith('#')]
        largura, altura = map(int, data[1].split())
        imagem = [[0]*largura]*altura
        for i in range(altura-2):
            for j in range(largura-2):
                imagem[i][j] = data[2]
    print(imagem)
