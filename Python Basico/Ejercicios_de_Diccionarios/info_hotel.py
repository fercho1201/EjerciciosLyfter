hotel_diccionatory = {
    "name": "Hotel California",
    "location": "Los Angeles",
    "rooms": {
        'room 101': {'floor': 'first', 'price': 100},
        'room 201': {'floor': 'second', 'price': 150},  
        'room 301': {'floor': 'third', 'price': 300},
        'room 401': {'floor': 'fourth', 'price': 100},
    } ,
    "rating": 4.5,
}

for room, details in hotel_diccionatory["rooms"].items():
    print(f"{room} is located on the {details['floor']} floor and costs ${details['price']} per night.")