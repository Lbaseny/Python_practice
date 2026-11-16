from multiprocessing import Process
"""场景：
你正在编写一个简单的 Python 程序，希望通过创建一个新进程来完成一项独立任务。"""

# 要求：
# 1. 使用 multiprocessing 模块中的 Process 创建一个子进程。
# 2. 子进程执行一个自定义函数。
# 3. 自定义函数只需要打印一句话：子进程正在执行任务！
# 4. 创建并启动该子进程。

def work():
    print('子进程正在执行任务')

if __name__ == '__main__':

    p = Process(target=work,name='进程p')
    p.start()
