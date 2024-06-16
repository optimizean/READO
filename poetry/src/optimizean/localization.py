import time
import requests
import warnings

warnings.filterwarnings(action="ignore")


def greetings():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    current_hour = int(current_time.split(" ")[-1].split(":")[0])

    if 6 <= current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 18:
        return "afternoon"
    elif 18 <= current_hour < 22:
        return "evening"
    elif 22 <= current_hour or current_hour < 6:
        return "night"
    else:
        raise ValueError("Wrong Time")


def get_location():
    response = requests.get("http://ip-api.com/json/")
    data = response.json()
    return data.get("country"), data.get("countryCode")


def get_local_greeting(greeting, country_code):
    greetings_dict = {
        "morning": {
            "AR": "صباح الخير",
            "DE": "Guten Morgen",
            "ES": "Buenos días",
            "FR": "Bonjour",
            "HI": "सुप्रभात",
            "IT": "Buongiorno",
            "JA": "おはようございます",
            "KR": "좋은 아침",
            "PT": "Bom dia",
            "RU": "Доброе утро",
            "US": "Good morning",
            "ZH": "早上好",
        },
        "afternoon": {
            "AR": "مساء الخير",
            "DE": "Guten Tag",
            "ES": "Buenas tardes",
            "FR": "Bon après-midi",
            "HI": "नमस्ते",
            "IT": "Buon pomeriggio",
            "JA": "こんにちは",
            "KR": "좋은 점심",
            "PT": "Boa tarde",
            "RU": "Добрый день",
            "US": "Good afternoon",
            "ZH": "下午好",
        },
        "evening": {
            "AR": "مساء الخير",
            "DE": "Guten Abend",
            "ES": "Buenas noches",
            "FR": "Bonsoir",
            "HI": "शुभ संध्या",
            "IT": "Buona sera",
            "JA": "こんばんは",
            "KR": "좋은 저녁",
            "PT": "Boa noite",
            "RU": "Добрый вечер",
            "US": "Good evening",
            "ZH": "晚上好",
        },
        "night": {
            "AR": "تصبح على خير",
            "DE": "Gute Nacht",
            "ES": "Buenas noches",
            "FR": "Bonne nuit",
            "HI": "शुभ रात्रि",
            "IT": "Buona notte",
            "JA": "おやすみなさい",
            "KR": "좋은 밤",
            "PT": "Boa noite",
            "RU": "Спокойной ночи",
            "US": "Good night",
            "ZH": "晚安",
        },
    }

    local_greeting = greetings_dict.get(greeting, {}).get(country_code, "Hello")

    return local_greeting


if __name__ == "__main__":
    greeting = greetings()
    country, country_code = get_location()
    local_greeting = get_local_greeting(greeting, country_code)

    print(local_greeting)
