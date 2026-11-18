"""题目背景： 模拟三个连续的数据处理步骤。"""
# 请手写三个异步函数：
# 1. step_one()
# - 返回数字 10。
# 2. step_two(value)
# - 接收一个数字。
# - 返回传入数字乘以 2。
# 3. step_three(value)
# - 接收一个数字。
# - 返回传入数字加上 5。
# 最终函数 main() 的要求：
# 1. 使用 await 等待 step_one()，获取结果。
# 2. 将结果传递给 step_two()，使用 await 等待并获取结果。
# 3. 将第二步结果传递给 step_three()，使用 await 等待并获取结果。
# 4. 返回最终结果。

import asyncio

async def step_one():
    return 10
async def step_two(value):
    return value * 2
async def step_three(value):
    return value + 5

async def main():
    res1 = await step_one()
    res2 = await step_two(res1)
    res3 = await step_three(res2)
    return res3
if __name__ == '__main__':
    result = asyncio.run(main())
    print(result)
