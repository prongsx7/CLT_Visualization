import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

data=pd.read_csv(r"C:\Users\Dell\Documents\sem2\es111\CLT_Visualization\IndianHousePrices.csv") #reading file

df=pd.DataFrame(data) #converting file into a data set

prices=df['Price'] #extracting price column

prices=prices.dropna() #dropping null values

population_length=len(prices) #finding number of prices

prices_array=np.array(prices) #converting prices column into an array
maximum=np.max(prices_array)
minimum=np.min(prices_array)

def mean(n,Prices):
    sum=0
    for i in Prices:
        sum+=i
    mean=sum/n
    return mean

def var(n,Prices):
    s=0
    for i in Prices:
        s+=i
    m=s/n
    f=0
    for z in range (0,n):
        f+=((Prices[z]-m)*(Prices[z]-m))
    v=f/n-1
    return v
def std_dev(n,Prices):
    s=math.sqrt(var(n,Prices))
    return s

print("----------------PART A----------------")
print("Number of valid prices: ",population_length)
print("Maximum value: ",maximum)
print("Minimum value: ",minimum)
print("Mean: ",mean(population_length,prices_array))
print("Variance: ",var(population_length,prices_array))
print("Standard Deviation: ",std_dev(population_length,prices_array))

plt.hist(prices_array,bins=90)
plt.title("Histogram of Original Price Data")
plt.xlim(0,1000)
plt.xlabel("Prices")
plt.ylabel("Frequency")
plt.show()

print("----------------PART B----------------")

#   SAMPLE SIZE = 5
sample1_means=[]
l=1
while l<=1000:    #looping through random samples a 1000 times and storing in sample means array
    sample1=[]
    for i in range(0,5):  #looping 5 time to get random prices and storing in sample array
        z=int((np.random.choice(prices_array)))
        sample1.append(z)
    m=mean(5,sample1)     #calculating sample mean
    sample1_means.append(m)
    l+=1
plt.hist(sample1_means,bins=100)
plt.title("Sampling Distribution of Mean Without Replacement (Sample size = 5)")
plt.xlim(0,400)
plt.xlabel("Prices")
plt.ylabel("Frequency")
plt.show()


#repeating same process above with different sample sizes
#   SAMPLE SIZE = 10
l=1
sample2_means=[]
while l<=1000:
    sample2=[]
    for i in range(0,10):
        z=int((np.random.choice(prices_array)))
        sample2.append(z)
    m=mean(10,sample2)
    sample2_means.append(m)
    l+=1
plt.hist(sample2_means,bins=100)
plt.title("Sampling Distribution of Mean Without Replacement (Sample size = 10)")
plt.xlim(0,400)
plt.xlabel("Prices")
plt.ylabel("Frequency")
plt.show()

#   SAMPLE SIZE = 30
sample3_means=[]
l=1
while l<=1000:
    sample3=[]
    for i in range(0,30):
        z=int((np.random.choice(prices_array)))
        sample3.append(z)
    m=mean(30,sample3)
    sample3_means.append(m)
    l+=1
plt.hist(sample3_means,bins=100)
plt.title("Sampling Distribution of Mean Without Replacement (Sample size = 30)")
plt.xlim(0,400)
plt.xlabel("Prices")
plt.ylabel("Frequency")
plt.show()

#   SAMPLE SIZE = 100
sample4_means=[]
l=1
while l<=1000:
    sample4=[]
    for i in range(0,100):
        z=int((np.random.choice(prices_array)))
        sample4.append(z)
    m=mean(100,sample4)
    sample4_means.append(m)
    l+=1
plt.hist(sample4_means,bins=100)
plt.title("Sampling Distribution of Mean Without Replacement (Sample size = 100)")
plt.xlim(0,400)
plt.xlabel("Prices")
plt.ylabel("Frequency")
plt.show()
