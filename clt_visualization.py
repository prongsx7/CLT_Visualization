import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

data=pd.read_csv(r"C:\Users\Dell\Documents\sem2\es111\CLT_Visualization\IndianHousePrices.csv") #reading file

df=pd.DataFrame(data) #converting file into a data set

prices=df['Price'] #extracting price column

prices=prices[prices!=0] #dropping zero values
prices=prices.dropna() #dropping null values

population_length=len(prices) #finding number of prices

prices_array=np.array(prices) #converting prices column into an array
maximum=np.max(prices_array)
minimum=np.min(prices_array)

def mean(n,Prices):  #calculating mean manually
    sum=0
    for i in Prices:
        sum+=i
    mean=sum/n
    return mean

def var(n,Prices):  #calculating variance manually
    s=0
    for i in Prices:
        s+=i
    m=s/n
    f=0
    for z in range (0,n):
        f+=((Prices[z]-m)*(Prices[z]-m))
    v=f/(n-1)
    return v

def std_dev(n,Prices):   #calculating standard deviation manually
    s=math.sqrt(var(n,Prices))
    return s

def z_value(n,x,std,mu):   #calculating z value manually
    z=(x-mu)/(std/math.sqrt(n))
    return z

mu=mean(population_length,prices_array)
sigma=std_dev(population_length,prices_array)

print("----------------PART A----------------")
print("Number of valid prices: ",population_length)
print("Maximum value: ",maximum)
print("Minimum value: ",minimum)
print("Mean: ",mu)
print("Variance: ",var(population_length,prices_array))
print("Standard Deviation: ",sigma)

plt.figure()
plt.hist(prices_array,bins=90)
plt.title("Histogram of Original Price Data")
plt.xlim(0,1000)
plt.xlabel("Prices")
plt.ylabel("Frequency")
plt.show()

#----------------PART C----------------

# SAMPLING DISTRIBUTUION OF MEAN FOR N=5
sample1_means=[]
l=1
while l<=1000:    #looping through random samples a 1000 times and storing in sample means array
    sample1=[]
    for i in range(0,5):  #looping 5 time to get random prices and storing in sample array
        s=float((np.random.choice(prices_array)))
        sample1.append(s)
    m=mean(5,sample1)     #calculating sample mean
    sample1_means.append(m)
    l+=1
plt.figure()
plt.hist(sample1_means,bins=100)
plt.title("Sampling Distribution of Mean (Sample size = 5)")
plt.xlim(0,400)
plt.xlabel("Prices")
plt.ylabel("Frequency")
plt.show()


#   SAMPLING DISTRIBUTUION OF MEAN FOR N=10
l=1
sample2_means=[]
while l<=1000:
    sample2=[]
    for i in range(0,10):
        s=float((np.random.choice(prices_array)))
        sample2.append(s)
    m=mean(10,sample2)
    sample2_means.append(m)
    l+=1
plt.figure()
plt.hist(sample2_means,bins=100)
plt.title("Sampling Distribution of Mean (Sample size = 10)")
plt.xlim(0,400)
plt.xlabel("Prices")
plt.ylabel("Frequency")
plt.show()


#   SAMPLING DISTRIBUTUION OF MEAN FOR N=30
sample3_means=[]
l=1
while l<=1000:
    sample3=[]
    for i in range(0,30):
        s=float((np.random.choice(prices_array)))
        sample3.append(s)
    m=mean(30,sample3)
    sample3_means.append(m)
    l+=1
plt.figure()
plt.hist(sample3_means,bins=100)
plt.title("Sampling Distribution of Mean (Sample size = 30)")
plt.xlim(0,400)
plt.xlabel("Prices")
plt.ylabel("Frequency")
plt.show()


#   SAMPLING DISTRIBUTUION OF MEAN FOR N=100
sample4_means=[]
l=1
while l<=1000:
    sample4=[]
    for i in range(0,100):
        s=float((np.random.choice(prices_array)))
        sample4.append(s)
    m=mean(100,sample4)
    sample4_means.append(m)
    l+=1
plt.figure()
plt.hist(sample4_means,bins=100)
plt.title("Sampling Distribution of Mean (Sample size = 100)")
plt.xlim(0,400)
plt.xlabel("Prices")
plt.ylabel("Frequency")
plt.show()


#----------------PART C----------------

# Z DISTRIBUTION FOR SAMPLE SIZE 10
sample2_z=[]
for i in range(0,1000):     #looping 1000 times to get 1000 z values for the 1000 means
    p=z_value(10,sample2_means[i],sigma,mu)    #calling z value function 
    sample2_z.append(p)
plt.figure()
plt.hist(sample2_z,bins=40)
plt.title("Distribution of z-values for N = 10")
plt.xlabel("Z-Value")
plt.ylabel("Frequency")
plt.show()


# Z DISTRIBUTION FOR SAMPLE SIZE 30
sample3_z=[]
for i in range(0,1000):
    p=z_value(30,sample2_means[i],sigma,mu)
    sample3_z.append(p)
plt.figure()
plt.hist(sample3_z,bins=40)
plt.title("Distribution of z-values for N = 30")
plt.xlabel("Z-Value")
plt.ylabel("Frequency")
plt.show()


# Z DISTRIBUTION FOR SAMPLE SIZE 100
sample4_z=[]
for i in range(0,1000):
    p=z_value(100,sample4_means[i],sigma,mu)
    sample4_z.append(p)
plt.figure()
plt.hist(sample4_z,bins=40)
plt.title("Distribution of z-values for N = 100")
plt.xlabel("Z-Value")
plt.ylabel("Frequency")
plt.show()