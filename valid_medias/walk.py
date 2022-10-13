import fnmatch
import os
import valid_medias.validando_texto as validando_texto

path = "/home/luzia-tpv/ATE/reports/"
arquivo = 'tvlog.txt'


def BuscaPastas(path):
    lista_pastas = []
    for _, subpastas, arquivos in os.walk(path, topdown=True):
        for pasta in subpastas:
            lista_pastas.append(pasta)
        return lista_pastas

def BuscaArquivo(caminho):
    for _, _, arquivos in os.walk(caminho, topdown=True):
        for file in arquivos:
            if fnmatch.fnmatch(file, str(arquivo)):
                return file


diretorios = BuscaPastas(path)

lista_dir = diretorios
print(len(lista_dir))
print(lista_dir)

for i in range(len(lista_dir)):
    caminho = path + lista_dir[i]
    busca_tvlog = BuscaArquivo(caminho)
    if busca_tvlog == 'tvlog.txt':
        print('Pasta: ', caminho)
        validando_texto.Varretexto(busca_tvlog)