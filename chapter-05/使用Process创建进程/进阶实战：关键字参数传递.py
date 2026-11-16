
"""场景：
某数据处理程序需要创建三个不同的任务进程，每个进程接收不同的用户信息和任务配置。"""

# 要求：
# 1. 定义函数 work，接收三个参数：
#    - username
#    - task
#    - level
# 2. 函数打印用户、任务和等级信息。
# 3. 创建三个进程，分别传入：
# 4.使用 Process 创建三个进程。
# 5.使用关键字参数传递数据。
# 6.为三个进程分别指定不同的名称。
# 7.启动三个进程。
from multiprocessing import Process

def work(username,task,level):
    print(f'{username}的任务是{task}任务等级是{level}级')

if __name__ == '__main__':

    A = Process(target=work,name='A',kwargs={'username':'张三','task':'数据分析','level':1})
    B = Process(target=work,name='B',kwargs={'username':'李四','task':'文件整理','level':2})
    C = Process(target=work,name='C',kwargs={'username':'王五','task':'数据统计','level':3})

    A.start()
    B.start()
    C.start()
