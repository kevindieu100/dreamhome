from pandas import *
import pandas
import numpy as np
import matplotlib.pyplot as plt
import random
<<<<<<< HEAD
housing = read_csv('C:\Users\Trey\Documents\CaliCounty.txt')
food = read_csv('C:\Users\Trey\Documents\cfood.txt')
temp = read_csv('C:\Users\Trey\Documents\meantemp.txt')
=======
import cgi
import cgitb; cgitb.enable() #for trouble
from django import forms


housing = read_csv('CaliCounty.txt')
food = read_csv('cfood.txt')
temp = read_csv('meantemp.txt')
curl = read_csv('curl.txt')
>>>>>>> 26e2b6f8280d94ff7d8afd88e21ebf9b0a93bdfb
city = Series(food['geoname'])
county = Series(food['county_name'])
foodcost = Series(food['cost_yr'])
median = Series(food['median_income'])
housingcounty = Series(housing['State/Region/County'])
countyprices = Series(housing['15-Sep'])
temperature = Series(temp['Avg Daily Max Air Temperature'])
countyTemp = Series(temp['County'])
#temp.ix[0:10]
#housing[0:10]
#temperature[0:15]
#price[1000:1003]
tempindex = []
values = []
def simplesearch(x,y,aseries):
    for i in range(0, len(aseries.index)):
        if x<aseries[i]<y:
            values.append(i)
def tempsearch(x,y,aseries):
    for i in range(0, len(aseries.index)):
        if x<aseries[i]<y:
            tempindex.append(i)
<<<<<<< HEAD
=======

#all variables
maxbudgethouse = 800000
#bracket
#temp
low = 90000
high = 96000
t1 = 60
t2 = 80
bracket0 = '$1 - $18k'
bracket1 = '$19k - $75k'
bracket2 = '$76k - $151k'
bracket3 = '$152k - $230k'
bracket4 = '$231k - $411k'
bracket5 = '$412k - $464k'
bracket6 = '$464k - up'



bracket = forms.ModelChoiceField(label='tax')
temperature = forms.ModelChoiceField(label='temperature')
maxbudgethouse = forms.CharField(label='budget', max_length = 100)


if bracket == bracket0:
	low = 1
	high = 18000
if bracket == bracket1:
	low = 19000
	high = 75000
if bracket == bracket2:
	low = 76000
	high = 151000
if bracket == bracket3:
	low = 152000
	high = 2300000
if bracket == bracket4:
	low = 231000
	high = 411000
if bracket == bracket5:
	low = 412000
	high = 464000
if bracket == bracket0:
	low = 465000
	high = 10000000000
temp0 = '40-50'
temp1 = '50-60'
temp2 = '60-70'
temp3 = '70-80'
temp4 = '80-90'

if temp == temp0:
	t1 = 40
	t2 = 50
if temp == temp1:
	t1 = 50
	t2 = 60
if temp == temp2:
	t1 = 60
	t2 = 70
if temp == temp3:
	t1 = 70
	t2 = 80
if temp == temp4:
	t1 = 80
	t2 = 90

>>>>>>> 26e2b6f8280d94ff7d8afd88e21ebf9b0a93bdfb
values = []
tempindex = []
low = 19000
high = 75000
simplesearch(low, high, median)
t1 = 60
t2 = 90
tempsearch(t1,t2, temperature)
apples = []
acost = []
toDifCounties = []
differentcounties = []
def pair(avalue, b, a, c):
    for i in range(0, len(avalue)):
        thisiscounty = b[avalue[i]]
        thisiscity = a[avalue[i]]
        thisisreturn = 'City: '+str(thisiscity) + '       County: ' + str(thisiscounty)
        apples.append(thisisreturn)
        acost.append(c[avalue[i]])
        differentcounties.append(thisiscounty)
    return 0
def countytms(index,names):
    for j in range(0, len(index)):
        avariable = names[index[j]]
        toDifCounties.append(avariable)
apples = []
acost = []
toDifCounties = []
differentcounties = []
pair(values, county, city, foodcost)
countytms(tempindex, countyTemp)
toDifCounties
#apples
#toDifCounties
#countyTemp[tempindex[10]]
TempArray = []

secondIndex = []
for z in range(0, len(differentcounties)):
    for q in range(0, len(toDifCounties)):
        if differentcounties[z]==toDifCounties[q]:
            TempArray.append(differentcounties[z])
            secondIndex.append(values[z])


#TempArray
#foodcost[secondIndex]

#countyname
#yup
indexprices = []
structure = []
def lowerthan(takeArray, countieshousing, pricecounties, maxprice):
    for w in range(0, len(takeArray)):
        for p in range(0, len(countieshousing.index)):
            if takeArray[w] == countieshousing[p]:
                if pricecounties[p] < maxprice:
                    indexprices.append(secondIndex[w])
                    structure.append(takeArray[w])
maxbudgethouse = 8000000
indexprices = []
structure = []
lowerthan(TempArray, housingcounty, countyprices, maxbudgethouse)
min = 1000000000
temporary = 0;

for t in range(0, len(indexprices)):
    if foodcost[indexprices[t]] < min:
        min = foodcost[indexprices[t]]
        temporary = t
        thestring = foodcost[indexprices[temporary]]
        countyname = structure[temporary]
for p in range(0, len(housingcounty.index)):
    if countyname == housingcounty[p]:
        zebopdedop = countyprices[p]
structure[temporary] + '       Annual Food Cost: $' + str(thestring) + "       Median House Price: $" + str(zebopdedop)