import pandas as pd
from sympy import *
import os
def truth_table(args,expr_strs):
    from itertools import product
    iterator = product((True,False),repeat=len(args))
    res = pd.DataFrame(iterator,columns=args)
    for key,expr_str in expr_strs.items():
        expr_str = expr_str.lower().replace(' ', '').replace('→','>>').replace('∨','|').replace('∧','&').replace('¬','~').replace('!','~')
        expr = eval(expr_str)
        print(expr)
        print(simplify_logic(expr))
        res[key] = res.apply(lambda x: expr.subs({p:p_ for p,p_ in zip(args,x)}),axis=1)
    return res.replace(True,'T').replace(False,'F')

def start_after_save(save):
    def save_and_start(df,fileName):
        save(df,fileName)
        os.system(f'cmd /k start {fileName}')
    return save_and_start

@start_after_save
def save_tex(df,fileName):
    output = r"""
\documentclass{article}
\usepackage{booktabs}
\begin{document}
"""+df.to_latex().replace('{}','n')+r"""
\end{document}"""
    open(fileName,'w',encoding='utf-8').write(output)

@start_after_save
def save_pdf(df,fileName):
    fileDir,fileName = os.path.split(fileName)
    os.chdir(fileDir)
    fileName = os.path.splitext(fileName)[0]
    save_tex(df,f"{fileName}.tex")
    os.system(f'pdflatex "{fileName}.tex"')
    os.system(f'del "{fileName}.aux"  "{fileName}.log" "{fileName}.tex" "{fileName}.toc"')

@start_after_save
def save_xlsx(df,fileName):
    res.to_excel(fileName)

@start_after_save
def save_md(df,fileName):
    with open(fileName, 'w') as f:
        f.write(f"|${'$|$'.join(map(str,res.keys()))}$|\n")
        f.write(":--:".join('|'*(len(res.keys())+1))+"\n")
        for i,row in df.iterrows():
            f.write(f"|{'|'.join(row)}|\n")


if __name__ == '__main__':
    from sympy.abc import *
    res = truth_table([p,q,r],{
        'P1':'p | ~q',
        'P2':'r >> ~p',
        '(a)':'q >> ~r',
        '(b)':'~r >> ~q',
        '(c)':'~p | ~r',
        '(d)':'~q >> (~r & p | r & ~p)',
    })
    # save_tex(res,'D:/output.tex')
    save_pdf(res,'D:/output.pdf')
    # save_xlsx(res,'D:/output.xlsx')
    # save_md(res,'D:/output.md')

	 


