import requests

# Функція для отримання актуальних курсів валют з НБУ
def info():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Не вдалося отримати курси валют. Спробуйте пізніше.")
        return None
    
    data = response.json()
    
    # Створюємо словник з курсами валют
    exchange_rates = {}
    for item in data:
        if item['cc'] in ['USD', 'EUR', 'PLN']:  # Тільки для цих валют
            exchange_rates[item['cc']] = item['rate']
    
    return exchange_rates

# Функція для конвертації валюти в гривні
def convert_currency(amount, currency, exchange_rates):
    if currency not in exchange_rates:
        print(f"Курс для валюти {currency} не знайдений.")
        return None
    
    rate = exchange_rates[currency]
    return amount * rate

# Головна функція програми
def main():
    # Отримуємо курси валют
    exchange_rates = info()
    if not exchange_rates:
        return
    
    print("Доступні валюти для конвертації: EUR, USD, PLN.")
    currency = input("Введіть валюту, яку хочете конвертувати (EUR, USD, PLN): \n").upper()
    
    if currency not in ['EUR', 'USD', 'PLN']:
        print("Невірна валюта. Доступні лише EUR, USD, PLN.")
        return
    
    try:
        amount = float(input("Введіть кількість валютних одиниць: "))
    except ValueError:
        print("Некоректне введення кількості.")
        return
    
    # Конвертуємо валюту в гривні
    result = convert_currency(amount, currency, exchange_rates)
    
    if result is not None:
        print(f"{amount} {currency} дорівнює {result:.2f} гривень.")
    
