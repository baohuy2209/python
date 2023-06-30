with open('fileinteger.txt','w') as fileobj:
    fileobj.write('tomato \n pasta \n garlic')
with open('fileinteger.txt') as obj:
    # This method make a list where each line
    lines = obj.readline()

print(lines)

with open('fileinteger.txt','r') as obj:
    lines = []
    for line in obj:
        lines.append(line.strip())

print(lines)