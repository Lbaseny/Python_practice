# 请编写程序：
# 1. 定义协程函数 func，内部打印 "正在执行"。
# 2. 调用 func()，赋值给变量 obj。
# 3. 打印 obj。
# 4. 使用 type() 打印 obj 的类型。
# 5. 使用 inspect.iscoroutine() 判断 obj 是否为协程对象。
import inspect
from inspect import iscoroutine


async def func():
    print('正在执行')

obj = func()
print(obj)
print(type(obj))
print(inspect.iscoroutine(obj))
