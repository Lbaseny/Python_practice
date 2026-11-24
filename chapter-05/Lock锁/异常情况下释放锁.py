"""假设线程在执行临界区代码时，可能发生异常。"""
import threading
from threading import Thread

# 要求：
# 1. 创建一个 threading.Lock() 对象。
# 2. 使用 acquire() 获取锁。
# 3. 执行临界区代码。
# 4. 临界区代码发生异常时，仍然必须释放锁。
# 5. 必须使用 acquire() 和 release()，不能使用 with。
# 请写出完整 Python 代码。

def task(lock):
    lock.acquire()
    try:
        print('正在执行临界区代码')
    finally:
        lock.release()
if __name__ == '__main__':
    lock = threading.Lock()
    t = Thread(target=task,args=(lock,))
    t.start()
