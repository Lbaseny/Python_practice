# 要求：
import asyncio


# 请手写一个异步函数 get_info()。
# 1. 第一次使用 await 等待一个异步操作，得到数字 10。
# 2. 第二次使用 await 等待另一个异步操作，得到数字 20。
# 3. 将两个结果相加并返回。
# 4. 最终获取函数的返回值。

async def get_info(n):
    print('异步操作')
    return n

async def main():
    x = await get_info(10)
    y = await get_info(20)
    res = x + y
    return res

result = asyncio.run(main())
print(result)

