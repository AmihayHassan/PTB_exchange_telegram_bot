# this module is a temporary patch module
# to solve the problem of getting blocked by the API

# need to check if it can be used as a permanent solution


import requests
from messages_parser import *
from convert_api import coins_dict
from messages_parser import reply


def create_url(currency_from, currency_to):
    return f"https://www.google.com/search?q={currency_from}+to+{currency_to}"


def get_rate(processed_url):
    return float(requests.get(processed_url).text.split(" = ")[1][:6])


def make_exchange(num, currency_from, currency_to="ILS"):
    return round(get_rate(create_url(currency_from, currency_to)) * num, 3)


def google_reply(s):
    coins = find_coins_in_order(s)
    num = 1 if find_num(s) is None else find_num(s)
    if len(coins) == 0:
        return
    elif len(coins) == 1:
        return make_exchange(num, coins[0])
    elif len(coins) == 2:
        return make_exchange(num, coins[0], coins[1])
    else:
        return
