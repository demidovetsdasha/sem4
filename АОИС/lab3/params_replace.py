def replece_params(formula : str):
    return formula.replace("x1", "a").replace("x2", "b").replace("x3", "c")

def dereplece_params(formula: str):
    return formula.replace("a", "x1").replace("b", "x2").replace("c", "x3")

old_variables = ["a", "b", "c"]
new_variables = ["x1", "x2", "x3"]