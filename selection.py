import datetime

available_rooms = ['1204', '1206', '1212', '1218', '1224', '1226', '1231', '1232', '1237', '1238', '1239', '1244', '1246',
                    '1314', '1316', '1321', '1322', '1323', '1325', '1328', '1334', '1336', '1342', '1348', '1352', '1354', '1356',
                    '1358', '1381', '1382', '1383', '1384', '1387', '1392', '1398', '2101', '2104', '2106', '2107', '2108', '2109',
                    '2239', '2240', '3101', '3104', '3105', '3106', '3107']

week_from_today = datetime.date.today() + datetime.timedelta(days=7)

print("You are booking a room on " + str(week_from_today))
room_number = (input("Which room number are you interested in?\n"))

if room_number not in available_rooms:
    while room_number not in available_rooms:
        room_number = (input("Invalid room number, pick again: "))

times_available = []

for i in range(7,12):
    times_available.append(str(i) + ":00am")
    times_available.append(str(i) + ":30am")

times_available.append("12:00pm")
times_available.append("12:30pm")

for i in range(1,7):
    times_available.append(str(i) + ":00pm")
    times_available.append(str(i) + ":30pm")

print(times_available)

times_requested = []

ask_time = input("Input 4 time slots on one line (Ex. 8:00am 6:30pm 12:00pm 7:30am)\n")
print(ask_time)

times_requested = ask_time.split()
print(times_requested)
