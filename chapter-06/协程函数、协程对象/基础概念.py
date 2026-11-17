"""请定义一个名为 hello 的协程函数"""
# 要求：
# 1. 函数内部打印 "Hello Python"。
# 2. 调用该函数，将得到的结果赋值给变量 result。
# 3. 判断 result 是不是协程对象，并打印判断结果

async def task():
    print('Hello Python')

result = task()

print(result)