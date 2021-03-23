# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 23:10:43 2021

@author: Hassan
"""
#Part 1: Take in user input for both heigh and eidth print out the area #hint: Use the "input" function and don't forget to convert them to ints
h = int(input ("Exter height: "))
w = int(input ("Enter width: ") )
print ("Area: ", h * w)

#Part 2: Iterate through the given list, calculate each item's doubled value, then print out the results #hint: use a for loop my_list = [1,3,5,4,2,6,8,4,8,9,11]
my_list = [1,3,5,4,2,6,8,4,8,9,11]
for I in my_list:
    print ("doubled valued: ", I *2 , "\n")

#Part 3: Iterate through the given dictionary to print out the name (key) and which party they belong to (value) #For example: print out 'Name: Steve' on one line and 'Party: Bride' on the next (for each name in the dictionary) my_dict = {'Steve': 'Bride', 'Tony': 'Groom', 'Peter': 'Bride', 'Josh': 'Bride', 'Clara': 'Groom', 'Martha': 'Groom', 'Charlotte': 'Bride'}
my_dict = {'Steve': 'Bride', 'Tony': 'Groom', 'Peter': 'Bride', 'Josh': 'Bride', 'Clara': 'Groom', 'Martha': 'Groom',
'Charlotte': 'Bride'}

for k, v in my_dict.items():
    print ("Key: ", k, "Value: ", v, "\n")
    
#Part 4: Define a function to calculate the mean, median, and range (range = max-min) of a given list of numbers #hint: use the 'statistics' library for mean and median import statistics my_list = [1,3,5,4,2,6,8,4,8,9,11]
import statistics as stat
my_list = [1,3,5,4,2,6,8,4,8,9,11]

def my_stats (in_list):
    Mn = stat.mean(in_list)
    Md = stat.mean(in_list)
    Rng = max(in_list) - min (in_list)
    return [Mn, Md, Rng]

X, Y, Z = my_stats(my_list)

#Part 5: Print out the current temperature in Fahrenheit for Stanford CA #hint: Use the 'requests' library to make a 'get' call to the 'url', then use the 'json' library to convert the response #to something you can sort through like a dictionary #You'll be looking for 'FeelsLikeF' import requests import json url = 'http://wttr.in/stanford?format=j1'
import requests as req
import json as js
info = req.get('http://wttr.in/stanford?format=j1')
data = info.json()
data.get('current_condition')[0].get("FeelsLikeF")


# I used the following code to visualize the data structure
data.keys()
data.get('current_condition')[0]
