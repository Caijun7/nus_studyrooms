import urllib2 #change to python3 
import datetime


def extractInfo(url):
	
	page = urllib2.urlopen(url).read()
	page = page[page.find("Booking Schedule"):page.find("thedate")]
	palce = page.split("<td>")
	palce= palce[1:]
	palce = list(map(lambda string : string[:string.find("</td>")],palce))
	tem, tem2 = palce[::2],palce[1::2]
	
	tem3 =list(map(lambda string : to24H(string),tem))
	tem4 =[]
	for x in tem3:
		if(x is None): 
			break
		tem4.append(x[0])
		tem4.append(x[1])
	tem, tem3 = tem4[::2],tem4[1::2]
	tupleList = zip(tem,tem3,tem2)
	return tupleList

def to24H(timeString):
	if "No" in timeString: 
		return None
	time = timeString.split(" - ")
	result = []
	for x in time:
		print(x)
		if x[1] != ':':
			hours = int(x[:2])
		else:
			hours = int(x[0])
			
		if "pm" in x and hours != 12:
			result.append(str((hours+12)*100))
		elif hours == 12 and "am" in x: 
			result.append(str(0000))
		else:
			result.append(str(hours*100))
	return result
	
def printf(list):
	for room in list:
		print(room)
		print(list[room])
		print("\n")
		
def getBooking(buildingName):
	rooms = ["DR1","DR2","DR3","DR4","DR6","DR7","DR8","DR9","DR10","DR11","DR12","ExecutiveClassRm","MR1","MR2","MR3","MR4","MR5","MR6","MR7","VideoConf"]
	now = datetime.datetime.now()

#urllib2.urlopen("https://mysoc.nus.edu.sg/~calendar/getBooking.cgi?room=DR2&thedate=2018/01/30").read()
#print(extractInfo("https://mysoc.nus.edu.sg/~calendar/getBooking.cgi?room="+rooms[0]+"&thedate=2018/01/30"))
	schedule = dict()
	buildingSchedule = { 
		'COM1': dict(),
		'COM2': dict(),
		'I-CUBE': dict(),
		'AS6': dict(),
	}
	#print(buildingSchedule)
	for room in rooms:
		print(room)
		if buildingName == "COM1" and rooms.index(room)<4 or rooms.index(room) == 10 or (rooms.index(room)>12 and rooms.index(room)<17 and rooms.index(room) != 14) or rooms.index(room)> len(rooms)-2:
			schedule = {room:extractInfo("https://mysoc.nus.edu.sg/~calendar/getBooking.cgi?room="+room+"&thedate="+str(now.year)+"/"+"2"+"/"+"2")}
			buildingSchedule["COM1"].update(schedule.items())
		elif buildingName == "COM2" and (rooms.index(room)>3 and rooms.index(room)<10) or rooms.index(room) == 11 or rooms.index(room) == 14:  
			schedule = {room:extractInfo("https://mysoc.nus.edu.sg/~calendar/getBooking.cgi?room="+room+"&thedate="+str(now.year)+"/"+"2"+"/"+"2")}
			buildingSchedule["COM2"].update(schedule.items())
		elif buildingName == "AS6" and rooms.index(room) == 17 :
			schedule = {room:extractInfo("https://mysoc.nus.edu.sg/~calendar/getBooking.cgi?room="+room+"&thedate="+str(now.year)+"/"+"2"+"/"+"2")}
			buildingSchedule["AS6"].update(schedule.items())
		elif buildingName == "i3" and rooms.index(room)>17 and rooms.index(room)<21:
			schedule = {room:extractInfo("https://mysoc.nus.edu.sg/~calendar/getBooking.cgi?room="+room+"&thedate="+str(now.year)+"/"+"2"+"/"+"2")}
			buildingSchedule["I-CUBE"].update(schedule.items())
		#printf(buildingSchedule)
	return buildingSchedule
	#schedule[room] = extractInfo("https://mysoc.nus.edu.sg/~calendar/getBooking.cgi?room="+room+"&thedate="+str(now.year)+"/"+str(now.month)+"/"+str(now.day))
	#for room in schedule:
	#	print(room);print(schedule[room])
#list = getBooking()
#print(list["COM1"]["MR1"])