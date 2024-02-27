import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    plt.figure(figsize=(14, 16))
    sns.set()
    sns.set_palette("husl")
    x_values = ["Scrambled Legs","Croissant Crawl","Morocco", "First Pollo Bar", "Comedy Club Date",
                "St Christopher's", "Oxford Weekend", "BFT Day", "Pub Quiz", "Second Hyrox Session",
                "Bingo Night", "4th of Feb in Victoria", "F45 with Sam", "Kate's Birthday",
                "Cabin in the Woods", "" , "", "", "", "", "", "", "", "", ""
                ,"Bolton", "", "", "", "Love Trails", "", "", "", "Hyrox Doubles"]
    allVladYValues = np.zeros_like(x_values) # create list of zeros
    vladYValues = [0, 10, 20, 40, 50, 60, 70, 90, 95, 100, 99, 101]
    allVladYValues[:12] = vladYValues[:12]
    allVladYValues[12:] = [0 for value in allVladYValues[12:]]
    plt.xticks(rotation=40, ha='right')
    plt.xlabel('t', fontsize=14)
    plt.ylabel('f', fontsize=14)
    plt.tight_layout()
    plt.grid(True)
    print(allVladYValues)
    plt.plot(x_values, allVladYValues)

    plt.subplots_adjust(bottom=0.3)
    plt.show()

    print('hello')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
