from matplotlib import pyplot as plt

# ---- stackplot ---- #

## fig, ax 
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

fig, ax = plt.subplots(figsize=(5,3))
ax.stackplot(years, gdp, labels=['green line'])
ax.set_title('Nominal GDP (Area Chart)')
ax.legend(loc='upper left')
ax.set_ylabel('Billions of $')
fig.tight_layout()
fig.show()

## plt
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
plt.stackplot(years, gdp, color="green")
plt.title("Nominal GDP")
plt.ylabel("Billions of $")
plt.xlabel("Years")
plt.show()



# ---- line ---- #
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

fig, ax = plt.subplots(figsize=(5,3))
ax.plot(years, gdp, color='green', marker='x', linestyle='solid')
ax.set_title('Nominal GDP (Line Chart)')
ax.legend(loc='upper left')
ax.set_ylabel('Billions of $')
fig.tight_layout()
fig.show()

# ---- bar plot ---- #
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

fig, ax = plt.subplots(figsize=(5,3))
ax.bar(years, gdp, color='green')
ax.set_title('Nominal GDP (Bar Chart)')
ax.legend(loc='upper left')
ax.set_ylabel('Billions of $')
fig.tight_layout()
fig.show()

# ---- scatter plot ---- #
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x=years, y=gdp, marker='o', c='blue', edgecolor='orange')
ax.set_title('Nominal GDP (Scatter: Year & GDP)')
ax.legend(loc='upper left')
ax.set_ylabel('Billions of $')
fig.tight_layout()
fig.show()

##########
# movies #
##########

#---- Original Bar Chart ----#

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5,11,3,8,10]

plt.bar(range(len(movies)), num_oscars)
plt.title("My Favorite Movies")
plt.ylabel("# of Academy Awards")
plt.xticks(range(len(movies)), movies)
plt.show()

# ---- Stem Chart ---- #

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5,11,3,8,10]
plt.stem(range(len(movies)), num_oscars)
plt.title("My Favorite Movies")
plt.ylabel("# of Academy Awards")
plt.xticks(range(len(movies)), movies)
plt.show()

#---- Horizontal Bar Chart ----#

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5,11,3,8,10]

fig, ax = plt.subplots(figsize=(5,3))
ax.barh(movies, num_oscars, color='purple')
ax.set_title('Favorite Movies: Horizontal Bar Chart')
ax.set_xlabel('# of Academy Awards')
fig.tight_layout()
fig.show()

#---- Step Plot ----#

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5,11,3,8,10]

fig, ax = plt.subplots(figsize=(5,3))
ax.step(movies, num_oscars)
ax.set_title('Favorite Movies: Step Plot')
ax.set_xlabel('# of Academy Awards')
fig.tight_layout()
fig.show()

#---- Stem Plot ----#

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5,11,3,8,10]
plt.stem(movies, num_oscars)
plt.title("My Favorite Movies")
plt.ylabel("# of Academy Awards")
plt.xticks(range(len(movies)), movies)
plt.show()

# ---- Plot Vertical Lines (confusing)----#
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5,11,3,8,10]
plt.vlines(movies, num_oscars, ymax=15)
plt.title("My Favorite Movies")
plt.ylabel("# of Academy Awards")
plt.xticks(range(len(movies)), movies)
plt.show()


