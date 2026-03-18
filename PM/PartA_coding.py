# PART A:
#Q1.
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000)
#mean
total = 0
for x in data:
    total += x
mean = total/len(data)
#variance
var_sum = 0
for x in data:
    var_sum += (x-mean)** 2
variance = var_sum/len(data)
#standard deviation
std = variance**0.5

print("Mean:", mean)
print("Variance:", variance)
print("Std:", std)

# plot
plt.hist(data, bins=30)
plt.title("Normal Distribution")
plt.show()

#---------------------------------------------------------------------------------
#Q2.
z_data = []

for x in data:
    z = (x-mean)/std
    z_data.append(z)

new_mean = sum(z_data)/len(z_data)

var_sum = 0
for x in z_data:
    var_sum += (x-new_mean)**2
new_std = (var_sum/len(z_data))**0.5

print("New Mean:", new_mean)
print("New Std:", new_std)

#-------------------------------------------------------------------------------------------
#Q3.
marks = [50, 60, 70, 80, 90, 100, 30, 20, 85, 95]

# mean
mean = sum(marks)/len(marks)

# median
sorted_marks = sorted(marks)
n = len(marks)
if n % 2==0:
    median=(sorted_marks[n//2]+sorted_marks[(n//2)-1])/2
else:
    median = sorted_marks[n//2]

# variance
var_sum = 0
for x in marks:
    var_sum += (x-mean)**2
variance = var_sum/len(marks)

#std
std = variance ** 0.5

print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Std:", std)

# outliers
for x in marks:
    z = (x-mean)/std
    if abs(z)>2:
        print("Outlier:", x)
#------------------------------------------------------------------------------------------
#Q4.
import math
data = [50, 55, 60, 65, 70]
mean = sum(data) / len(data)

# std
var_sum = 0
for x in data:
    var_sum += (x - mean)** 2
std = (var_sum / len(data)) ** 0.5

# given mean
mu = 60

# Z formula
z = (mean -mu) / (std / math.sqrt(len(data)))

print("Z value:", z)

# decision
if abs(z) > 1.96:
    print("Reject H0")
else:
    print("Do not reject H0")

#----------------------------------------------------------------------------------
#Q5.
import random
import math

count = 0
tests = 1000

for t in range(tests):
    data = []
    for i in range(30):
        data.append(random.gauss(0, 1))  # H0 true

    mean = sum(data) / len(data)

    var = 0
    for x in data:
        var += (x-mean)**2
    std = (var/len(data))**0.5

    z = mean/(std / math.sqrt(len(data)))

    if abs(z)>1.96:
        count += 1

print("False positive rate:", count/tests)
