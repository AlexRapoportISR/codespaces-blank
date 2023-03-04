import requests


class CurrencyPrice:

    @staticmethod
    def get_price(base, quote, amount):
        rates_class = Rates()
        rates = rates_class.get_rates()
        if base in rates and quote in rates.keys():
            base_rate = rates[base]
            quote_rate = rates[quote]
            return base_rate/quote_rate*amount


class Rates:

    @staticmethod
    def get_rates():
        # API отдает JSON!!!
        url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=20230303&json'  # 'https://api.monobank.ua/bank/currency'
        res = requests.get(url)
        result = res.json()
        rates = {}
        for entry in result:
            if entry['r030'] in [840, 978, 826, 643]:
                rates[entry['cc']] = entry['rate']
        return rates