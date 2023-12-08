import json, unittest, datetime,time

# with open(r"D:\deloitte\Newfolder\data-1.json","r",encoding="utf8") as f:
#     jsonData1 = json.load(f)
with open(r"D:\deloitte\Newfolder\data-2.json","r",encoding="utf8") as f:
    jsonData2 = json.load(f)
# with open(r"D:\deloitte\Newfolder\data-result.json","r",encoding="utf8") as f:
#     jsonExpectedResult = json.load(f)

# print(jsonData1)
# print((jsonData1.get('locatio')))
# print(jsonData1.get('location').split('/'))
# jsondata2 = {}
# jsondata2['location'] = {}
# jsondata2['location']['country'] = jsonData1.get('location').split('/')[0]
# print(jsondata2)



# print(jsondata2)

# {'deviceID': 'dh28dslkja', 
#  'deviceType': 'LaserCutter', 
#  'timestamp': 1624445837783, 
#  'location': 'japan/tokyo/keiyō-industrial-zone/daikibo-factory-meiyo/section-1', 
#  'operationStatus': 'healthy', 
#  'temp': 22}

# {
#     "deviceID": "dh28dslkja",
#     "deviceType": "LaserCutter",
#     "timestamp": 1624445837783,
#     "location": {
#         "country": "japan",
#         "city": "tokyo",
#         "area": "keiyō-industrial-zone",
#         "factory": "daikibo-factory-meiyo",
#         "section": "section-1"
#     },
#     "data": {
#         "status": "healthy",
#         "temperature": 22
#     }
# }

# print(jsonData1.get('location').split('/'))

# location = ["country","city","area","factory","section"]
# attributes = jsonData1.get('location').split('/')
# jsonData1['location'] = {}


# for i,j in enumerate(location):
#     jsonData1['location'][j] = attributes[i]

   
# jsonData1['status'] = jsonData1['operationStatus']
# del jsonData1['operationStatus']
# jsonData1['data'] = {}
# jsonData1['data']['status'] = jsonData1['status']
# jsonData1['data']['temperature'] = jsonData1['temp']
# del jsonData1['status']
# del jsonData1['temp']
# print(jsonData1)








def convertFromFormat1 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    location = ["country","city","area","factory","section"]
    attributes = jsonObject.get('location').split('/')
    jsonObject['location'] = {}


    for i,j in enumerate(location):
        jsonObject['location'][j] = attributes[i]

   
    jsonObject['status'] = jsonObject['operationStatus']
    del jsonObject['operationStatus']
    jsonObject['data'] = {}
    jsonObject['data']['status'] = jsonObject['status']
    jsonObject['data']['temperature'] = jsonObject['temp']
    del jsonObject['status']
    del jsonObject['temp']
    # print(jsonObject)

    return jsonObject

# print(convertFromFormat1(jsonData1))


# print(jsonData2)
# data2 = jsonData2
# data2['deviceID'] = data2['device']['id']
# data2['deviceType'] = data2['device']['type']
# del data2['device']
# # print(data2['deviceID'],data2['deviceType'])
# # print(data2)
# data2['location'] = {}
# data2['location']['country'] = data2['country']
# data2['location']['city'] = data2['city']
# data2['location']['area'] = data2['area'] 
# data2['location']['factory'] = data2['factory'] 
# data2['location']['section'] = data2['section']
# del data2['section']
# del data2['factory'] 
# del data2['area']
# del data2['city']
# del data2['country']


def convertFromFormat2 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    jsonObject['deviceID'] = jsonObject['device']['id']
    jsonObject['deviceType'] = jsonObject['device']['type']
    del jsonObject['device']
# print(data2['deviceID'],data2['deviceType'])
# print(data2)
    jsonObject['location'] = {}
    jsonObject['location']['country'] = jsonObject['country']
    jsonObject['location']['city'] = jsonObject['city']
    jsonObject['location']['area'] = jsonObject['area'] 
    jsonObject['location']['factory'] = jsonObject['factory'] 
    jsonObject['location']['section'] = jsonObject['section']
    del jsonObject['section']
    del jsonObject['factory'] 
    del jsonObject['area']
    del jsonObject['city']
    del jsonObject['country']
    dt = jsonObject.get('timestamp')
    jsonObject['timestamp'] = int(datetime.datetime.strptime(dt,  "%Y-%m-%dT%H:%M:%S.%f%z").timestamp()*1000)

    return jsonObject

