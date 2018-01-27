import sys

sys.path.insert(0, "nus_studyrooms")
import datetime
import fetch
import booking_parser


# importlib.import_module(fetch)
# importlib.import_module(booking_parser)
def openByBuilding(fac):
    if "FASS" in fac:
        return {'AS1': ['AS1-0201', 'AS1-0301', 'AS1-0208', 'AS1-0304', 'AS1-0303', 'AS1-0205', 'AS1-0209', 'AS1-0204',
                        'AS1-0203', 'AS1-0302', 'AS1-0213', 'AS1-0210', 'AS1-0207', 'AS1-0548', 'AS1-0524', 'AS1-0401',
                        'AS1-0212'],
                'AS2': ['AS2-0413', 'AS2-0311', 'AS2-0509', 'AS2-0510', 'AS2-0312', 'AS2-0203', 'AS2-0313', 'AS2-0204',
                        'AS2-0302', 'AS2-0316', 'AS2-0201'],
                'AS3': ['AS3-0303', 'AS3-0307', 'AS3-0305', 'AS3-0207', 'AS3-0208', 'AS3-0209', 'AS3-0302', 'AS3-0214',
                        'AS3-0304', 'AS3-0308', 'AS3-0306', 'AS3-0215', 'AS3-0212', 'AS3-0309', 'AS3-0312', 'AS3-0314',
                        'AS3-0316', 'AS3-0523', 'AS3-0101', 'AS3-0213'],
                'AS4': ['AS4-0206', 'AS4-0109', 'AS4-0119', 'AS4-0603', 'AS4-0604', 'AS4-0110', 'AS4-0602', 'AS4-0118',
                        'AS4-0117', 'AS4-0116', 'AS4-B107', 'AS4-0601', 'AS4-0114', 'AS4-0115', 'AS4-0335', 'AS4-0208',
                        'AS4-B110', 'AS4-B109'], 'AS5': ['AS5-0309', 'AS5-0205', 'AS5-0202', 'AS5-0203'],
                'AS6': ['AS6-0212', 'AS6-0208', 'AS6-0421', 'AS6-0426', 'AS6-0214', 'AS6-0338', 'AS6-0215B', 'AS6-0333',
                        'AS6-0204'],
                'AS7': ['AS7-0214', 'AS7-0106', 'AS7-0101', 'AS7-0119', 'AS7-0102', 'AS7-0201A', 'AS7-0201'],
                'AS8': ['AS8-0402', 'AS8-0646', 'AS8-0401', 'AS8-0405', 'AS8-0647']};
    elif "SOC" in fac:
        return {'COM1': ['COM1-0212', 'COM1-0204', 'COM1-0203', 'COM1-0201', 'COM1-0209', 'COM1-0217', 'COM1-0113',
                         'COM1-0114', 'COM1-B108', 'COM1-B111', 'COM1-B110', 'COM1-0207', 'COM1-0208', 'COM1-B109',
                         'COM1-0120', 'COM1-0218', 'COM1-B112', 'COM1-0210', 'COM1-0216', 'COM1-B103', 'COM1-B113',
                         'COM1-B102', 'COM1-0206'],
                'COM2': ['COM2-0108'],
                'I3': ['i3-0339', 'i3-0344', 'i3-0336', 'i3-0338', 'i3-Aud', 'i3-0337']};

    elif "BIZ" in fac:
        return {'BIZ1': ['BIZ1-0301', 'BIZ1-0205', 'BIZ1-0304', 'BIZ1-0201', 'BIZ1-0202', 'BIZ1-0206', 'BIZ1-0204',
                         'BIZ1-0303', 'BIZ1-SR6-4', 'BIZ1-SR6-1', 'BIZ1-0302', 'BIZ1-0307', 'BIZ1-0203', 'BIZ1-0305',
                         'BIZ1-CMRI'],
                'BIZ2': ['BIZ2-0301', 'BIZ2-0404', 'BIZ2-0509', 'BIZ2-0510', 'BIZ2-0202', 'BIZ2-0413B', 'BIZ2-0413C',
                         'BIZ2-0201', 'BIZ2-0413A', 'BIZ2-B104', 'BIZ2-0420', 'BIZ2-0228', 'BIZ2-0227', 'BIZ2-0229',
                         'BIZ2-0302', 'BIZ2-0303', 'BIZ2-0117', 'BIZ2-0112', 'BIZ2-0114', 'BIZ2-0115', 'BIZ2-0118',
                         'BIZ2-0224']};
    elif "SDE" in fac:
        return {'SDE': ['SDE-427', 'SDE-SR15', 'SDE-SR10', 'SDE-SR13', 'SDE-424', 'SDE-423', 'SDE-DV3', 'SDE-SR11',
                        'SDE-ER5', 'SDE-SR9', 'SDE-SR12', 'SDE-426', 'SDE-SR14', 'SDE-422', 'SDE-DV1', 'SDE-425',
                        'SDE-421', 'SDE-MEZZ', 'SDE-ES1', 'SDE-DDL2-2', 'SDE-ES2', 'SDE-ER4', 'SDE-DV2', 'SDE-ER1',
                        'SDE-ISD-1', 'SDE-IDS1', 'SDE-IDS2', 'SDE-ISD-2']};
    elif "FOS" in fac:
        return {'S1': ['S1-03CR'],
                'S1A': ['S1A-0217'],
                'S2': ['S2-0414', 'S2-0415'],
                'S3': ['S3-05CR'],
                'S4': ['S4-02Lab'],
                "S4A": ['S4A-03-10', 'S4A-03-11', 'S4A-0308'],
                "S5": ['S5-0224', 'S5-01GEN', 'S5-0223', 'S5-0410', 'S5-01PHY'],
                'S8': ['S8-0403', 'S8-0203', 'S8-0314'],
                'S11': ['S11-0301', 'S11-0204', 'S11-0302', 'S11-0401'],
                'S12': ['S12-0401', 'S12-0402', 'S12-0403'],
                'S13': ['S13-M-09', 'S13-M-08'],
                'S14': ['S14-0620', 'S14-0619', 'S14-04Lab'],
                'S16': ['S16-0437', 'S16-03ALR', 'S16-0307', 'S16-0430', 'S16-0436', 'S16-0435', 'S16-0598', 'S16-0440',
                        'S16-0304', 'S16-0309', 'S16-0431', 'S16-05102', 'S16-05101', 'S16-06118'],
                'S17': ['S17-0404', 'S17-0611', 'S17-0512', 'S17-0302', 'S17-0304', 'S17-0405', 'S17-0406',
                        'S17-0511']};
    elif "FOE" in fac:
        return {'E1': ['E1-06-01', 'E1-06-04', 'E1-06-06', 'E1-06-09', 'E1-06-03', 'E1-06-08', 'E1-06-07', 'E1-06-02',
                       'E1-06-16', 'E1-06-05', 'E1-06-10', 'E1-06-12', 'E1-06-11', 'E1-06-15', 'E1-06-13', 'E1-06-14',
                       'E1A-05-19', 'E1-04-10PC'],
                'E2': ['E2-03-02', 'E2-03-03', 'E2-0307PC4', 'E2-0306PC3', 'E2-03-32'],
                'E2A': ['E2A-02-02', 'E2A-03-01', 'E2A-03-02', 'E2A-04-02', 'E2A-04-03'],
                'E3': ['E3-06-04', 'E3-06-03', 'E3-06-15', 'E3-06-07', 'E3-06-09', 'E3-06-08', 'E3-06-01', 'E3-06-06',
                       'E3-06-11', 'E3-06-10', 'E3-06-05', 'E3-06-12', 'E3-06-13', 'E3-06-14', 'E3-06-02',
                       'E3-0519ESP'],
                'E3A': ['E3A-0504'],
                'E4': ['E4-04-02', 'E4-04-04', 'E4-04-03', 'E4-02-01'],
                'E4A': ['E4A-06-03'],
                'E5': ['E5-02-32', 'E5-03-19', 'E5-03-22', 'E5-03-21', 'E5-03-20', 'E5-03-23'],
                'EA': ['EA-06-04', 'EA-06-02', 'EA-02-11', 'EA-06-07', 'EA-06-03', 'EA-06-05', 'EA-06-06']};
    elif "ERC" in fac:
        return {'ERC': ['ERC-GLR', 'ERC-SR8', 'ERC-SR9CAM', 'ERC-SR11', 'ERC-SR10', 'ERC-SR3', 'ERC-ALR', 'ERC-SR4', 'ERC-SR5']};
    elif "UTSRC" in fac:
        return {'UTSRC': ['UTSRC-DA2', 'UTSRC-LT50', 'UTSRC-SR8', 'UTSRC-LT52', 'UTSRC-LT53', 'UTSRC-SR5', 'UTSRC-SR2', 'UTSRC-SR1', 'UTSRC-SR9', 'UTSRC-SR6', 'UTSRC-GLR', 'UTSRC-LT51', 'UTSRC-SR3', 'UTSRC-SR7', 'UTSRC-SR4']};
    return None;


def getAvailability(fac, buildingName):
    now = datetime.datetime.now()
    availability = dict()

    facBuilding = openByBuilding(fac)
    buildingRooms = facBuilding[buildingName]
    buildingBookings = booking_parser.getBooking()

    for room in buildingRooms:
        availability[room] = checkAvailable(buildingBookings, room)
    print(availability)


def getAvailability(fac , buildingName):
	now = datetime.datetime.now()
	availability = dict()
	
	facBuilding = openByBuilding(fac)
	buildingRooms = facBuilding[buildingName]
	
	
	for room in buildingRooms:
		availability[room] = fetch.findRoomState(room,"1300")
		
	if "COM" in buildingName or "AS6" in buildingName or "i3" in buildingName:
		buildingBookings =  booking_parser.getBooking(buildingName)
		for room in buildingBookings[buildingName]:
			availability[room] = checkBooking(room, buildingBookings[buildingName][room])
	print(availability)
	

def checkBooking(room,bookings):
	now = datetime.datetime.now()
	for event in bookings:
		if int(event[0])<=1300 and int(event[1])>1300:
			return "occupied"
	return "vacant"
		

#getAvailability("SOC", "COM1")
