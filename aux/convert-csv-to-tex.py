import pandas as pd

df = pd.read_csv('materialdesignicons.csv', header=None, keep_default_na=False)

def old__return_tex_string(name, code):
    import stringcase
    return """
    \expandafter\def\csname%
    mdi@""" + name + """\endcsname{\symbol{\"""" + code + """}}
    \def\mdi""" + stringcase.pascalcase(name.replace('-', '_')) + """{{\mdifont\csname%
    mdi@""" + name + """\endcsname}}
    """
def return_tex_string(name):
    return "  \\mdi{" + name + "}: "+ f"{name}"

output = r"\begin{longtable}{p{4.5cm} p{4.5cm} p{4.5cm}}" + '\n'
count = 0
for index, row in df.iterrows():
    name = row[0]
    code = row[1]
    # print(code, name)
    # print(index)
    # print(index % 3)
    if (count == 2):
        count = 0
        term_string = r' \\'
    else:
        count += 1
        term_string = ' &'
    output += return_tex_string(name) + term_string + '\n'
print(output[-2])
if (output[-2] == '&'):
    output = output[:-2]
    output += '\n'
output += r'\end{longtable}'

with open('mdi-definitions.tex', 'w') as f:
    f.write(output)