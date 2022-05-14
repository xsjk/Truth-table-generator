# 真值表生成器

做离散作业时顺手写的小工具，给逻辑表达式，生成真值表，导出pdf/excel/markdown

## Usage

### 生成真值表

调用truth_table函数

```python
df = truth_table(List[Symbol],Dict{name_str:expr_str})->pd.DataFrame
```

e.g.

```python
import sympy
a,b,c = sympy.symbols('a b c')
res = truth_table([a,b,c],{
    "R":"(a&c|b&c)&(~(a&b&c))",
    "S":"(c & (a | b) & ~(a & b))",
})
```

### 导出真值表

调用save_tex函数，导出latex

```python
save_latex(df:pd.DataFrame,path:str)
```

调用save_pdf函数，导出pdf （需将pdflatex加入环境变量）

```python
save_pdf(df:pd.DataFrame,path:str)
```

调用save_xlsx函数，导出excel

```python
save_xlsx(df:pd.DataFrame,path:str)
```

调用save_md函数，导出markdown

```python
save_md(df:pd.DataFrame,path:str)
```

e.g.

```python
res = ...
save_pdf(res,'D:/output.pdf')
```

![image-20220502083700237](https://github.com/xsjk/Truth-table-generator/raw/master/example_output.png)

## Requirements

sympy（用于逻辑运算）
pandas（用于列表，导出latex/excel）
pdflatex（用于导出pdf）
