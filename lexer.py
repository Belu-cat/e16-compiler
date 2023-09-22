def lexer(text):
    tokens = []
    types = []
    temp = ""
    exeptions = ["(", ")"]
    for x in text:
        if x == " ":
            tokens.append(temp)
            temp = ""
        elif x in exeptions:
            tokens.append(temp)
            tokens.append(x)
            temp = ""
        else:
            temp = temp + x
        
    return tokens