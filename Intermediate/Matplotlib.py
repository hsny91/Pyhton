import matplotlib.pyplot as plt

year=[2000,2001,2002,2003,2004,2005,2006]
pop=[10.5,20.5,8.5,9,10,10,10]

plt.plot(year,pop)
plt.show()  # show line



gdp_cap=[2000,2001,2002,2003,2004,2005,2006]
life_exp=[10.5,20.5,8.5,9,10,10,10]
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
