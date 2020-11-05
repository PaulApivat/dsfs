from matplotlib import pyplot as plt

# ---- stackplot ---- #
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

fig, ax = plt.subplots(figsize=(5,3))
ax.stackplot(years, gdp, labels=['green line'])
ax.set_title('Nominal GDP (Area Chart)')
ax.legend(loc='upper left')
ax.set_ylabel('Billions of $')
fig.tight_layout()
fig.show()

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

