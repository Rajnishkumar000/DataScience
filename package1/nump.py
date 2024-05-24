import numpy as np
import seaborn as sns
import pandas as pd
my_lst1=[1,2,3,4,5]
my_lst2=[1,2,3,4,5]
my_lst3=[1,2,3,4,5]
arr=np.array([my_lst1,my_lst2,my_lst3])
print(arr)
print(type(arr))
print(arr.shape)
# print(arr[3:][2:])
print(np.arange(5,33))
print(np.arange(0,20,step=2))
arr_ex=np.random.randn(3,5)
print(sns.displot(pd.DataFrame(arr_ex.reshape(15,1))))
# ls = [3,45,2,45,34]
# for i in range(len(ls)):
#     print(ls[i])
#
# i = 0
# while i<len(ls):
#     print(ls[i])
#     i+=1
#
# lis = [i for i in range(30) if i%2 == 0]
# print(lis)
#
# f = open("myFile.txt","r")
#
# print(f.read())
# f.close()

import pyautogui as py
# import time as t
# t.sleep(5)
# py.hotkey('alt', 'f4')
# py.hotkey('enter')