print(convertFromFormat2(jsonData2))
# "2021-06-23T10:57:17.783Z"
# dt = jsonData2.get('timestamp')


# jsonData2['timestamp'] = time.mktime(datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S.%f%z").timetuple())
# print(jsonData2)
# string = "20/01/2020"
# dt = jsonData2.get('timestamp')
# dt = dt.replace('T', ' ')
# print(dt)
# print(time.mktime(datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S.%f%z").timetuple()))
# print((datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S.%f%z").timetuple()))

# print(int(datetime.datetime.strptime(dt,  "%Y-%m-%dT%H:%M:%S.%f%z").timestamp()*1000))

# jsonData2['timestamp'] = time.mktime(datetime.datetime.strptime(jsonData2['timestamp'], "%Y-%m-%dT%H:%M:%S.%f%z").timetuple())



# dt = jsonData2.get('timestamp')
# # epoch time
# print((dt))

# print(type(dt))
# epoch_time = datetime.datetime(1,1,1)
# print(epoch_time)
# # subtract Datetime from epoch datetime
# delta = (dt - epoch_time)
# print('Datetime to Seconds since epoch:', delta.total_seconds())


# def main (jsonObject):

#     result = {}

#     if (jsonObject.get('device') == None):
#         result = convertFromFormat1(jsonObject)
#     else:
#         result = convertFromFormat2(jsonObject)

#     return result


# class TestSolution(unittest.TestCase):

#     def test_sanity(self):

#         result = json.loads(json.dumps(jsonExpectedResult))
#         self.assertEqual(
#             result,
#             jsonExpectedResult
#         )

#     def test_dataType1(self):

#         result = main (jsonData1)
#         self.assertEqual(
#             result,
#             jsonExpectedResult,
#             'Converting from Type 1 failed'
#         )

#     def test_dataType2(self):

#         result = main (jsonData2)
#         self.assertEqual(
#             result,
#             jsonExpectedResult,
#             'Converting from Type 2 failed'
#         )

# if __name__ == '__main__':
#     unittest.main()













-------------------------------------------

import json, unittest, datetime

with open("./data-1.json", "r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json", "r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat2(jsonObject):
    jsonObject['deviceID'] = jsonObject['device']['id']
    jsonObject['deviceType'] = jsonObject['device']['type']
    del jsonObject['device']
    # print(data2['deviceID'],data2['deviceType'])
    # print(data2)
    jsonObject['location'] = {}
    jsonObject['location']['country'] = jsonObject['country']
    jsonObject['location']['city'] = jsonObject['city']
    jsonObject['location']['area'] = jsonObject['area']
    jsonObject['location']['factory'] = jsonObject['factory']
    jsonObject['location']['section'] = jsonObject['section']
    del jsonObject['section']
    del jsonObject['factory']
    del jsonObject['area']
    del jsonObject['city']
    del jsonObject['country']
    dt = jsonObject.get('timestamp')
    jsonObject['timestamp'] = int(
        datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S.%f%z").timestamp() *
        1000)

    # IMPLEMENT: Conversion From Type 1

    return jsonObject


def convertFromFormat1(jsonObject):

    location = ["country", "city", "area", "factory", "section"]
    attributes = jsonObject.get('location').split('/')
    jsonObject['location'] = {}

    for i, j in enumerate(location):
        jsonObject['location'][j] = attributes[i]

    jsonObject['status'] = jsonObject['operationStatus']
    del jsonObject['operationStatus']
    jsonObject['data'] = {}
    jsonObject['data']['status'] = jsonObject['status']
    jsonObject['data']['temperature'] = jsonObject['temp']
    del jsonObject['status']
    del jsonObject['temp']
    # print(jsonObject)

    return jsonObject

    # IMPLEMENT: Conversion From Type 1


def main(jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):
    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(result, jsonExpectedResult)

    def test_dataType1(self):

        result = main(jsonData1)
        self.assertEqual(result, jsonExpectedResult,
                         'Converting from Type 1 failed')

    def test_dataType2(self):

        result = main(jsonData2)
        self.assertEqual(result, jsonExpectedResult,
                         'Converting from Type 2 failed')


if __name__ == '__main__':
    unittest.main()
