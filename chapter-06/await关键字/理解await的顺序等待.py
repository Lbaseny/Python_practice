# 请手写一个异步函数 task()：
# 1. 第一个异步操作完成后，打印 "第一步完成"。
# 2. 第二个异步操作完成后，打印 "第二步完成"。
# 3. 第二个操作必须等第一个操作完成后才能执行。
# 4. 最后返回 "全部完成"。
# 5. 正确调用函数并打印最终返回值。
import asyncio

async def task(msg):
    print(f'{msg}任务完成')

async def main():
    await task('第一步')
    await task('第二步')
    return '任务全部完成'

res = asyncio.run(main())
print(res)
