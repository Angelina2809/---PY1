import json
INPUT_FILE = "input.csv"
def csv_to_list_dict(f):
    result = []
    columnName = []
    file = open(f, "r")
    for i in list(file.readline()[:-1].split(" , ")):
        columnName.append(i)
    s = file.readline()
    while s != "":
        l = {}
        values = list(s[:-1].split(" , "))
        for i in range(len(values)):
            l[columnName[i]] = values[i]
        result.append(l)
        s = file.readline()
    file.close()
    return result
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
