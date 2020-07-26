#Tomer Paz 315311365
#Topaz Tcherkafs 206867871

import cloudpickle
import base64
import sys
import csv
import math

inFile = sys.argv[1]
outFile = sys.argv[2]
funcString = 'gAWV9AQAAAAAAACMF2Nsb3VkcGlja2xlLmNsb3VkcGlja2xllIwNX2J1aWx0aW5fdHlwZZSTlIwKTGFtYmRhVHlwZZSFlFKUKGgCjAhDb2RlVHlwZZSFlFKUKEt4SwBLAEt4SwNLQ0MKdAB8WXwdgwJTAJROhZSMAmx0lIWUKIwDSU4wlIwDSU4xlIwDSU4ylIwDSU4zlIwDSU40lIwDSU41lIwDSU42lIwDSU43lIwDSU44lIwDSU45lIwESU4xMJSMBElOMTGUjARJTjEylIwESU4xM5SMBElOMTSUjARJTjE1lIwESU4xNpSMBElOMTeUjARJTjE4lIwESU4xOZSMBElOMjCUjARJTjIxlIwESU4yMpSMBElOMjOUjARJTjI0lIwESU4yNZSMBElOMjaUjARJTjI3lIwESU4yOJSMBElOMjmUjARJTjMwlIwESU4zMZSMBElOMzKUjARJTjMzlIwESU4zNJSMBElOMzWUjARJTjM2lIwESU4zN5SMBElOMziUjARJTjM5lIwESU40MJSMBElONDGUjARJTjQylIwESU40M5SMBElONDSUjARJTjQ1lIwESU40NpSMBElONDeUjARJTjQ4lIwESU40OZSMBElONTCUjARJTjUxlIwESU41MpSMBElONTOUjARJTjU0lIwESU41NZSMBElONTaUjARJTjU3lIwESU41OJSMBElONTmUjARJTjYwlIwESU42MZSMBElONjKUjARJTjYzlIwESU42NJSMBElONjWUjARJTjY2lIwESU42N5SMBElONjiUjARJTjY5lIwESU43MJSMBElONzGUjARJTjcylIwESU43M5SMBElONzSUjARJTjc1lIwESU43NpSMBElONzeUjARJTjc4lIwESU43OZSMBElOODCUjARJTjgxlIwESU44MpSMBElOODOUjARJTjg0lIwESU44NZSMBElOODaUjARJTjg3lIwESU44OJSMBElOODmUjARJTjkwlIwESU45MZSMBElOOTKUjARJTjkzlIwESU45NJSMBElOOTWUjARJTjk2lIwESU45N5SMBElOOTiUjARJTjk5lIwFSU4xMDCUjAVJTjEwMZSMBUlOMTAylIwFSU4xMDOUjAVJTjEwNJSMBUlOMTA1lIwFSU4xMDaUjAVJTjEwN5SMBUlOMTA4lIwFSU4xMDmUjAVJTjExMJSMBUlOMTExlIwFSU4xMTKUjAVJTjExM5SMBUlOMTE0lIwFSU4xMTWUjAVJTjExNpSMBUlOMTE3lIwFSU4xMTiUjAVJTjExOZR0lIwIPHN0cmluZz6UjAg8bGFtYmRhPpRLAUMAlCkpdJRSlH2UTk5OdJRSlIwcY2xvdWRwaWNrbGUuY2xvdWRwaWNrbGVfZmFzdJSMEl9mdW5jdGlvbl9zZXRzdGF0ZZSTlGiNfZR9lCiMCF9fbmFtZV9flGiHjAxfX3F1YWxuYW1lX1+UaIeMD19fYW5ub3RhdGlvbnNfX5R9lIwOX19rd2RlZmF1bHRzX1+UTowMX19kZWZhdWx0c19flE6MCl9fbW9kdWxlX1+UTowHX19kb2NfX5ROjAtfX2Nsb3N1cmVfX5ROjBdfY2xvdWRwaWNrbGVfc3VibW9kdWxlc5RdlIwLX19nbG9iYWxzX1+UfZRoC4wJX29wZXJhdG9ylIwCbHSUk5RzdYaUhlIwLg=='
func056 = 'gAWVSQ0AAAAAAACMF2Nsb3VkcGlja2xlLmNsb3VkcGlja2xllIwNX2J1aWx0aW5fdHlwZZSTlIwKTGFtYmRhVHlwZZSFlFKUKGgCjAhDb2RlVHlwZZSFlFKUKEt4SwBLAEt4SylLQ0KyBQAAdAB0AXQCdAF0AmQBdAJkAXx3dAJ0AGQCdAF0AnQBdAJ0AXQCZAF8aHx3gwN0A3QCdAF0AnQAZAJ0AXQCdAF0AmQCfHV0AmQBfHV8dYMDgwN0AnQBdAJkAnQCZAF8aHx3gwN8d4MDdAJ0BHxnfHWDAnx3fHWDA4MCfAB0AnQEfGd8dYMCfHd8dYMDgwODAnxofACDA3QCZAF0A3QCdAF0AmQBfGh8d4MDdAJ0BHx1fCCDAnx3fHWDA4MCfAl8d4MDdAV0AnQEfBl8HYMCfHV0AmQBfGh8d4MDgwN8d4MCgwJ0AmQBfDh8dYMDgwODAoMCdAJ0AXQCZAF8aHwfgwN0AnQEdAJ0BHwZfB2DAnx1dAJkAXxofHeDA4MDdAV0AmQBdAN0AnQBdAJkAXQCdAF8d3xxgwJ8cXwggwN8H4MDdAJ0BHxNfHWDAnxzfB+DA4MCdAZ0Bnw7fDiDAnQHfGZ8RYMCgwJ8TYMDfHGDAnx1gwN8dYMCgwJ8d3QCZAF8SHx1gwODA4MCfDh8dYMDfHeDA3xxgwJ8SnwZgwN8cYMCgwJ8dXQCdAF0AnQEfBl0BXQCZAF8cXx1gwN0AmQBdAV0AmQCdAJ0BHwZfB2DAnx1fHeDA3x3gwN8AIMCfHeDA4MCgwJ8aHx3gwN0AnQBdAJkAXwJfB+DA3QCZAF8SHwfgwODAnxIfHWDA4MCfHV8dYMDgwN8d4MCfGh0A3QCdAF0AmQBfGh8d4MDdAJ0BHx1fCCDAnx3fHWDA4MCfAl8d4MDdAV0BXQDfGB8K4MCdAZ8NHxOgwKDAnwhgwKDAoMDdAJ0AXQCZAF0AmQCfHd0AnQEfBl8HYMCfDh8cYMDgwN8d4MDdAJ0AXQCZAF0AnQEfHd8c4MCfHF8dYMDfB+DA3QCdAR8TXx1gwJ8d3wfgwODAnx3fHWDA4MCdAN0AnQBdAJkAXxofHeDA3QCdAR8dXwggwJ8d3x1gwODAnwJfHeDA3QFdAJ0BHwZfB2DAnQFfDd8GIMCdAJkAXxofHeDA4MDfHeDAoMCfHWDA4MCgwJ8H3xxgwODA3x3gwN0AnQBdAJkAXQCdAF8d3xxgwJ8cXx1gwN8H4MDdAJ0BHxNfHWDAnxzfB+DA4MCfHd8dYMDgwJ0AnQEfBl8HYMCfHV8d4MDfHeDA3QCdAF8dXQCdAF0AmQBdAV0AnQEfBl8bYMCdAN0AnQBdAJkAXQCdAR8d3xzgwJ8OHx1gwN8d4MDfHGDAnxKfE2DA3xxgwJ8dYMDdAJ0AGQCdAF0AnQBdAJ0BHQCdAR8GXwdgwJ8dXQCZAF8aHx3gwODA3wdgwJ8dXQCdAF0AnQEfBl0B3x3dAh8X4MBgwKDAnxofHeDA3QCdAF0AmQCfHd8H4MDdAJ0AXQCZAJ8aHx3gwN0AnQBdAJkAnx3fB+DA3QCZAF8SHwfgwODAnxIfHWDA4MCfEh8H4MDgwJ8SHx1gwODAnx1fHWDA4MDdAJ0AXQCZAF0AmQBfGh8d4MDfHeDA3QCdAR8Z3x1gwJ8d3x1gwODAnx1dAJ0BHwZfB2DAnx3fHWDA4MDgwJ8aHwAgwN0AmQBdAN0AnQBdAJkAXxofHeDA3QCdAR8dXwggwJ8d3x1gwODAnwJfHeDA3QFdAJ0BHwZfB2DAnx1dAJkAXxofHeDA4MDfHeDAoMCdAJkAXw4fHWDA4MDgwKDAnQFfEp8AIMCfHeDA4MCfB+DA3QCZAF8TXwfgwODAnxIfHWDA4MCdAJ0AXQCdAR8GXxtgwJ8aHx3gwN0AnQBdAJ0BHx3fHODAnwJfB+DA3QCZAF8SHwfgwODAnxNfHWDA4MCdAJ0BHwZfB2DAnx1fHeDA3x3gwN8dYMDgwJ0AXQCdAR8AXwFgwJ8dXQCZAJ0AnQEfCF8HYMCfHV8d4MDfHeDA4MDdAJ0BHx3fHODAnQCZAF8aHx3gwN8dYMDgwKDAlMAlE6JiIeUKIwEYW5kX5SMAmx0lIwMaWZfdGhlbl9lbHNllIwDbXVslIwCZXGUjANzdWKUjAxwcm90ZWN0ZWREaXaUjANhZGSUjANzaW6UdJQojANJTjCUjANJTjGUjANJTjKUjANJTjOUjANJTjSUjANJTjWUjANJTjaUjANJTjeUjANJTjiUjANJTjmUjARJTjEwlIwESU4xMZSMBElOMTKUjARJTjEzlIwESU4xNJSMBElOMTWUjARJTjE2lIwESU4xN5SMBElOMTiUjARJTjE5lIwESU4yMJSMBElOMjGUjARJTjIylIwESU4yM5SMBElOMjSUjARJTjI1lIwESU4yNpSMBElOMjeUjARJTjI4lIwESU4yOZSMBElOMzCUjARJTjMxlIwESU4zMpSMBElOMzOUjARJTjM0lIwESU4zNZSMBElOMzaUjARJTjM3lIwESU4zOJSMBElOMzmUjARJTjQwlIwESU40MZSMBElONDKUjARJTjQzlIwESU40NJSMBElONDWUjARJTjQ2lIwESU40N5SMBElONDiUjARJTjQ5lIwESU41MJSMBElONTGUjARJTjUylIwESU41M5SMBElONTSUjARJTjU1lIwESU41NpSMBElONTeUjARJTjU4lIwESU41OZSMBElONjCUjARJTjYxlIwESU42MpSMBElONjOUjARJTjY0lIwESU42NZSMBElONjaUjARJTjY3lIwESU42OJSMBElONjmUjARJTjcwlIwESU43MZSMBElONzKUjARJTjczlIwESU43NJSMBElONzWUjARJTjc2lIwESU43N5SMBElONziUjARJTjc5lIwESU44MJSMBElOODGUjARJTjgylIwESU44M5SMBElOODSUjARJTjg1lIwESU44NpSMBElOODeUjARJTjg4lIwESU44OZSMBElOOTCUjARJTjkxlIwESU45MpSMBElOOTOUjARJTjk0lIwESU45NZSMBElOOTaUjARJTjk3lIwESU45OJSMBElOOTmUjAVJTjEwMJSMBUlOMTAxlIwFSU4xMDKUjAVJTjEwM5SMBUlOMTA0lIwFSU4xMDWUjAVJTjEwNpSMBUlOMTA3lIwFSU4xMDiUjAVJTjEwOZSMBUlOMTEwlIwFSU4xMTGUjAVJTjExMpSMBUlOMTEzlIwFSU4xMTSUjAVJTjExNZSMBUlOMTE2lIwFSU4xMTeUjAVJTjExOJSMBUlOMTE5lHSUjAg8c3RyaW5nPpSMCDxsYW1iZGE+lEsBQwCUKSl0lFKUfZROTk50lFKUjBxjbG91ZHBpY2tsZS5jbG91ZHBpY2tsZV9mYXN0lIwSX2Z1bmN0aW9uX3NldHN0YXRllJOUaJV9lH2UKIwIX19uYW1lX1+UaI+MDF9fcXVhbG5hbWVfX5Roj4wPX19hbm5vdGF0aW9uc19flH2UjA5fX2t3ZGVmYXVsdHNfX5ROjAxfX2RlZmF1bHRzX1+UTowKX19tb2R1bGVfX5ROjAdfX2RvY19flE6MC19fY2xvc3VyZV9flE6MF19jbG91ZHBpY2tsZV9zdWJtb2R1bGVzlF2UjAtfX2dsb2JhbHNfX5R9lChoEowJX29wZXJhdG9ylIwDYWRklJOUaA5oqIwDbXVslJOUaBOMCm51bXB5LmNvcmWUjBJfdWZ1bmNfcmVjb25zdHJ1Y3SUk5SMHG51bXB5LmNvcmUuX211bHRpYXJyYXlfdW1hdGiUjANzaW6UhpRSlGgMaKiMAmx0lJOUaBBoqIwDc3VilJOUaA1oBShoCChLA0sASwBLA0sBS0NDEHwAcgh8AVMAfAJTAGQAUwCUToWUKYwFaW5wdXSUjAdvdXRwdXQxlIwHb3V0cHV0MpSHlIwrQzovVXNlcnMvVXNlci9QeWNoYXJtUHJvamVjdHMvRXZvMk5ldy9HUC5weZRoDUuNQwYAAQQABAGUKSl0lFKUfZQojAtfX3BhY2thZ2VfX5ROaJuMCF9fbWFpbl9flIwIX19maWxlX1+UjCtDOi9Vc2Vycy9Vc2VyL1B5Y2hhcm1Qcm9qZWN0cy9Fdm8yTmV3L0dQLnB5lHVOTk50lFKUaJhoyH2UfZQoaJtoDWicaA1onX2UaJ9OaKBOaKFoxGiiTmijTmikXZRopn2UdYaUhlIwaA9oqIwCZXGUk5RoC2iojARhbmRflJOUaBFoBShoCChLAksASwBLAksIS0NDJnoKfAB8ARsAVwBTAAQAdABrCnIgAQABAAEAWQBkAVMAWABkAFMAlE5LAYaUjBFaZXJvRGl2aXNpb25FcnJvcpSFlIwEbGVmdJSMBXJpZ2h0lIaUaL5oEUuIQwgAAQIACgEOAJQpKXSUUpRowk5OTnSUUpRomGjefZR9lChom2gRaJxoEWidfZRon05ooE5ooWjEaKJOaKNOaKRdlGimfZR1hpSGUjB1dYaUhlIwLg=='

