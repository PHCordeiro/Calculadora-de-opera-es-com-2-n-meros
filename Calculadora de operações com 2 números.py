#!/usr/bin/env python
# coding: utf-8

# Vou TENTAR fazer uma calculadora

# In[10]:


def soma(numero1, numero2): 
    soma = numero1 + numero2
    return soma

def subtracao(numero1, numero2): 
    subtracao = numero1 - numero2
    return subtracao

def divisao(numero1, numero2): 
    divisao = numero1 / numero2
    return divisao

def multiplicacao(numero1, numero2): 
    multiplicacao = numero1 * numero2
    return multiplicacao 
    
def resultado(valor):
    print(f'O resultado da operação é {valor}')
    return resultado


numero1 = int(input("Digite o primeiro número "))
numero2 = int(input("Digite o segundo número "))
conta = int(input('1 para soma, 2 para subtração, 3 para divisão e 4 para multiplicação: '))

if(conta == 1):
    resultado(soma(numero1, numero2))

if(conta == 2):
    resultado(subtracao(numero1, numero2))
    
if(conta == 3):
    resultado(divisao(numero1, numero2))

if(conta == 4):
    resultado(multiplicacao(numero1, numero2))



# In[ ]:





# In[ ]:





# In[ ]:




