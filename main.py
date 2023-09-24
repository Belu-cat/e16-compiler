import lexerparser as lexer
import sys
if len(sys.argv) > 1:
    xyz = sys.argv[1] + ".e16"
    zyx = sys.argv[1] + ".txt"
else:
    xyz = "input.e16"
    zyx = "compilied.txt"
f = open(xyz)
# lexed = lexer.lexer("func _main { printc 2; printa; };")
input = f.read()
input = input.replace("\n", "")
input = input.strip()
lexed = lexer.lexer(input)
f.close()
# print(lexed)
parsed = lexer.parser(lexed)
# print(parsed)
compiled = lexer.compile(parsed)
# print(compiled)
f = open(zyx, "w")
f.write(compiled)
f.close()
print("Program '" + xyz + "' has been compilied to '" + zyx + "'")