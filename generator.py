import pandas as pd
from sympy import *
import os
def truth_table(args,expr_strs):
    from itertools import product
    iterator = product(*[(True,False)]*len(args))
    res = pd.DataFrame(iterator,columns=args)
    for key,expr_str in expr_strs.items():
        expr_str = expr_str.replace(' ', '').replace('→','>>').replace('∨','|').replace('∧','&').replace('¬','~').replace('!','~')
        expr = eval(expr_str)
        print(expr)
        print(simplify_logic(expr))
        res[key] = res.apply(lambda x: expr.subs({p:p_ for p,p_ in zip(args,x)}),axis=1)
    return res.replace(True,'T').replace(False,'F')

def save_pdf(df,fileName):
    fileDir,fileName = os.path.split(fileName)
    os.chdir(fileDir)
    fileName = os.path.splitext(fileName)[0]
    output = r"""
\documentclass{article}
\usepackage{booktabs}
\begin{document}
"""+df.to_latex().replace('{}','n')+r"""
\end{document}"""
    open(f"{fileName}.tex",'w',encoding='utf-8').write(output)
    os.system(f'pdflatex "{fileName}.tex"')
    os.system(f'del "{fileName}.aux"  "{fileName}.log" "{fileName}.tex" "{fileName}.toc"')
    os.system(f'start {fileName}.pdf')

def save_xlsx(df,fileName):
    res.to_excel(fileName)


if __name__ == '__main__':
    import sympy
    a,b,c = sympy.symbols('a b c')
    res = truth_table([a,b,c],{
        # '¬p':'¬p',
        # '¬r':'¬r',
        "R":"(a&c|b&c)&(~(a&b&c))",
        "S":"(c & (a | b) & ~(a & b))",
    })
    save_pdf(res,'D:/output.pdf')
    save_xlsx(res,'D:/output.xlsx')

	 