COL1_AVG = 3618.046
COL1_SD = 13129.675
COL2_AVG = 99.979
COL2_SD = 0.159
COL3_AVG = 3778.947
COL3_SD = 16734.940
COL4_AVG = 100.017
COL4_SD = 0.158


def str2lambda(string):
    b = base64.b64decode(string)
    exp = cloudpickle.loads(b)
    return exp

def normalization(data, deepnessRows):
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

def makePredictionFileFromTestInput(func):
    data = []
    with open(inFile) as data_file:
        data_reader = csv.reader(data_file)
        row_count = sum(1 for row in data_reader)
    with open(inFile) as data_file:
        data_reader = csv.reader(data_file)
        for i in range(row_count):
            row = data_reader.__next__()
            row[0] = 2
            data.append(list(float(elem) for elem in row))
    dataNorm = normalization(data, row_count)
    # Evaluate labels
    if len(dataNorm[0]) == 121:
        result = [bool(func(*mail[1:])) for mail in dataNorm]
    else:
        raise (f'enexpected length! {len(dataNorm[0])}')
    with open(outFile,'w') as f:
        for i in range(row_count):
            resI = result[i]
            f.write(str(int(resI)))
            if(i != (row_count -1)):
                f.write('\n')

def main():
    # get chosen function
    func = str2lambda(funcString)
    with open('dataset/validate.csv') as data_file:
        data_reader = csv.reader(data_file)
        dataBeforeNorm = []
        for i in range(50000):
            row = data_reader.__next__()
            dataBeforeNorm.append(list(float(elem) for elem in row))
    data = normalization(dataBeforeNorm, 50000)
    if len(data[0]) == 121:
        result = [bool(func(*mail[1:])) for mail in data]
    else:
        raise (f'enexpected length! {len(data[0])}')
    size = len(result)
    if True:  # Prediction by validate - data
        TP = 0
        TN = 0
        FP = 0
        FN = 0
        for i in range(size):
            resI = result[i]
            valI = data[i][0]
            if (resI == True and valI == 1):
                TP += 1
            if (resI == False and valI == 0):
                TN += 1
            if (resI == True and valI == 0):
                FP += 1
            if (resI == False and valI == 1):
                FN += 1
        print(f'TP = {TP} FP = {FP} TN = {TN} FN = {FN}')
        accuracy = (TP + TN) / (TP + FP + TN + FN)
        precision = (TP) / (TP + FP)
        recall = (TP) / (TP + FN)
        beta = 0.25
        betaPowed = math.pow(beta, 2)
        fb = (1 + betaPowed) * ((precision * recall) / ((betaPowed * precision) + recall))
        print(f'Accuracy = {accuracy}\nPrecision = {precision}\n'
              f'Recall = {recall}\n'
              f'F0.25 = {fb}')
    makePredictionFileFromTestInput(func)

if __name__ == "__main__":
    main()
