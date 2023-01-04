import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import csv

filename = 'crawl_tweets.csv'

fh = open(filename, 'r', encoding='utf-8', errors='ignore')
csvreader = csv.reader(fh)

csv_header = next(csvreader)
lst_dt_csv = next(csvreader)

dt_csv = np.array(list(map(datetime.fromisoformat, lst_dt_csv[1:3])))
lst_fs = next(csvreader)
np_d_fs = np.array(list(map(str, lst_fs[1:3])))
fh.close()
df_sig = pd.read_csv(filename, header=None, skiprows=5, names=csv_header)

df_sig.CH1.plot()
plt.xlabel('sample number')
plt.ylabel('crawling data')