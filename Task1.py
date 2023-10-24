lst = list(input("Input List of Digits (seperated by commas): "))

str = ''
for i in lst:
    if i == ',':
        continue
    else:
        str += i

print(str)
