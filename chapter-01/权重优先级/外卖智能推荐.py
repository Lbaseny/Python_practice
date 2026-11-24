"""场景： 你正在开发一个外卖推荐系统，需要根据价格、评分和配送时间对商家进行优先级排序。"""

weight = {"rating": 0.5,
          "delivery_time": 0.3,
          "price": 0.2}
restaurants = [{"name": "A餐厅", "rating": 4.8, "delivery_time": 35, "price": 30},
               {"name": "B餐厅", "rating": 4.5, "delivery_time": 20, "price": 25},
               {"name": "C餐厅", "rating": 4.9, "delivery_time": 40, "price": 35},
               {"name": "D餐厅", "rating": 4.6, "delivery_time": 25, "price": 20},
               {"name": "E餐厅", "rating": 4.7, "delivery_time": 15, "price": 40}]
# 你的任务：
# 设计一个综合评分公式：
# \[
# Score = rating \times 0.5
# + delivery\_score \times 0.3
# + price\_score \times 0.2
# \]
# 其中：
# - 评分越高，得分越高。
# - 配送时间越短，得分越高。
# - 价格越低，得分越高。
# 提示：你需要先将配送时间和价格转换成可比较的分数，例如：
# delivery_score = 100 - delivery_time
# price_score = 100 - price
# 然后：
# 1. 计算每家餐厅的综合评分。
# 2. 按照综合评分降序排列。
# 3. 输出排名、餐厅名称和综合得分。
class Dinner:
    def __init__(self,name,rating,delivery_time,price):
        self.name = name
        self.rating = rating
        self.delivery_time = delivery_time
        self.price = price

    def score(self,weight):
        delivery_score = 60 - self.delivery_time
        price_score = 100 -self.price
        core = (self.rating * weight['rating']
                + delivery_score*weight['delivery_time']
                + price_score*weight['price'])
        return core

dinners = []
for d in restaurants:
    dn = Dinner(d['name'],d['rating'],d['delivery_time'],d['price'])
    dinners.append(dn)

result = sorted(
    dinners,
    key=lambda x:x.score(weight),
    reverse = True
)
for rank,d in enumerate(result,1):
    print(rank,d.name,round(d.score(weight),2))

