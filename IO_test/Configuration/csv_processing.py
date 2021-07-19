# this code converts information stored in csv file 
#  into a list of lists, then into a dictionary if required

import csv

with open('configuration.csv','r') as config_file:

# turns csv into list of lists e.g.[['Cancer Depth', '35']...]
    configuration = list(csv.reader(config_file))  

configuration = dict([a, float(x)] for a,x in configuration) 
print (configuration)
# converts information stored in configuration.csv into dictionary 
# with keys as str and values as float {'Cancer Depth' : 35.0, ...}


