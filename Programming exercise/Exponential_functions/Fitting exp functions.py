import numpy as np
import matplotlib.pyplot as plt


""" The function fit_exp_fun finds the best exponential graph (in red) that best fits the given 
data set rapresented by the blue dots."""

def fit_exp_fun(filename):
    parameters = np.array([]) #creates an empty array to store the used parameters
    
    x_data, y_data = np.loadtxt(filename, skiprows=1, unpack = True) #opens the .txt file

    log_y_data = np.log(y_data) #takes the natural log of the Y_values

    val_1, val_2 = np.polyfit(x_data, log_y_data, 1) #thanks to the finction polyfit I found
    #the parameters that best approximate the exponential growth
    y = np.exp(val_2)*np.exp(val_1*x_data) #makes a curve with those values
    
    parameters = np.append(parameters, val_1) #saves the parameters in a Readme.txt file
    parameters = np.append(parameters, val_2)
    np.savetxt("Readme_for_parameters.txt", parameters, header="Parameters")
    
    #plotting operations
    plt.plot(x_data, y_data, "o")
    plt.plot(x_data, y, color="r")
    plt.title('Fitting of exponential function', c="r")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()
    
    
fit_exp_fun("expFcn3.txt")