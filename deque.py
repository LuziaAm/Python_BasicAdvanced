"""
Deque é uma lista de auta performance

"""

from collections import deque

deq = deque('Luzia Amorim')

print(deq)

# Adicionando

deq.append('!')
deq.appendleft('->')# Add no inicio

print(deq)

deq.pop()
deq.popleft()#Remove do inicio


print(deq)
