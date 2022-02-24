import csv
from collections import Counter

file = open("SOCR-HeightWeight.csv")
fileRead = csv.reader(file)
filedata = list(fileRead)
filedata.pop(0)
emptylist = []

for i in range(len(filedata)) :
    height = filedata[i][1]
    emptylist.append(float(height))

n = len(emptylist)
total = 0

for j in emptylist :
    total =total+j

mean = total/n

emptylist.sort()

if n % 2 == 0 :
    median1 =float(emptylist[n//2])
    median2 =float(emptylist[n//2 - 1])
    median = (median1 + median2) /2
else:
    median =emptylist[n//2]

data = Counter(emptylist)
modeData = {
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occurence in data.items():
    if 50 < float(height) < 60 :
        modeData["50-60"] += occurence
    elif 60 < float(height) < 70 :
        modeData["60-70"] += occurence
    elif 70 < float(height) < 80 :
        modeData["70-80"] += occurence

modeRange,modeOccurence = 0,0

for range,occurence in modeData.items() :
    if occurence > modeOccurence :
        modeRange,modeOccurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence

mode = float((modeRange[0]+modeRange[1])/2)
print(mode)