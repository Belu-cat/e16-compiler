import lexerparser as lexer
f = open("input.e16")
# lexed = lexer.lexer("func _main { printc 2; printa; };")
input = f.read()
lexed = lexer.lexer(input.replace("\n", ""))
f.close()
print(lexed)
parsed = lexer.parser(lexed)
print(parsed)
compiled = lexer.compile(parsed)
print(compiled)
f = open("compilied.txt", "w")
f.write(compiled)
f.close()