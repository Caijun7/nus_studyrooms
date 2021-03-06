# import urllib2 #change to python3
import json
import datetime

# jsonData =  urllib2.urlopen("https://nusmods.com/api/2017-2018/2/venueInformation.json").read()
# venueInfo = json.loads(jsonData)
venueInfo = json.load(open('venueinformation.json'))


# print(venueInfo)

def findRoom(room):
    if room in venueInfo:
        return venueInfo[room]
    else:
        print("Invalid room")
        return "Invalid room"


def findDay(weekday, rooms):
    # check if it is sunday
    if weekday == 6:
        day = rooms[0]
        availability = day["Availability"]
        return availability
    day = rooms[weekday]
    availability = day["Availability"]
    return availability


def findTiming(timing, availability):
    if timing in availability:
        return availability[timing]
    else:
        print("Invalid timing")
        return "Invalid timing"


def findRoomState(roomInput, timing):
    room = findRoom(roomInput)
    now = datetime.datetime.now()
    availability = findDay(now.weekday(), room)

    roomState = findTiming(timing, availability)
    while int(timing) < 2330:
        timing = int(timing) + 30
        if timing % 100 == 60:
            timing = timing - 60 + 100
        if roomState != findTiming(str(timing), availability):
            break
    return str(roomState + ' until ' + str(timing))

# print(findRoomState("COM1-0203", "1300"))

