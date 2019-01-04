import json
from operator import itemgetter

filename = "room_price.json"

with open(filename, 'r') as fin:
	offices = json.load(fin)

room_list = offices['office']
rooms_by_price = sorted(room_list, key=itemgetter('price'))
rooms_by_room_number = sorted(room_list, key=itemgetter('room-number'))


print("Sorted by price:\n{}".format(rooms_by_price))
print("Sorted by room-number:\n{}".format(rooms_by_room_number))
