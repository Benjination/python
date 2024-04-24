
#Benjamin Niccum
#1002111609
#04/24/24


cnt = 0
cnt2 = 0
cnt3 = 0
file = "example.txt"
with open(file, "r") as file:
    for line in file:
        for char in line:
            if cnt3 > 1:
                cnt3 = 0
                break
            if char == '"':
                if cnt2 == 0:
                    cnt2 += 1
                    break
                else:
                    cnt2 -= 1
                    break
            if char == '/':
                cnt3 +=1
                break
            if char == "{":
                cnt += 1
            elif char == "}":
                cnt -= 1
        print(str(cnt) + " " + line)
