import time
from datetime import date

from models.tour import Tour




# from models.historyPrice import HistoryPrice
# from models.historyPromo import HistoryPromo
# from models.mcityOffer import McityOffer
# from models.Offer import Offer
# from models.phone import Phone
# from models.user import User
# from userConverter import userConvert
#
import variants
# from db import session
from req import make as make_request
# from converter import convert
# from models.bc import Bc
# from models.house import House
# from models.location import Location
# from models.newbuilding import Newbuilding
# import csv
#
# with open('temp/locations.tsv') as tsvfile:
#     reader = csv.reader(tsvfile, delimiter='\t')
#     for row in reader:
#         params = tuple(row)
#         session.merge(Location(*params))
#
# with open('temp/newbuildings.tsv') as tsvfile:
#     reader = csv.reader(tsvfile, delimiter='\t')
#     for row in reader:
#         params = tuple(row)
#         session.merge(Newbuilding(*params))
#
# with open('temp/houses.tsv') as tsvfile:
#     reader = csv.reader(tsvfile, delimiter='\t')
#     for row in reader:
#         params = tuple(row)
#         session.merge(House(*params))
#
# with open('temp/bc.tsv') as tsvfile:
#     reader = csv.reader(tsvfile, delimiter='\t')
#     for row in reader:
#         if row[3]:
#             if not session.query(Bc).get(row[3]):
#                 continue
#         params = tuple(row)
#         session.merge(Bc(*params))
# session.commit()
from req import make as make_request


def process():
    while True:
        result = make_request()['result']

        if 'error' in result:
            exit()

        tour: list = result['tourProducts']
        hotels: list = result['hotels']
        scanned: list = result['scannedTours']

        for e in userConvert(data['all_agents']):
            session.merge(User(*e))
            for phone in e[-1]:
                session.merge(Phone(e[0], phone))

        mc_count = 0
        ok = True

        for e in convert(res):
            if e['offer'][9] not in ['dailyFlat', 'warehouse']:
                offer: Offer = session.query(Offer).get(e['offer'][0])
                userId = e['offer'][1]
                if not session.query(User).get(userId):
                    print('no user {}'.format(userId))
                    session.merge(User(userId, 'Anonimus', date.today().isoformat(), None, None, None, None, 5, None))

                session.merge(Offer(*e['offer']))

                stats_exists = offer and offer.stats and offer.stats[-1].date == date.today()
                if e['statsDaily'][1] is None or e['statsDaily'][1] is None:
                    print(offer_type, deal_type, current_page, 'Stats None')
                    ok = False
                    time.sleep(3)
                    break
                if not stats_exists:
                    session.merge(StatsDaily(*e['statsDaily']))
                elif stats_exists and (offer.stats[-1].stats_daily is None or offer.stats[-1].stats_daily <
                                       e['statsDaily'][2]):  # and e['statsDaily'][2] is not None
                    session.query(StatsDaily) \
                        .filter_by(id=e['statsDaily'][0], date=date.today()) \
                        .update({"stats_total": e['statsDaily'][1], "stats_daily": e['statsDaily'][2]})

                if e['offer'][1] == 9383110:
                    mc_count += 1
                    session.merge(McityOffer(*e['mcityOffer']))

                hp = e['historyPromo']
                if offer and not offer.promos:
                    print("Obj {} hasn't prices?".format(offer.id))
                if not (offer and offer.promos and offer.promos[-1].services == hp[1]):
                    session.add(HistoryPromo(*hp))

                if e['historyPrice'] is None:
                    print(offer_type, deal_type, current_page, 'Price None')
                    continue
                for p in e['historyPrice']:
                    h = HistoryPrice(*p)
                    c = session.query(HistoryPrice).filter_by(id=h.id, time=h.time).count()
                    if not c:
                        session.merge(h)

        if ok:
            session.commit()
            current_page += 1
            delay = randint(3, 10)
            length = res.__len__()
            print("{0} {1} {2} (inc {3} mcity) received.\nWaiting {4} seconds..".format(
                length, deal_type, offer_type, mc_count, delay
            ))
            time.sleep(delay)
            if length < 50:
                break  # Объявлений больше нет -> съёбки


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
