blocks = [
    {
        "blockId": 1,
        "startTime": "2012-05-18 07:00",
        "endTime": "2012-05-18 10:00",
    },
    {
        "blockId": 1,
        "startTime": "2012-05-18 12:00",
        "endTime": "2012-05-18 13:00",
    },
    {
        "blockId": 2,
        "startTime": "2012-05-18 13:00",
        "endTime": "2012-05-18 15:00",
    },
    {
        "blockId": 2,
        "startTime": "2012-05-18 15:00",
        "endTime": "2012-05-18 16:00",
    },
    {
        "blockId": 2,
        "startTime": "2012-05-18 16:30",
        "endTime": "2012-05-18 17:30",
    },
    {
        "blockId": 1,
        "startTime": "2012-05-18 18:00",
        "endTime": "2012-05-18 20:00",
    }
]
blocks2 = [
    {
        "blockId": 1,
        "startTime": "2012-05-18 07:00",
        "endTime": "2012-05-18 10:00",
    },
    {
        "blockId": 1,
        "startTime": "2012-05-18 12:00",
        "endTime": "2012-05-18 13:00",
    },
    {
        "blockId": 2,
        "startTime": "2012-05-18 13:00",
        "endTime": "2012-05-18 15:00",
    },
    {
        "blockId": 2,
        "startTime": "2012-05-18 15:00",
        "endTime": "2012-05-18 16:00",
    },
    {
        "blockId": 1,
        "startTime": "2012-05-18 16:30",
        "endTime": "2012-05-18 17:30",
    },
    {
        "blockId": 1,
        "startTime": "2012-05-18 18:00",
        "endTime": "2012-05-18 20:00",
    }
]
# if block id is same starttime is of first block and endtime = endtime of last block
temp = blocks2[0]
arr = []
for i in blocks2:
    if temp['blockId'] == i['blockId']:
        temp['endTime'] = i['endTime']
    else:
        arr.append(temp)
        temp = i
# arr.append(temp)
print(arr)