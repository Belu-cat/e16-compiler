import lexerparser as lexer
lexed = lexer.lexer("func _main { int hello = 12; int hello2 = 34; };")
print(lexed)
print(lexer.parser(lexed))