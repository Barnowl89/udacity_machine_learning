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

enron_data = pickle.load(open("/Users/Barney/PycharmProjects/machine_learning/lib/ud120-projects/final_project/final_project_dataset.pkl", "br"))


print(len(enron_data))

employee_list = list(enron_data.keys())

print(employee_list)
poi_count = 0

for i, name in zip(range(1), list(enron_data.keys())):

    print(enron_data[name])  #data for employee i
    # print(len(enron_data[name]))
    if(enron_data[name]['poi']) == True:
        poi_count = poi_count + 1

print(poi_count)

poi_file = '/Users/Barney/PycharmProjects/machine_learning/lib/ud120-projects/final_project/poi_names.txt'

poi_count_from_text = 0
with open(poi_file) as f:
    content = f.readlines()
    print(content)
    for line in content:
        if line[0:3] == '(y)' or line[0:3] == '(n)':
            print(line[0:3])
            poi_count_from_text = poi_count_from_text + 1
        else:
            print(line[0:2])
    print(poi_count_from_text)
f.close()

# James Prentice
employee = 'PRENTICE JAMES'
print(enron_data[employee]['total_stock_value'])

employee = 'COLWELL WESLEY'
print(enron_data[employee]['from_this_person_to_poi'])

employee = 'SKILLING JEFFREY K'
print(enron_data[employee]['total_payments'])

employee = 'LAY KENNETH L'
print(enron_data[employee]['total_payments'])

employee = 'FASTOW ANDREW S'
print(enron_data[employee]['total_payments'])



sal_count = 0
for i, name in zip(range(200), list(enron_data.keys())):
    # print(enron_data[name])  #data for employee i
    # print(len(enron_data[name]))
    #if (enron_data[name]['poi']) == True:
    if(enron_data[name]['total_payments']) != 'NaN':
        sal_count = sal_count + 1

print(sal_count)






