"""有一个共享变量：
count = 0
现在创建两个线程，每个线程对 count 累加 1000 次。"""
import threading
from threading import Thread

# 要求：
# 1. 使用 threading.Lock() 创建锁。
# 2. 每次修改 count，必须先获取锁。
# 3. 修改完成后释放锁。
# 4. 最终输出必须是 2000。

count = 0

def task(lock):
    lock.acquire()
    global count
    for x in range(1000):
        count+=1
    lock.release()

if __name__ == '__main__':
    lock = threading.Lock()

    t1 = Thread(target=task,args=(lock,))
    t2 = Thread(target=task,args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f'count最终的值为：{count}')