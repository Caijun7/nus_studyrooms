import urllib.request
import json
import datetime
import numpy as np

jsonData = urllib.request.urlopen("https://nusmods.com/api/2017-2018/2/venueInformation.json").read()
venueInfo = json.loads(jsonData)
# venueInfo = np.array(jsonToPython)

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
        return None
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
    return roomState

def findRoomActivity(roomInput, timing):


print(main("COM1-0201", "1300"))

