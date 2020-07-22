#Tomer Paz 315311365
#Topaz Tcherkafs 206867871

import csv
import math

# standard
COL1_AVG = 3618.046
COL1_SD = 13129.675
COL2_AVG = 99.979
COL2_SD = 0.159
COL3_AVG = 3778.947
COL3_SD = 16734.940
COL4_AVG = 100.017
COL4_SD = 0.158

#eli way to preNorm
# def preNorm(deepnessRows=700000):
#     data = []
#     with open('dataset/train.csv') as data_file:
#         data_file = csv.reader(data_file)
#         for i in range(deepnessRows):
#             data.append(list(float(elem) for elem in (data_file.__next__()[1:])))
#     asum = 0
#     bsum = 0
#     csum = 0
#     dsum = 0
#     for i in range(deepnessRows):
#         for j in range(120):
#             if j % 4 == 0:
#                 asum = (asum + data[i][j])
#             elif j % 4 == 1:
#                 bsum = (bsum + data[i][j])
#             elif j % 4 == 2:
#                 csum = (csum + data[i][j])
#             elif j % 4 == 3:
#                 dsum = (dsum + data[i][j])
#     numOfABCD = deepnessRows*30
#     meana = asum/numOfABCD
#     meanb = bsum/numOfABCD
#     meanc = csum/numOfABCD
#     meand = dsum/numOfABCD
#     sumSDA = 0
#     sumSDB = 0
#     sumSDC = 0
#     sumSDD = 0
#     for i in range(deepnessRows):
#         for j in range(120):
#             if j % 4 == 0:
#                 sumSDA = (sumSDA + math.pow((data[i][j] - meana),2))
#             elif j % 4 == 1:
#                 sumSDB = (sumSDB + math.pow((data[i][j] - meanb),2))
#             elif j % 4 == 2:
#                 sumSDC = (sumSDC + math.pow((data[i][j] - meanc),2))
#             elif j % 4 == 3:
#                 sumSDD = (sumSDD + math.pow((data[i][j] - meand),2))
#     finalSDA = math.sqrt((sumSDA/numOfABCD))
#     finalSDB = math.sqrt((sumSDB/numOfABCD))
#     finalSDC = math.sqrt((sumSDC/numOfABCD))
#     finalSDD = math.sqrt((sumSDD/numOfABCD))
#     print(f'mean_a = {meana}\n'
#           f'stdev_a = {finalSDA}\n'
#           f'mean_b = {meanb}\n'
#           f'stdev_b = {finalSDB}\n'
#           f'mean_c = {meanc}\n'
#           f'stdev_c = {finalSDC}\n'
#           f'mean_d = {meand}\n'
#           f'stdev_d = {finalSDD}')


# standard normalization
def normalization(data, deepnessRows=700000):
    new_data = []
    for i in range(deepnessRows):
        new_data.append([0] * len(data[0]))
        for j in range(len(data[0])):
            # skips the label
            if j == 0:
                new_data[i][j] = data[i][j]
                continue
            if j % 4 == 1:
                new_data[i][j] = (data[i][j] - COL1_AVG) / COL1_SD
            elif j % 4 == 2:
                new_data[i][j] = (data[i][j] - COL2_AVG) / COL2_SD
            elif j % 4 == 3:
                new_data[i][j] = (data[i][j] - COL3_AVG) / COL3_SD
            else:
                new_data[i][j] = (data[i][j] - COL4_AVG) / COL4_SD

    return new_data


# min-max normalization
def min_max_normalization(data, deepnessRows=700000):
    new_data = []

    # find min max
    max_arr = [0] * (len(data[0]) - 1)
    min_arr = [0] * (len(data[0]) - 1)
    for j in range(len(data[0])):
        if j == 0:
            continue
        min_val = data[0][j]
        max_val = data[0][j]
        for i in range(deepnessRows):
            if data[i][j] > max_val:
                max_val = data[i][j]
            if data[i][j] < min_val:
                min_val = data[i][j]
        max_arr[j - 1] = max_val
        min_arr[j - 1] = min_val

    for i in range(deepnessRows):
        new_data.append([0] * len(data[i]))
        for j in range(len(data[i])):
            # skips the label
            if j == 0:
                new_data[i][j] = data[i][j]
                continue
            print(data[i][j] - min_arr[j - 1])
            print((max_arr[j - 1] - min_arr[j - 1]))
            new_data[i][j] = (data[i][j] - min_arr[j - 1]) / (
                        max_arr[j - 1] - min_arr[j - 1])

    return new_data


def normalization2(data, deepnessRows=700000):
    new_data = []
    for i in range(0,25000):
        new_data.append([0] * len(data[0]))
        for j in range(len(data[0])):
            # skips the label
            if j == 0:
                new_data[i][j] = data[i][j]
                continue
            if j % 4 == 1:
                new_data[i][j] = (data[i][j] - COL1_AVG) / COL1_SD
            elif j % 4 == 2:
                new_data[i][j] = (data[i][j] - COL2_AVG) / COL2_SD
            elif j % 4 == 3:
                new_data[i][j] = (data[i][j] - COL3_AVG) / COL3_SD
            else:
                new_data[i][j] = (data[i][j] - COL4_AVG) / COL4_SD

    return new_data