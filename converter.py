def hotel(raw_dict: dict) -> tuple:
    for e in raw_dict:
        yield (
            e['id'],
            e['name'],
            e['resort'],
            e['country'],
            e['rating'],
            e['distances']['airport'],
            e['distances']['beach'],
            e['isNearToBeach'],
            e['beachLine'],
            e['beachOwner'],
            e['isPopular'],
            e['hasChildrenAttributes']
        )


def offer(raw_dict: dict) -> tuple:
    for e in raw_dict:
        e = e['tour']
        yield (
            e['identity'],
            e['price'],
            e['oilTax'],
            e['originalPrice'],
            e['nights'],
            e['touristGroup']['adults'],
            e['meal'],
            e['checkInDate'],
            e['hotel'],
            e['operator']['id'],
            e['room']['name'],
            e['hotelAvailable'],
            e['isLessTicketsQty'],
            e['sortRate']
        )
