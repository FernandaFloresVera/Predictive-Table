import re

predictive_table = {
    "F": [{"input": re.compile("function"), "production": ["function", "PNOMBRE", "PARAMETROS"]}],
    "PARAMETROS": [{"input": re.compile(r"\("), "production": ["PARAMLIST", ")"]}],
    "PARAMLIST": [{"input": re.compile("var"), "production": ["var", "VARIABLE", "LIST"]}],
    "var": [{"input": re.compile("var"), "production": ["var"]}],
    "VARIABLE": [{"input": re.compile(r"^[a-z]+$"), "production": ["PNOMBRE", ":", "IDENTIPO"]}],
    "PNOMBRE": [{"input": re.compile(r"^[a-z]+$"), "production": ["LETRA", "RESTOL"]}],
    "RESTOL": [
        {"input": re.compile(r"^[a-z]+$"), "production": ["L", "RN"]},
        {"input": re.compile(":"), "production": []},
        {"input": re.compile(r"\("), "production": []},
    ],
    "LETRA": [
        {
            "input": re.compile(r"^[a-z]+$"),
            "production": ["same"],
        }
    ],
    
    "IDENTIPO": [
        { "input": re.compile("integer"),
          "production": ["integer"],
        },
        
        { "input": re.compile("real"),
          "production": ["real"],
        },
        
        {
         "input": re.compile("boolean"),
         "production": ["boolean"],
        },
        
        {
            "input": re.compile("string"),
            "production": ["string"],
        },
    ],
    
    "LIST": [
        {"input": re.compile(r"\)"), "production": []},
        {"input": re.compile(";"), "production": ["VARIABLE", ":", "LISTT"]},
    ],
}

def separate(input):
    parts = re.findall(r"\w+|\S", input)
    return parts


def analize(input):
    stack = ["$", "FUNCION"]
    history = ""
    input = separate(input)
    for i in range(len(input)):
        while True:
            history += f"{stack} | Entrada: {input[0]}\n"
            if len(stack) == 0:
                return False, history
            if len(input) == 0:
                return False, history
            if stack[-1] == input[0]:
                stack.pop()
                input.pop(0)
                break
            if stack[-1] in predictive_table:
                for production in predictive_table[stack[-1]]:
                    if production["input"].match(input[0]):
                        stack.pop()
                        for i in range(len(production["production"]) - 1, -1, -1):
                            if production["production"][i] != "same":
                                stack.append(production["production"][i])
                            else:
                                stack.append(input[0])
                        break
                else:
                    return False, history
            else:
                return False, history
    history += f"{stack} | Entrada: {input}\n"
    print(history)

    if stack[-1] == "$" and len(input) == 0:
        return True, history
    return False, history



import re

predictive_table = {
    "FUNCION": [{"input": re.compile("function"), "production": ["function", "PNOMBRE", "PARAMETROS"]}],
    "PARAMETROS": [{"input": re.compile(r"\("), "production": ["(", "PARAMLIST", ")"]}],
    "PARAMLIST": [{"input": re.compile("var"), "production": ["var", "VARIABLE", "LIST"]}],
    "VARIABLE": [{"input": re.compile(r"^[a-z]+$"), "production": ["PNOMBRE", ":", "IDENTIPO"]}],
    "PNOMBRE": [{"input": re.compile(r"^[a-z]+$"), "production": ["LETTER", "RESTOL"]}],
    "RESTOL": [
        {"input": re.compile(r"^[a-z]+$"), "production": ["LETTER", "RESTOL"]},
        {"input": re.compile(":"), "production": []},
        {"input": re.compile(r"\("), "production": []},
    ],
    "LETTER": [
        {"input": re.compile(r"^[a-z]+$"), "production": ["same"]},
     ],
    "IDENTIPO": [
        {"input": re.compile("integer"), "production": ["integer"]}, 
        {"input": re.compile("real"), "production": ["real"]}, 
        {"input": re.compile("boolean"), "production": ["boolean"]}, 
        {"input": re.compile("string"), "production": ["string"]}
    ],
    "LIST": [
        {"input": re.compile(r"\)"), "production": []},
        {"input": re.compile(";"), "production": [";", "VARIABLE", "LIST"]},
    ],
}

def separate(input):
    parts = re.findall(r"\w+|\S", input)
    return parts

def analize(input):
    stack = ["$", "FUNCION"]
    history = ""
    input = separate(input)
    for i in range(len(input)):
        while True:
            history += f"{stack} | Entrada: {input[0]}\n"
            if len(stack) == 0:
                return False, history
            if len(input) == 0:
                return False, history
            if stack[-1] == input[0]:
                stack.pop()
                input.pop(0)
                break
            if stack[-1] in predictive_table:
                for production in predictive_table[stack[-1]]:
                    if production["input"].match(input[0]):
                        stack.pop()
                        for i in range(len(production["production"]) - 1, -1, -1):
                            if production["production"][i] != "same":
                                stack.append(production["production"][i])
                            else:
                                stack.append(input[0])
                        break
                else:
                    return False, history
            else:
                return False, history
    history += f"{stack} | Entrada: {input}\n"
    print(history)

    if stack[-1] == "$" and len(input) == 0:
        return True, history
    return False, history