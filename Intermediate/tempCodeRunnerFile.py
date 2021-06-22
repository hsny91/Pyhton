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