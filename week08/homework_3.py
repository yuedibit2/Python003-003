#实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
from time import time
import numpy as np
def timer(func):
    def inner(*args,**kargs):
        time1=time()
        ret=func(*args,**kargs)
        print(f'The runtime of the function is {time()-time1}')
        return ret
    return inner

@timer
def diy_sum(*args,**kargs):
    result=0
    for i in args:
        result+=sum(i)
    return result

diy_sum(list((range(100))))



