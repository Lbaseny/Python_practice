# 请手写一个异步函数 get_name()。
# 1. 函数内部使用 await 等待一个异步操作。
# 2. 异步操作完成后返回字符串 "Tom"。
# 3. 最后调用 get_name()，并正确获取它返回的结果。
import asyncio


async def get_name():
    print('异步操作')
    return 'Tom'

async def main():
    res = await get_name()
    print(res)


asyncio.run(main())