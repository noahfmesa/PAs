# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:47:41 2024

@author: NFCMesa
"""

import numpy as np

#%%

#PART 1:

# 4. 

expression = np.poly1d([2,3,0,1])
print(expression,"\n")

answer = expression(2)
print(answer)

#%%

import numpy as np

# 5. 

expression = np.poly1d([1,0,1])
print(expression,"\n")

derivative = np.polyder(expression)
print(derivative,'\n')

answer = derivative(1)
print(answer)

#%%

#PART 2:

import numpy as np    

# 1. 

coefficients = []

degree = int(input('What is the highest degree of your desired polynomial? '))

for i in range(degree,-1,-1):
    coefficient = int(input(f'What is the coefficient of the variable whose degree is {i}? '))
    coefficients.append(coefficient)
    
polynomial = np.poly1d(coefficients)
print(polynomial, '\n')

derivative = np.polyder(polynomial)

x_1 = float(input('Guess what a root of the polynomial is: '))

def check_thousandths_place(x_1, x_2):
    x_1_thousandth = int(x_1 * 1000) % 10
    x_2_thousandth = int(x_2 * 1000) % 10
    return x_1_thousandth == x_2_thousandth

def NewtonsMethod(x_1):
    print(x_1)
    x_2 = x_1 - (polynomial(x_1))/(derivative(x_1))
    if check_thousandths_place(x_1, x_2):
        print(x_2)
        print(f'The final value with stabilized thousandths place is: {x_2}')
    else: 
        NewtonsMethod(x_2)
    print(polynomial.roots)
        
NewtonsMethod(x_1)
        
    
    
   
   
    
        
        


# polynomial = np.poly1d(coefficients)
# print(polynomial)

