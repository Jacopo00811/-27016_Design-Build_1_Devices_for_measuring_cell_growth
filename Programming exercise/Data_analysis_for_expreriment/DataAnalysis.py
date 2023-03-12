import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.ticker as mticker

""" The following code analyzes and plots the data set (OD values) that has been collected over the week-end.
An easy user interface has been implemented to make the choice of the graph easier."""

# This def. is used in the curve fitting to give a certain shape at the curve
def S_curve(x, L ,x0, k, b):
    y = L / (1 + np.exp(-k*(x-x0)))
    return (y)

# Here the file is being opend and the last 1328 measuraments are being cut off
# because they were useless considering that we found the stationary phase
Y_vals = np.loadtxt("DATAEXP2.txt")
Y_vals = Y_vals[:-1328]
X_vals = np.arange(np.size(Y_vals)) # Creates an array that represents the time interval
# (We took one measurament every minute)
                   

p0 = [max(Y_vals), np.median(X_vals),1,min(Y_vals)] # this is an mandatory initial guess 
# used by the curve_fit function
popt, pcov = curve_fit(S_curve, X_vals, Y_vals ,p0 ,method='dogbox') # finds the fit of the data

S_curve_fit = S_curve(X_vals, *popt) # assign the fit of data to this variable for future uses

# Calculates the first derivative and uses the formula to find µ
dAdt = np.gradient(S_curve_fit ,X_vals)
µ = dAdt*(1/S_curve_fit)

np.seterr(all="ignore")


# makes a cut of the data to  graph the exponential curve fit
Y_vals1 = Y_vals[:1900]
X_vals1 = X_vals[:1900]
log_Y_vals = np.log(Y_vals1) #takes the log of the OD values 

# function used to make an exponential fit (re-used from the assignment)
val_1, val_2 = np.polyfit(X_vals1, log_Y_vals, 1)
y = np.exp(val_2)*np.exp(val_1*X_vals1) # Create the functio of the type y = exp(x)*exp(y*t)





# Creates the small user interface and get the input for the desired graph
request = input("Would you like the plot of:\n -A  Data and fitting\n -B  Growth rate (µ)\n -C  Growth rate (dOD/dt)\n Enter your answer here: ")

if request.lower() == "a": # Creates: scatter plot with data, best fit (red) and exponential fit (orange)
    plt.scatter(X_vals/60, Y_vals, s=1) 
    plt.plot(X_vals/60, S_curve_fit,c="r", label = "Fit of data")
    plt.title("Yeast growth S-curve", c="r") 
    plt.xlabel("Time")
    plt.ylabel("OD-value") # Set some titles and unit of measure 
    plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%d h'))
    plt.xticks(np.arange(min(X_vals/60), max(X_vals/60)+1, 5))
    plt.plot(X_vals1/60, y, color="orange",ls= "--", label = "Exponential fit")
    plt.ylim(0,5)
    plt.legend()
    plt.show()
    plt.savefig("1.jpg")
    
elif request.lower() == "b" : # Creates the graph for the growth rate  (µ)
    plt.plot(X_vals/60,µ*10000, "-")
    plt.title("Yeast growth rate", c="r")
    plt.xlabel("Time")
    plt.ylabel("Growth rate (10 mµ)") # Set some titles and unit of measure
    plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%d h'))
    plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d OD⋅h'))
    plt.xticks(np.arange(min(X_vals/60), max(X_vals/60)+1, 5))
    plt.show()
    plt.savefig("2.jpg")
    
elif request.lower() == "c": # Creates  the graph for the growth rate (dOD/dt)
    plt.plot(X_vals/60,dAdt, "-")
    plt.title("Yeast growth rate", c="r")
    plt.xlabel("Time")
    plt.ylabel("Growth rate (OD/h)")# Set some titles and unit of measure
    plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%d h'))
    plt.xticks(np.arange(min(X_vals/60), max(X_vals/60)+1, 5))
    plt.show()
    plt.savefig("3.jpg")
    
else:
    print("Sorry, invalid input") # Output message if the input is invalid