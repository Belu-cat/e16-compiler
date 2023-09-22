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
        
    for x in tokens:
        if type(x) is list:
            types.append("list")
        elif type(x) is str:
            if x == "(":
                types.append("openPar")
            elif x == ")":
                types.append("closePar")
            else:
                types.append("string")
        elif type(x) is int:
            types.append("integer")
        elif type(x) is float:
            types.append("float")
    return [tokens, types]