import sys

def main():
    # Given two arrays of equal length, create a dictionary such that element 0 in keys is the key to value of element 0 in values
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    result = dict()
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    print(result)

    # Loop through each of the keys=>values in the dict
    for key in result:
        print(key + " => " + str(result[key]))

if __name__ == "__main__":
    main()