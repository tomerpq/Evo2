import random
import cloudpickle
import base64


def str2lambda(string):
    b = base64.b64decode(string)
    exp = cloudpickle.loads(b)
    return exp

def main():
    random.seed(10)
    # get chosen function
    file = open("function.txt", "r")
    func = str2lambda(file.read())
    print(func)


if __name__ == "__main__":
    main()
