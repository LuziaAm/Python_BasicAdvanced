# if __name__ == '__main__':
#     listOne = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
        
#         listOne.append([name, score])

#     for n in range(len(listOne)):
#         nome = []

# def main():
#     tam = int(input('Digite tamanho da sequência: '))
#     soma = 0
#     lista = []
#     for i in range(tam):
#         n = int(input('Digite os números:'))
#         if n != 0:
#             lista.append(n)
        
#     print(lista)
#     print(sum(lista))

# main()

# def main():
#     num = int(input('Digite o número: '))
#     lista = []
#     lista.append(num)
#     while num != 0:
#         num = int(input('Digite o número: '))
#         lista.append(num)
#     #for i in range(len(lista)):
#     #print(lista)
           
#     print(sum(lista))

# main()
class Solution:
    def minJumps(self, arr, n):
        self.arr = list(arr)
        self.n = n
        lista  = self.arr
        indice = 0
        pula = 0
        print(indice)

        conta = 0

    
        for x in range(self.n):
            indice = pula
            pula = lista[indice]
            print(x)
        
        return pula

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = 11


pula = Solution()
print(pula.minJumps(arr, n))