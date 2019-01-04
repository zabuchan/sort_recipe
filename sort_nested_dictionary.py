import json

filename = "room_price.json"

with open(filename, 'r') as fin:
	offices = json.load(fin)

rooms = offices['office']
# for room in rooms:
# 	print(room.get('price'))

sorted_rooms = sorted(rooms, key=lambda x: x.get('price'), reverse=True)
print(sorted_rooms)
