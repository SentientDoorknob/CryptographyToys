import random

text_paths = ["aliceinwonderland.txt", "doriangrey.txt", "frankenstein.txt", "greatgatsby.txt", "pride.txt",
              "simplesabotage.txt", "jeeves.txt"]


def GetParagraph(line_count):
    path = "Text/" + random.choice(text_paths)
    paragraph = ""

    with open(path, "rb") as file:
        num_lines = sum(1 for _ in file)

    read_line = random.randint(0, num_lines - line_count)

    with open(path, "r", encoding="utf8") as file:
        lines = file.read().split("\n")
        for line in lines[read_line:read_line + line_count]:
            paragraph += line + "\n"

    return paragraph


def GetWord():
    path = "Text/" + random.choice(text_paths)

    with open(path, "rb") as file:
        num_lines = sum(1 for _ in file)

    read_line = random.randint(0, num_lines - 1)

    with open(path, "r", encoding="utf8") as file:
        line = file.read().split("\n")[read_line]
        word = random.choice(line.split(" "))

    return word


def GetRandomParagraph(char_count):
    output = ""
    for i in range(char_count):
        x = random.randint(97, 122)
        output += chr(x)
    return output


def GetEnglishCorpus():
    output = ""
    for path in text_paths:
        with open(f"Text/{path}", "r", encoding="utf8") as file:
            output += file.read()
    return output
        
