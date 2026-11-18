"""这道题考查一个异步函数内部等待另一个异步函数，并获取其返回值。"""
import asyncio


# 题目要求：
# 请手写两个异步函数：
# 1. get_age()：返回数字 18。
# 2. get_user()：
#    - 使用 await 等待 get_age()。
#    - 获取年龄。
#    - 返回字符串 "用户年龄：18"，其中年龄必须使用获取到的结果拼接，不能写死。
# 最后使用 asyncio.run() 正确调用，并打印结果。

async def get_age(name):
    age = input('请输入用户年龄：')
    return age

async def get_user():
    name = input('请输入用户名称：')
    return name

async def main():
    name = await get_user()
    age = await get_age(name)
    return f'{name}年龄：{age}'

if __name__ == '__main__':
     print(asyncio.run(main()))

