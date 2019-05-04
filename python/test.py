import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../emonxcsv.csv", index_col = 0)
data.plot()
print(plt.show())