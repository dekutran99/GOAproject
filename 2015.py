from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
import numpy as np
import math

f = open("2015.csv", "r")
country = []
happinessRank = []
happinessScore = []
GDPperCapita = [] 
family = []
lifeExpectancy = [] 
freedom = []
generosity = []
trust = []

for line in f.readlines():
  line = line.strip()
  data = line.split(",")
  #print(data)
  country.append(data[0])
  #print(country)
  happinessRank.append(data[1])
  #print(happinessRank)
  happinessScore.append(float(data[2]))
  #print(happinessScore)
  GDPperCapita.append(float(data[5]))
  #print(GDPperCapita)
  family.append(float(data[6]))
  #print(family)
  lifeExpectancy.append(float(data[7]))
  #print(lifeExpectancy)
  freedom.append(float(data[8]))
  #print(freedom)
  generosity.append(float(data[10]))
  #print(generosity)
  trust.append(float(data[9]))
  #print(trust)


#GDPperCapita
hist = np.histogram(GDPperCapita, bins = 155)
yvals = GDPperCapita
xvals = hist[1]
xvals = xvals[0:-1]+(xvals[0]+xvals[1])/2
f1 = figure(y_axis_label = "GDP per Capita")
for (x,y) in zip(xvals, yvals):
  w = (xvals[0]+xvals[1])/2
  f1.vbar(x,w*.9,y,0)
show(f1)

#family
hist = np.histogram(family, bins = 155)
yvals = family
xvals = hist[1]
xvals = xvals[0:-1]+(xvals[0]+xvals[1])/2
f2 = figure(y_axis_label = "Family Score")
for (x,y) in zip(xvals, yvals):
  w = (xvals[0]+xvals[1])/2
  f2.vbar(x,w*.9,y,0)
show(f2)

#lifeExpectancy
hist = np.histogram(lifeExpectancy, bins = 155)
yvals = lifeExpectancy
xvals = hist[1]
xvals = xvals[0:-1]+(xvals[0]+xvals[1])/2
f3 = figure(y_axis_label = "Life Expectancy")
for (x,y) in zip(xvals, yvals):
  w = (xvals[0]+xvals[1])/2
  f3.vbar(x,w*.9,y,0)
show(f3)

#freedom
yvals = freedom
xvals = []
for i in range(len(freedom)):
  xvals.append(float(i+1))
f4 = figure(y_axis_label = "Freedom Score")
for (x,y) in zip(xvals,yvals):
  f4.circle(x,y)
show(f4)

#generosity
yvals = generosity
f5 = figure(y_axis_label = "Generosity Score")
for (x,y) in zip(xvals, yvals):
  f5.circle(x,y)
show(f5)

#trust
yvals = trust
f6 = figure(y_axis_label = "Trust (Government Corruption")
for (x,y) in zip(xvals, yvals):
  f6.circle(x,y)
show(f6)

'''
p = gridplot([[f1,f2],[f3,f4],[f5,f6]])
show(p)
'''
