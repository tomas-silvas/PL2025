import sys

def rec_inteiros(linha):
    inteiros = ""
    sum = 0
    on_str = "On"
    off_str = ""
    for char in linha:
        if on_str == "On":
            if off_str == "" and char.lower() == 'o':
                off_str = "O"
            elif off_str == "O" and char.lower() == 'f':
                off_str = "Of"
            elif off_str == "Of" and char.lower() == 'f':
                off_str = "Off"
                on_str = ""
            elif char == '=':
                if inteiros:
                    sum += int(inteiros)
                print(sum)
                inteiros = ""
            elif char.isdigit():
                inteiros += char
            elif not char.isdigit():
                if inteiros:
                    sum += int(inteiros)
                    inteiros = ""
                    
        elif off_str == "Off":
            if on_str == "" and char.lower() == 'o':
                on_str = "O"
            elif on_str == "O" and char.lower() == 'n':
                on_str = "On"
                off_str = ""
            elif char == '=':
                if inteiros:
                    sum += int(inteiros)
                print(sum)
                inteiros = ""


for linha in sys.stdin:
    if linha == "q":
        break
    rec_inteiros(linha)
