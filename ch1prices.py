# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 23:42:04 2018

@author: ckory
"""

import numpy as np
import matplotlib.pyplot as plt
#列表
x,y = [],[]
#open用法，文件地址链接用斜线，同时'r'是指读写模式，默认为只读模式
for sample in open("C:/Users/ckory/Downloads/python与机器学习实战/study/prices.txt","r"):
    
    #运行时报错，因为数据集的格式问题，数据之间不能有换行符号，否则无法执行split
    _x,_y=sample.split(",")
    
    #将字符append进列表
    x.append(float(_x))
    y.append(float(_y))
    
    #np。array数组是一种数据形式，可以进行数据操作必须的格式
x,y=np.array(x),np.array(y)
x=(x-x.mean())/x.std()

#figure定义图片大小，scatter定义图形类型
plt.figure()
plt.scatter(x,y,c="r",s=18)

#plt.show执行后图片很小，可以通过tools-references-ipythonconsole-graphics-backend-automatic 调整，记得变更之后要重启spyder
plt.show()


#linespace的用法，将-2至4之间均分为100等份
x0=np.linspace(-2,4,100)
def get_model(deg):
    #什么时候使用lambda?
    #调用不同包中的函数，类似在不同层级的文件夹中找文件，该包中必须有该文件才能被打开
    #plotfit函数中输入的是之前的x,y,则能得到损失函数最小的p系数值，带入polyval之后得到根据模型计算得出的y值
    return lambda input_x=x0:np.polyval(np.polyfit(x,y,deg),input_x)
def get_cost(deg,input_x,input_y):
    #求损失函数
    return 0.5*((get_model(deg)(input_x)-input_y)**2).sum()

test_set=(1,4,10)
for d in test_set:
    print(get_cost(d,x,y))
plt.scatter(x,y,c="g",s=20)
for d in test_set:
    plt.plot(x0,get_model(d)(),label="degree={}".format(d))
plt.xlim(-2,4)
plt.ylim(1e5,8e5)
#显示图例
plt.legend()
plt.show()
    