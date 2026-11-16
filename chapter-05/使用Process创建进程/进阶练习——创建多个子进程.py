"""场景：
某任务管理程序需要同时创建两个子进程，分别执行不同的任务。"""

# 要求：
# 1. 创建两个不同的自定义函数。
# 2. 第一个函数打印：任务A正在执行！
# 3. 第二个函数打印：任务B正在执行！
# 4. 使用 Process 分别创建两个子进程。
# 5. 分别启动这两个子进程。

from multiprocessing import  Process

def work_a():
    print('任务A正在执行！')

def work_b():
    print('任务B正在执行！')

if __name__ == '__main__':

    p1 = Process(target=work_a,name='A进程')
    p2 = Process(target=work_b,name='B进程')

    p1.start()
    p2.start()
