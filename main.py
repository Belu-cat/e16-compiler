import lexerparser as lexer
lexed = lexer.lexer("func _main { int hello = 12; };")
print(lexed)
print(lexer.parser(lexed))
print(lexer.exeptions)
print(lexer.keywords)