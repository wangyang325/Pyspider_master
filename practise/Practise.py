import os
from multiprocessing import Process

try:
    f = open(r'C:\Users\wangy\Documents\Test.R', 'r')
    ##print(f.read())

finally:
    if f:
        f.close()

##print(os.listdir(r'C:/Users/wangy/Documents/'))


###

def run_proc(name):
    print(r'Main Process is running')


if __name__ == '__main__':
    print(r'father process is running' + str(os.getpid()))
    for i in range(5):
        p = Process(target=run_proc, args=str(i), )
        p.start()
    p.join()
    print('Finished')


