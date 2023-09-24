exeptions = ["(", ")", "'", '"', "=", ";", "{", "}"]
keywords = ["int", "=", "func", "printc", "printa", "var", "char"]

def lexer(text):
    tokens = []
    types = []
    temp = ""
    for x in text:
        if x == " ":
            try:
               temp = int(temp)
            except ValueError:
                try:
                    temp = float(temp)
                except ValueError:
                    pass
            tokens.append(temp)
            temp = ""
        elif x in exeptions:
            try:
               temp = int(temp)
            except ValueError:
                try:
                    temp = float(temp)
                except ValueError:
                    pass
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
            elif x == ";":
                types.append("endLine")
            elif x in keywords:
                types.append("keyword")
            else:
                types.append("val")
        elif type(x) is int:
            types.append("integer")
        elif type(x) is float:
            types.append("float")
    
    i = 0
    while i != len(tokens):
        if tokens[i] == "":
            del tokens[i]
            del types[i]
        else:
            i += 1
    return [tokens, types]

# def parser(lexer):
#     tokens = lexer[0]
#     types = lexer[1]
#     parsedTokens = []
#     parsedTypes = []
#     i = -1
#     while i != len(tokens):
#         if types[i] == "keyword":
#             if tokens[i] == "int":
#                 parsedTokens.append(["int"])
#         elif types[i] == "val":
#             try:
#                 if parsedTokens[len(parsedTokens)][0] == "int":
#                   parsedTokens[len(parsedTokens)].append(tokens[i])
#             except IndexError:
#                 pass
#         elif types[i] == "integer":
#             try:
#                 if parsedTokens[len(parsedTokens)][0] == "int":
#                   parsedTokens[len(parsedTokens)].append(tokens[i])
#             except IndexError:
#                 pass
#         i += 1
#     return [parsedTokens, parsedTypes]

def parser(lexer):
    tokens = lexer[0]
    types = lexer[1]
    parsedTokens = {}
    parsedTypes = {}
    i = 0
    while i != len(tokens):
        temp1 = types[i] == "keyword"
        temp2 = tokens[i] == "func"
        if temp1 & temp2:
            funcName = tokens[i + 1]
            parsedTokens[funcName] = []
            i += 3
            while tokens[i] != "}":
                temp1 = tokens[i] != "="
                # temp2 = types[i] != "keyword"
                if temp1:
                    parsedTokens[funcName].append(tokens[i])
                i += 1
        i += 1
    i = 0
    countedFunction = []
    newFunction = []
    # while i != len(parsedTokens["_main"]):
    #     temp1 = tokens[i] == ";"
    #     temp2 = types[i] == "endLine"
    #     if temp1 & temp2:
    #         newFunction.append(countedFunction)
    #         countedFunction = []
    #     else:
    #         countedFunction.append(parsedTokens["_main"][i])
    #     i += 1
    # parsedTokens["_main"] = newFunction
    for x in parsedTokens["_main"]:
        if x == ";":
            newFunction.append(countedFunction)
            countedFunction = []
        else:
            countedFunction.append(x)
    parsedTokens["_main"] = newFunction
    return parsedTokens

def variableValue(variables, value):
    if str(value) in variables:
        return variables[str(value)]
    else:
        return value

def compile(parsed):
    parsedTokens = parsed
    variables = {}
    compilied = ""
    chartable = ["return", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "`", "~", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", "\\", "|", ";", ":", "'", "\"", ",", "<", ".", ">", "/", "?"]
    for x in parsedTokens["_main"]:
        temp1 = x[0] == "var"
        temp2 = x[0] == "int"
        if temp2 | temp1:
            variables[x[1]] = len(variables) + 1
            ramLoc = variables[x[1]]
            compilied += "mov $" + str(ramLoc) + " " + str(x[2]) + "\n"
        elif x[0] == "printc":
            compilied += "mov @a " + str(variableValue(variables, x[1])) + "\nint 0x3\n"
        elif x[0] == "printa":
            compilied += "int 0x4\n"
        elif x[0] == "char":
            variables[x[1]] = len(variables) + 1
            ramLoc = variables[x[1]]
            compilied += "mov $" + str(ramLoc) + " " + str(chartable.index(x[2]) + 1) + "\n"
    return compilied