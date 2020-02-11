import requests
variants = [
    {
        'departureCity': 2,
        'countries[]': 87,
        'checkInDateRange[from]': '2020-02-13',
        'checkInDateRange[to]': '2020-02-19',
        'nightRange[from]': 6,
        'nightRange[to]': 15,
        'touristGroup[adults]': 2,
        'touristGroup[kids]': 0,
        'touristGroup[infants]': 0,
        'meals[]': 2,
        'limit': 100,
    }
]
COMMON_URL = "https://inventory-app.travelata.ru/tourProduct/search"


def _read_cookies() -> dict:
    with open("./cookies.txt", encoding='utf-8', newline="\n") as f:
        return {cookie.split(" ", 2)[0]: cookie.split(" ", 2)[1].replace('\n', '') for cookie in f}


def make() -> dict:
    headers = {
        "Accept": "*/*",
        "Authorization": "simple eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjM3NDMxOTA5LWQ3OWQtNGUwMy04OGRjLWE3"
                         "ODRkYzZjMDE5YyIsImlzUmVnaXN0ZXJlZCI6ZmFsc2V9.MbZKw7_e6ZZiUdzPTPohzWahEnIZQAfvkxPZGoTs4j4",
        # "ApplicationID": "7B8669C8-E0CF-4F4E-AE15-70A1B0606D9F",
        # "User-Agent": "CIAN/1.84 (iPhone; iOS 12.2; Scale/3.00; 7B8669C8-E0CF-4F4E-AE15-70A1B0606D9F)",
    }
    cookies = _read_cookies()

    # url = url.format(deal_type, offer_type, page_number, bs_center_id)
    r = requests.get(COMMON_URL, variants[0], headers=headers, cookies=cookies)
    return r.json()
