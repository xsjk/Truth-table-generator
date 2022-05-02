# 真值表生成器

做离散作业时顺手写的小工具，给逻辑表达式，生成真值表，导出pdf

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

调用save_pdf函数，导出pdf

```python
save_pdf(pd.DataFrame,path_str)
```

调用save_xlsx函数，导出excel

```python
save_xlsx(pd.DataFrame,path_str)
```

e.g.

```python
res = ...
save_pdf(res,'D:/output.pdf')
```

![image-20220502083700237](.\example_output.png)

## Requirements

sympy	pandas	pdftex
