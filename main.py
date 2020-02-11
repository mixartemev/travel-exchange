# import time
# from datetime import date

from req import make as make_request

from models.tour import Tour
from models.hotel import Hotel

from db import session
import converter


def process():
    result = make_request()['result']

    if 'error' in result:
        exit()

    # scanned: list = result['scannedTours']

    for e in converter.hotel(result['hotels']):
        session.merge(Hotel(*e))
    session.commit()

    for e in converter.offer(result['tourProducts']):
        session.merge(Tour(*e))
    session.commit()


def main():
    try:
        process()
    except Exception as e:
        print(e)
        # print("Unknown exception.. Push: {}".format(push(False)))
        exit()
    except KeyboardInterrupt:
        print("Finishing...")
        exit()
    # print("Done. Push: {}".format(push()))


# def push(ok=True):
#     url = 'https://fcm.googleapis.com/fcm/send'
#     title = 'Парсер отработал'
#     mess = 'Данные успешно спизджены полностью' if ok else 'Пизда рулю. Все сломалось'
#     act = 'https://docs.google.com/spreadsheets/d/1lPFc1p_5TNSxYOtJ4hSqcSMAiUig4slRQTdMmgJroic/edit#gid=656058326'
#     tok = 'cDBL0-jYBWQ:APA91bG294ZcB0TkztsUkt-hBayeC6kPnYBzY6swFSEgNtJGdB5ht1xm-Kq_7VokWMLH35ecV9SbR0PMm7qrxmXtTO' \
#           '8tPkNUJ09F1j2m0B923BYrh8mOzQGubb3xdNHR249mvwrWM-fb'
#     body = {
#       "notification": {
#         "title": title,
#         "body": mess + ' ' + date.today().isoformat(),
#         "icon": "https://avatars1.githubusercontent.com/u/5181924?s=460&v=4",
#         "topic": "excel",
#         "click_action": act
#       },
#       "to": tok
#     }
#     headers = {
#         "Authorization": "key=AAAAdDA0FEM:APA91bGovsJXVAm0R3P5DNBZsWbvwbXacLmjvlDst2t3o8VNWUhJ63UUgNeZfcTZXuWQw9L"
#                          "WPHGJt5dn20hDBEDt-cjmw91i_ncfg9qE5eqifRNULeEbMPQgMRUpLw4yZrUCyeluO2TZ",
#         "Content-Type": "application/json"
#     }
#     return requests.post(url, json=body, headers=headers).status_code


if __name__ == '__main__':
    main()
