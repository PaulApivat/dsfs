# coding: utf-8

# NOTE: this will create a new text file
with open('tab_delimited_stock_prices.txt', 'w') as f:
    f.write("""6/20/2014\tAAPL\t90.91
6/20/2014\tMSFT\t41.68
6/20/2014\tFB\t64.5
6/19/2014\tAAPL\t91.86
6/19/2014\tMSFT\t41.51
6/19/2014\tFB\t64.34
""")

# this will read that text file and print to console
with open('tab_delimited_stock_prices.txt') as file:
    text = file.read()
print(text)
