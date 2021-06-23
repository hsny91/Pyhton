import matplotlib.pyplot as plt

year=[2000,2001,2002,2003,2004,2005,2006]
pop=[10.5,20.5,8.5,9,10,10,10]
gdp_cap=[2000,2001,2002,2003,2004,2005,2006]
life_exp=[10.5,20.5,8.5,9,10,10,10]

plt.plot(year,pop)
plt.show()  # show line

####  Customized  ####
## plt.xlabel('year')=> x axis labels 
## plt.ylabel('year')=> y axis labels
#  plt.title('title') => title
# plt.yticks/yticks([0,1,2], ["one","two","three"]) ==>scale

# Basic scatter plot, log scale
plt.scatter(year, pop)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels

plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# After customizing, display the plot
plt.show()

# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# After customizing, display the plot
plt.show()

#### SCATTER ######

plt.scatter(gdp_cap, life_exp)  # nokta nokta gosterim

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()

import matplotlib.pyplot as plt
life_exp=[10.5,20.5,8.5,9,10,10,10]
#########  HISTOGRAM  #########
# plt.hist(value, bins=20)
# plt.show() displays a plot;
# bins ==> divide value how many piece
#plt.clf() cleans it up again so you can start afresh.


# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()

# Build histogram with 5 bins
plt.hist(life_exp, bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins=20)

# Show and clean up again
plt.show()
plt.clf()
