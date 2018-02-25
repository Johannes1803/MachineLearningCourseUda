#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle


enron_data = pickle.load(open("/home/johannes/PycharmProjects/UdacityMLIntro/BayesAnaConda/final_project/final_project_dataset.pkl", "r"))

counter = 0
for key in enron_data:
    if enron_data[key]["email_address"] != 'NaN':
        counter +=1

#salaryQuan = {key: value for (key, value) in enron_data.items() if key[poi]}


print("length: ")
print(counter)

print("stock: ")
print(enron_data["SKILLING JEFFREY K"])
