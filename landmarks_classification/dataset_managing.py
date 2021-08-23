import pandas as pd
import numpy as np
import math

#Loading the data
spread = pd.read_csv("dataset_spread.csv", header = None)
fist = pd.read_csv("dataset_fist.csv", header = None)
peace = pd.read_csv("dataset_peace.csv", header = None)
rocknroll = pd.read_csv("dataset_rocknroll.csv", header = None)

#Giving to each gesture the same number of instances

min_size = min(spread.shape[0], fist.shape[0], peace.shape[0], rocknroll.shape[0])
spread = spread.loc[:min_size-1, :]
fist = fist.loc[:min_size-1, :]
peace = peace.loc[:min_size-1, :]
rocknroll = rocknroll.loc[:min_size-1, :]

#Regrouping the gestures instances into one dataset

dataset = pd.concat([spread, fist, peace, rocknroll], axis= 0)

#Saving the dataset
#np.savetxt('vec_dataset.csv',vec_dataset, delimiter=',')

#Turning landmarks into Normalized Vectors
vec_dataset = []
for index, row in dataset.iterrows():
    line = []
    save_line = True
    for j in range(0,42,2):
        if(j in [10, 18, 26, 34]):
            div = math.sqrt((row.iloc[j] - row.iloc[0])**2 + (row.iloc[j + 1] - row.iloc[1])**2)
            if(div!=0):
                line.append((row.iloc[j] - row.iloc[0]) / div)
                line.append((row.iloc[j + 1] - row.iloc[1]) / div)
            else:
                save_line = False
                break
        if(j not in [8, 16, 24, 32, 40]):
            div = math.sqrt((row.iloc[j+2] - row.iloc[j])**2 + (row.iloc[j + 3] - row.iloc[j+1])**2)
            if (div != 0):
                line.append((row.iloc[j+2] - row.iloc[j]) / div)
                line.append((row.iloc[j+3] - row.iloc[j+1]) / div)
            else:
                save_line = False
                break
    if save_line:
        line.append(row.iloc[-1])
        vec_dataset.append(line)
vec_dataset = np.vstack(vec_dataset)

#Saving the dataset
#np.savetxt('vec_dataset.csv',vec_dataset, delimiter=',')





