import numpy as np
import matplotlib.pyplot as plt
import math as mt


"""The function data_generator creates 1000 datapoints for a S curve and saves them in a .txt file 
that can be found in the work directory. It is a parameterizable function that allows to pass: min. value, max value,
the parameters a & k that control the shape of the curve and a random value that simulates the noise on the data points"""

def data_generator(min_v,max_v,a,k,random_value):
    x = np.arange(0,1000) #creates the X value array with 1000 integer numbers
    x0 = np.mean(x)  #finds the mean for future calculations 
    data = np.vstack((x,np.zeros(1000))) 
    data = data.T #stacks and transpose the two arrays into a 1000x2 matrix
    
    if random_value < 0: #check on the random value sing
        for i in range(1000):
            data[i,1] = min_v+(max_v-min_v)*(1/(1+mt.exp(-k*(x[i]-x0)))**a)+np.random.uniform(random_value, -random_value)
            np.savetxt("data.txt", data, delimiter = " | ", header= "X values | Y values")
    else:
        for i in range(1000):
           data[i,1] = min_v+(max_v-min_v)*(1/(1+mt.exp(-k*(x[i]-x0)))**a)+np.random.uniform(-random_value, random_value)
           np.savetxt("data.txt", data, delimiter = " | ", header= "X values | Y values")
           #writes the Y-value into the file that has been found according to the above (with the additon of the noise)
    return data


"""The following function simply plots the X and Y values and sets titles for the graph and the axis"""

def plot_data(data):
    
    plt.plot(data[:,0],data[:,1])
    plt.title('S-curve Plot', c="r")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()
    
    
    
    
    
    
data=data_generator(5,70,1.2,0.01,2.3)
#print(data_generator(0,1000,1,3,-10))
print(plot_data(data))