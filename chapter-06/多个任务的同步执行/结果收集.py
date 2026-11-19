"""编写一个 Python 程序，模拟同时执行 4 个数据处理任务。"""
import asyncio
from datetime import datetime


# 任务要求：
# 1. 创建 4 个任务，分别处理以下数据：
# - 任务 A：处理 10 条数据，耗时 2 秒
# - 任务 B：处理 20 条数据，耗时 3 秒
# - 任务 C：处理 30 条数据，耗时 1 秒
# - 任务 D：处理 40 条数据，耗时 4 秒
# 2. 每个任务开始时打印任务名称和开始信息。
# 3. 每个任务结束时打印任务名称和处理的数据数量。
# 4. 4 个任务必须同步执行。
# 5. 主程序需要收集每个任务的执行结果。
# 6. 所有任务完成后，统一打印每个任务处理的数据数量。
# 7. 最后统计并打印总共处理了多少条数据。

async def task(name,n,time):
    print(f'任务{name}开始处理任务，预计耗时{time}')
    await asyncio.sleep(time)
    print(f'任务{name}已完成，共处理{n}条数据')
    return n
async def main():
    start = datetime.now()
    result = await asyncio.gather(task('A',10,2),
                                  task('B',20,3),
                                  task('C',30,1),
                                  task('D',40,4))
    res = sum(result)
    print(f'任务已全部完成，总耗时{datetime.now() - start},共处理{res}条数据')

if __name__ == '__main__':
    asyncio.run(main())