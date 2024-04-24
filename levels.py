
#Benjamin Niccum
#1002111609
#04/24/24


depthNum = 0
quote = 0
comment = 0
file = "example.txt"
with open(file, "r") as file:
    for line in file:
        for char in line:
            if comment > 1:
                comment = 0
                break
            if char == '"':
                if quote == 0:
                    quote += 1
                    break
                else:
                    quote -= 1
                    break
            if char == '/':
                comment +=1
                break
            if char == "{":
                depthNum += 1
            elif char == "}":
                depthNum -= 1
        print(str(depthNum) + " " + line)
