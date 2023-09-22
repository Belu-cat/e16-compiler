exeptions = ["(", ")", "'", '"', "="]
keywords = ["int", "="]

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
            elif x in keywords:
                types.append("keyword")
            else:
                types.append("val")
        elif type(x) is int:
            types.append("integer")
        elif type(x) is float:
            types.append("float")
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