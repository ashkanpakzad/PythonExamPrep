import csv
import json
import matplotlib.pyplot as plt
import numpy as np

## Load CSV file.
with open("python_language_1_data.csv") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = []
    for row in reader:
        data.append(row)

## Convert to dictionary keyed by year.
data_dict = {}
for i in range(1937, 2012+1, 1): # create year keys for all years in data
    data_dict[i] = {}
    for row in data:
        if i == int(row[0]):
            data_dict[i][int(row[1])] = float(row[2]) # day key equal to rainfall value
        else:
            pass

## save as JSON file.
with open('rainfall.json', 'w') as outfile:
    json.dump(data_dict, outfile)

## plot yearly data function
def PlotYearRain(JSONfilename, year, color='blue'):
    year = str(year)
    with open(JSONfilename, 'r') as f:
        datastore = json.load(f)
    currentdata = datastore[year]
    x,y = zip(*currentdata.items()) # seperate key and value into new lists.
    x = [int(i) for i in x] # change string numbers to ints.
    new_x, new_y = zip(*sorted(zip(x, y))) # sort days into order.
    return plt.plot(new_x,new_y, color=color, marker='.', linestyle='-')

## Plot data for 1998 in Question b
PlotYearRain('rainfall.json', 1998, color='blue')
plt.savefig('questionb.png')

## Plot year mean function
def PlotYearlyMean(JSONfilename, lowertime, uppertime):
    with open(JSONfilename, 'r') as f:
        datastore = json.load(f)
    years = list(np.arange(lowertime, uppertime+1))
    means = np.zeros_like(years)
    for i in range(lowertime, uppertime+1):
        idx = i-lowertime
        datalist = sorted(datastore[str(i)].items())
        _,y = zip(*datalist)
        means[idx] = np.mean(y)
    years = [int(i) for i in years]
    means = [float(i) for i in means]
    return plt.plot(years, means ,'.-')

## Plot data for 1988 to 2000 in Question c
plt.cla()
PlotYearlyMean('rainfall.json', 1988, 2000)
plt.savefig('questionc.png')

## correction factor question d
def correctRain(InCorrectRainfall):
    return InCorrectRainfall*1.2**np.sqrt(2)

## Function 1 in Question d - using for loop
def loopCorrection(JSONfilename, lowertime, uppertime):
    with open(JSONfilename, 'r') as f:
        datastore = json.load(f)
    for i in range(lowertime, uppertime+1):
        for j in range(366+1):
            try:
                datastore.get(str(i))[str(j)]
                datastore[str(i)][str(j)] = correctRain(datastore[str(i)][str(j)])
            except KeyError:
                pass
    return datastore

loop_correct = loopCorrection('rainfall.json', 2005, 2011)
with open('rainfall_corrected_loop.json', 'w') as outfile:
    json.dump(loop_correct, outfile)

## Function 2 in Question d - using list comprehension
def listcomCorrection(JSONfilename, lowertime, uppertime):
    """
        List comprehension often more expressive, rolls of the tongue and can be written in fewer lines, however, can get very confusing when it gets this complicated.
        List comprehensions also execute by allocating required memory rather than allocating on the go, increasing memory efficiency and computational speed.
    """
    with open(JSONfilename, 'r') as f:
        datastore = json.load(f)
    years = np.arange(lowertime, uppertime+1)
    datastore = {outer_k: {k: (correctRain(v)  if int(outer_k) in years else v) for (k,v) in outer_v.items()} for (outer_k,outer_v) in datastore.items()}
    return datastore

list_correct = listcomCorrection('rainfall.json', 2005, 2011)
with open('rainfall_corrected_list.json', 'w') as outfile:
    json.dump(list_correct, outfile)
