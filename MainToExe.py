#Tomer Paz 315311365
#Topaz Tcherkafs 206867871

import cloudpickle
import base64
import sys
import csv

inFile = sys.argv[1]
outFile = sys.argv[2]
funcString = 'gAWV9AQAAAAAAACMF2Nsb3VkcGlja2xlLmNsb3VkcGlja2xllIwNX2J1aWx0aW5fdHlwZZSTlIwKTGFtYmRhVHlwZZSFlFKUKGgCjAhDb2RlVHlwZZSFlFKUKEt4SwBLAEt4SwNLQ0MKdAB8WXwdgwJTAJROhZSMAmx0lIWUKIwDSU4wlIwDSU4xlIwDSU4ylIwDSU4zlIwDSU40lIwDSU41lIwDSU42lIwDSU43lIwDSU44lIwDSU45lIwESU4xMJSMBElOMTGUjARJTjEylIwESU4xM5SMBElOMTSUjARJTjE1lIwESU4xNpSMBElOMTeUjARJTjE4lIwESU4xOZSMBElOMjCUjARJTjIxlIwESU4yMpSMBElOMjOUjARJTjI0lIwESU4yNZSMBElOMjaUjARJTjI3lIwESU4yOJSMBElOMjmUjARJTjMwlIwESU4zMZSMBElOMzKUjARJTjMzlIwESU4zNJSMBElOMzWUjARJTjM2lIwESU4zN5SMBElOMziUjARJTjM5lIwESU40MJSMBElONDGUjARJTjQylIwESU40M5SMBElONDSUjARJTjQ1lIwESU40NpSMBElONDeUjARJTjQ4lIwESU40OZSMBElONTCUjARJTjUxlIwESU41MpSMBElONTOUjARJTjU0lIwESU41NZSMBElONTaUjARJTjU3lIwESU41OJSMBElONTmUjARJTjYwlIwESU42MZSMBElONjKUjARJTjYzlIwESU42NJSMBElONjWUjARJTjY2lIwESU42N5SMBElONjiUjARJTjY5lIwESU43MJSMBElONzGUjARJTjcylIwESU43M5SMBElONzSUjARJTjc1lIwESU43NpSMBElONzeUjARJTjc4lIwESU43OZSMBElOODCUjARJTjgxlIwESU44MpSMBElOODOUjARJTjg0lIwESU44NZSMBElOODaUjARJTjg3lIwESU44OJSMBElOODmUjARJTjkwlIwESU45MZSMBElOOTKUjARJTjkzlIwESU45NJSMBElOOTWUjARJTjk2lIwESU45N5SMBElOOTiUjARJTjk5lIwFSU4xMDCUjAVJTjEwMZSMBUlOMTAylIwFSU4xMDOUjAVJTjEwNJSMBUlOMTA1lIwFSU4xMDaUjAVJTjEwN5SMBUlOMTA4lIwFSU4xMDmUjAVJTjExMJSMBUlOMTExlIwFSU4xMTKUjAVJTjExM5SMBUlOMTE0lIwFSU4xMTWUjAVJTjExNpSMBUlOMTE3lIwFSU4xMTiUjAVJTjExOZR0lIwIPHN0cmluZz6UjAg8bGFtYmRhPpRLAUMAlCkpdJRSlH2UTk5OdJRSlIwcY2xvdWRwaWNrbGUuY2xvdWRwaWNrbGVfZmFzdJSMEl9mdW5jdGlvbl9zZXRzdGF0ZZSTlGiNfZR9lCiMCF9fbmFtZV9flGiHjAxfX3F1YWxuYW1lX1+UaIeMD19fYW5ub3RhdGlvbnNfX5R9lIwOX19rd2RlZmF1bHRzX1+UTowMX19kZWZhdWx0c19flE6MCl9fbW9kdWxlX1+UTowHX19kb2NfX5ROjAtfX2Nsb3N1cmVfX5ROjBdfY2xvdWRwaWNrbGVfc3VibW9kdWxlc5RdlIwLX19nbG9iYWxzX1+UfZRoC4wJX29wZXJhdG9ylIwCbHSUk5RzdYaUhlIwLg=='

def str2lambda(string):
    b = base64.b64decode(string)
    exp = cloudpickle.loads(b)
    return exp

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
    # Evaluate labels
    if len(data[0]) == 121:
        result = [bool(func(*mail[1:])) for mail in data]
    else:
        raise (f'enexpected length! {len(data[0])}')
    with open(outFile,'w') as f:
        for i in range(row_count):
            resI = result[i]
            f.write(str(int(resI)))
            if(i != (row_count -1)):
                f.write('\n')

def main():
    # get chosen function
    func = str2lambda(funcString)
    makePredictionFileFromTestInput(func)

if __name__ == "__main__":
    main()
