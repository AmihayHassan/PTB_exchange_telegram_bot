import re
import convert_api


def find_num(s):
    all_nums = re.findall(r"[-+]?\d*\.\d+|\d+", str(s))
    if len(all_nums) == 1:
        return float(all_nums[0])
    else:
        return


def find_coins_in_order(s):
    ans = []
    for word in s.split():
        tested = [ele for ele in convert_api.get_coins_list() if (ele in word)]
        if len(tested) == 1:
            ans.append(convert_api.coins_dict[tested[0]])
    return ans


def reply(s):
    coins = find_coins_in_order(s)
    num = 1 if find_num(s) is None else find_num(s)
    if len(coins) == 0:
        return
    elif len(coins) == 1:
        return convert_api.make_exchange(num, coins[0])
    elif len(coins) == 2:
        return convert_api.make_exchange(num, coins[0], coins[1])
    else:
        return
