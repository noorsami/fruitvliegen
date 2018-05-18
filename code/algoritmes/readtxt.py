file = open("Output.txt", "r")

data = file.read()

data = data.split("),")

for line in data:
    print(line)

print(len(data))
file.close()