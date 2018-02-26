#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)


### your code below
# find outliers: people who made the most salary and highest bonuses
greedy = []
for (outer_k) in data_dict:
        person = data_dict[outer_k]
        if (person['salary']> 1000000 and person['salary'] != 'NaN' and  person['bonus']> 5000000 and person['salary'] != 'NaN'):
            greedy.append(outer_k)
for item in greedy:
    print(item)

stock_options = []
for person in data_dict:
    stock = data_dict[person]['exercised_stock_options']
    if stock != 'NaN':
        stock_options.append(stock)

stock_options2 = [value['salary'] for key, value in data_dict.items()
                  if value['salary'] != 'NaN']
#for element in stock_options2:
#    print (element)
print(min(stock_options2))
print(max(stock_options2))

for point in data:
    salary = int(point[0])
    bonus = int(point[1])
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.autoscale(False)
#matplotlib.pyplot.xlim((0, 10000000))
#matplotlib.pyplot.ylim((0, 10000000))

matplotlib.pyplot.show()
