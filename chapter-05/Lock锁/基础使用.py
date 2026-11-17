"""创建一个 threading.Lock() 锁对象。"""

# 请写出代码，实现以下要求：
# 1. 创建一个锁对象 lock。
# 2. 主动获取锁。
# 3. 打印 "正在执行临界区"。
# 4. 释放锁。

import threading
from threading import Thread

def task(lock):
    lock.acquire()
    print('正在执行临界区')
    lock.release()

if __name__ == '__main__':

    lock = threading.Lock()
    t = Thread(target=task,args=(lock,))
    t.start()