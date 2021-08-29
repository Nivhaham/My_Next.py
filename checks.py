import math
import numpy as np

def fibo(n, num1=0, num2=1, index=2):
    if index==n:
        return num2
    tmp = num1
    num1 = num2
    num2 += tmp
    index += 1
    return fibo(n, num1, num2, index)
def gen_sec():
    while True:
        gen_sec = (f"{secs:02}" for secs in range(60))
        for i in gen_sec:
            yield i
def main():
    #print(fibo(15))
    #np.linalg.qr
    #A=np.array([[1,2,3,4],[2,4,-4,8],[-5,4,1,5],[5,0,-3,-7]])
    #A.li
    #gen_date_time= (f"{hour:02}:{mins:02}:{secs:02}" for hour in range(24) for mins in range(60) for secs in range(60))
    #for i in gen_date_time:
    #    print(i)
    secs = gen_sec()
    for i in secs:
        print(i)

if __name__ == '__main__':
    main()
