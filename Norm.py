import csv

# standard
COL1_AVG = 3512.0527729
COL1_SD = 12683.73537
COL2_AVG = 99.98126338
COL2_SD = 0.0156
COL3_AVG = 3677.905554
COL3_SD = 15184.67272
COL4_AVG = 100.0187626
COL4_SD = 0.065


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
