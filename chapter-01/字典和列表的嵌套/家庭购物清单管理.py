"""你去超市采购了一些生活用品，现在需要编写一个 Python 程序，帮助自己统计购物清单。"""
from itertools import product

# 已有数据：
shopping_list = [{"name": "牛奶", "price": 15, "count": 2, "category": "食品"},
                 {"name": "鸡蛋", "price": 12, "count": 3, "category": "食品"},
                 {"name": "洗衣液", "price": 35, "count": 1, "category": "日用品"},
                 {"name": "苹果", "price": 8, "count": 5, "category": "食品"},
                 {"name": "垃圾袋", "price": 10, "count": 2, "category": "日用品"},
                 {"name": "面包", "price": 12, "count": 2, "category": "食品"}]
# 每个商品包含四个字段：
# 字段	含义
# name	商品名称
# price	商品单价
# count	购买数量
# category	商品类别
# 二、练习任务
# 请独立完成下面 5 个小任务。
# 任务 1：计算购物总金额
# 计算所有商品的总花费。
# 计算公式：
# 商品单价 × 购买数量
# 要求：最后输出一个总金额。
# 任务 2：筛选商品
# 找出所有单价大于 10 元的商品。
# 要求：输出商品名称和单价。
# 任务 3：统计食品数量
# 统计购物清单中，食品类别的商品一共购买了多少件。
# 注意：不是统计有多少种食品，而是统计购买总件数。
# 任务 4：找出最贵的一笔商品支出
# 找出总价最高的商品。
# 注意：
# - 不是单价最高。
# - 而是单价 × 数量之后，金额最高。
# 输出商品名称和总价。
# 任务 5：商品价格排序
# 按照每种商品的总价从高到低排序。

def test1():
    sum_price = 0
    for product in shopping_list:
        sum_price += float(product['price']) * int(product['count'])
    return f'总价格：{sum_price}'
def test2():
    products = []
    for product in shopping_list:
        if float(product['price']) > 10:
            products.append(product['name'])
    return products
def test3():
    products = []
    for product in shopping_list:
        if product['category'] == '食品':
            products.append(product['count'])
    return f'商品总数量：{sum(products)}'
def test4():
    result = max(
        shopping_list,
        key=lambda x:x['price']*x['count']
        )
    return f'总价最高的商品：{result['name']}'
def test5():
    result =sorted(
        shopping_list,
        key=lambda x:float(x['price']) * int(x['count']),
        reverse=True
    )
    return f'排序：{result}'


print(test1())
print(test2())
print(test3())
print(test4())
print(test5())