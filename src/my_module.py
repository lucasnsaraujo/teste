
def get_cheapest_hotel(number):   #DO NOT change the function's name

    weekdays = ['mon', 'tues', 'wed', 'thur', 'fri']
    weekends = ['sat', 'sun']

    client_type = number.split(':')[0]
    dates = number.split(':')[1].split(',')
    for index, date in enumerate(dates):
        date = date.split('(')[1].split(')')[0]
        dates[index] = date
    

    lakewood = {
        'rating': 3,
        'price': {
            'weekdays': {
                'Regular': 110,
                'Rewards': 80
            },
            'weekends': {
                'Regular': 90,
                'Rewards': 80
            }
        }
    }
    
    bridgewood = {
        'rating': 4,
        'price': {
            'weekdays': {
                'Regular': 160,
                'Rewards': 110
            },
            'weekends': {
                'Regular': 60,
                'Rewards': 50
            }
        }
    }

    ridgewood = {
        'rating': 5,
        'price': {
            'weekdays': {
                'Regular': 220,
                'Rewards': 100
            },
            'weekends': {
                'Regular': 150,
                'Rewards': 40
            }
        }
    }


    price_bridgewood = {'name': 'Bridgewood', 'value': 0, 'rating': 4}
    price_ridgewood = {'name': 'Ridgewood', 'value': 0, 'rating': 5}
    price_lakewood = {'name': 'Lakewood', 'value': 0, 'rating': 3}

    
    for day in dates:
        if day in weekdays:
            price_bridgewood['value'] += bridgewood['price']['weekdays'][client_type]
            price_ridgewood['value'] += ridgewood['price']['weekdays'][client_type]
            price_lakewood['value'] += lakewood['price']['weekdays'][client_type]
        elif day in weekends:
            price_bridgewood['value'] += bridgewood['price']['weekends'][client_type]
            price_ridgewood['value'] += ridgewood['price']['weekends'][client_type]
            price_lakewood['value'] += lakewood['price']['weekends'][client_type]
        else:
            pass
    
    prices = [price_bridgewood['value'], price_ridgewood['value'], price_lakewood['value']]

    hotels = [price_bridgewood, price_ridgewood , price_lakewood]

    cheapest = min(prices)
    cheapest_hotel_arr = []

    for item in hotels:
        if cheapest == item['value']:
            cheapest_hotel_arr.append(item)
    
    cheapest_hotel = cheapest_hotel_arr[0]['name']
    
    if len(cheapest_hotel_arr) > 1:
        cheap = 0
        for hotel in cheapest_hotel_arr:
            if hotel['rating'] > cheap:
                cheapest_hotel = hotel['name']
                cheap = hotel['rating']
    
    return cheapest_hotel
    