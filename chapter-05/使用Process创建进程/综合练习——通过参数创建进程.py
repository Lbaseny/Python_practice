from multiprocessing import Process
"""场景：

某程序需要创建一个进程，负责处理指定用户的任务。不同用户启动进程时，需要传入不同的用户名。"""

# 要求：
# 1. 定义一个函数，接收一个用户名参数。
# 2. 函数打印该用户名对应的任务提示，例如：张三正在处理任务！
# 3. 使用 Process 创建两个子进程。
# 4. 分别向两个子进程传递不同的用户名：张三、李四。
# 5. 启动两个子进程。

def work(user):
    print(f'{user}正在处理任务！')

if __name__ == '__main__':

    p1 = Process(target=work,name='A进程',args=('张三',))
    p2 = Process(target=work,name='B进程',args=('李四',))

    p1.start()
    p2.start()

