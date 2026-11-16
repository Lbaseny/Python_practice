"""场景：
你正在开发一个订单处理系统，每个子进程负责处理一个订单，需要接收订单编号、客户姓名和订单金额三个信息。
"""
# 编程要求：
# 1. 定义一个名为 process_order 的函数。
# 2. 函数接收三个参数：
#    - 订单编号 order_id
#    - 客户姓名 username
#    - 订单金额 price
# 3. 函数打印订单信息。
# 4. 使用 Process 创建两个子进程。
# 5. 两个进程分别传入以下信息：

from multiprocessing import Process


def process_order(order_id,username,price):
    print(f'{order_id}--{username}(先生/女士)消费{price}元')

if __name__ == '__main__':

    A = Process(target=process_order,name='进程A',args=(1001,'张三',299))
    B = Process(target=process_order,name='进程B',args=(1002,'李四',599))

    A.start()
    B.start()
