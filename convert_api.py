import requests
from consts import api_key

coins_dict = {
    # region ILS/NIS
    "שקל": "ILS",
    # "שקל חדש": "ILS",
    # "שקלים": "ILS",
    # "שקלים חדשים": "ILS",
    "שח": "ILS",
    'ש"ח': "ILS",
    # endregion

    # region USD
    "דולר": "USD",
    # "דולרים": "USD",
    "ירוקים": "USD",
    # endregion

    # region EUR
    "אירו": "EUR",
    "יורו": "EUR",
    # endregion

    # region GBP
    "לירה שטרלינג": "GBP",
    "לירה סטרלינג": "GBP",
    "לירות שטרלינג": "GBP",
    "לירות סטרלינג": "GBP",
    'ליש"ט': "GBP",
    "פאונד": "GBP",
    "פאונדים": "GBP"
    # endregion
}


def get_coins_list():
    return list(coins_dict.keys())


def create_url(currency_from, currency_to="ILS"):
    return f"https://free.currconv.com/api/v7/convert?q={currency_from}_{currency_to}&compact=ultra&apiKey={api_key}"


def get_rate(processed_url):
    return list(requests.get(processed_url).json().values())[0]


def make_exchange(num, currency_from, currency_to="ILS"):
    return round(get_rate(create_url(currency_from, currency_to)) * num, 3)
