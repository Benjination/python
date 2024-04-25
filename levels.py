
#Benjamin Niccum
#1002111609
#04/24/24


depthNum = 0
quote = False
comment = 0
silent = False
file = "example.txt"
with open(file, "r") as file:
    for line in file:                          #Checks each line one at a a time
        index = -1                             #Starts -1 at each line start and iterates to 0 for first char
        for char in line:                      #Checks each char in line
            index += 1
            if char == '*':                    #Could be the first symbol of unsilence
                if line[index + 1] == '/':     #Checks if next symbol unsilences
                    silent = False             #Sets silent to false if conditions are met
                    break                      #Breaks to next char in line
            if comment > 1:                    #Checks if // is active for line
                comment = 0                    #Resets comment
                break                          #Breaks to new line
            if char == '"':                    #Checks if symbol is begin or end of quote
                if quote == False:             #If false, is beginning of quote
                    quote = True               #Sets quote to true
                    break                      #Breaks to next character in line
                else:                          #If True, is the end of a quote
                    quote = False              #Sets quote to False
                    break                      #Breaks to next char in line
            if char == '/':                    #Could be the beginning of // or /*
                if line[index + 1] == '/':     #is the beginning of a comment
                    comment +=1                #Comment is set to 1 for first / or 2 for second /
                    break                      #breaks to next char in line
                if line[index + 1] == '*':     #Checks if this is the beginning of /* silent 
                    silent = True              #Sets silent to True
                    break                      #Breaks to new char in line
            if char == "{" and silent == False:
                depthNum += 1
            elif char == "}" and silent == False:
                depthNum -= 1
        print(str(depthNum) + " " + line)
