from core_system import CoreSystem
from block import ReturnBlock
from operand import Int, Var, Label
from procedure import Procedure

system = CoreSystem()

one = Int(1)
two = Int(2)
three = Int(3)

vars = [
    Var("x", one),
    Var("y", two),
    Var("z", three)
]

prologue = Label("prologue")
epilogue = Label("epilogue")

return_statement_label = Label("return_three")
return_statement = ReturnBlock(three)

main_function = Procedure(name="main",
                          vars=vars,
                          prologue=prologue,
                          epilogue=epilogue)

main_function.add_block(return_statement_label, return_statement)

print("Main function: ")
print(f"{main_function.name}")
print(f"{main_function.vars}")
print(f"{main_function.prologue}")
print(f"{main_function.epilogue}")
print(f"{main_function.blocks}")
print(f"Return block: {main_function.get_block(return_statement_label)}")
