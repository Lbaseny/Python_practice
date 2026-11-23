"""场景：
开发一个外卖平台配送费计算系统。"""
# 规则：
# 首先判断配送距离：
# - 3 公里以内：
#   - 普通天气：配送费 3 元。
#   - 恶劣天气：配送费 6 元。
# - 3～5 公里：
#   - 普通天气：配送费 5 元。
#   - 恶劣天气：配送费 9 元。
# - 超过 5 公里：
#   - 如果是会员，配送费 8 元。
#   - 如果不是会员，配送费 12 元。
# 额外规则：
# - 订单金额满 50 元，免配送费。
# - 但恶劣天气不参与免配送费活动。

def main(distance,weather,is_member,order_amount):
    if weather == '恶劣':
        if distance < 3:
            print('配送费 6 元')
        elif 3 <= distance <= 5:
          print('配送费 9 元')
        elif distance > 5:
            if is_member:
                print('配送费 8 元')
            else:
                print('配送费 12 元')
    elif weather == '普通':
        if order_amount < 50:
            if distance < 3:
                print('配送费 3 元')
            elif 3 <= distance <= 5:
                print('配送费 5 元')
            elif distance > 5:
                if is_member:
                    print('配送费 8 元')
                else:
                    print('配送费 12 元')
        else :
            print('免配送费')


main(4,'普通',True,60)
main(7,'恶劣',True,50)




