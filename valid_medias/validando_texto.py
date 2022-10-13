
def Varretexto(arquivo):
    index = 0
    lista_string = ['Shell: quit', 'string']
    file1 = open(arquivo, "r")
    for line in file1:
        index += 1
        for i in range(len(lista_string)):
            string1 = lista_string[i]
            if string1 in line:
                print('->', string1, '<-', 'encontrado na linha', index)
            else:
                pass
            #     #print(index, 'Não encontrado')
    file1.close
    return index


varrer = Varretexto('/home/luzia-tpv/Documents/Aulas/guppe/valid_medias/tvlog.txt')
print('\n Total de linhas percorridas:', varrer)