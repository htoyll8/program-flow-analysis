from abc import ABC


class Operand(ABC):
    pass


class Int(Operand):
    def __init__(self, value: int) -> None:
        self.value = value


class Str(Operand):
    def __init__(self, value: str) -> None:
        self.value = value


class Bool(Operand):
    def __init__(self, value: bool) -> None:
        self.value = value


class Var(Operand):
    def __init__(self, name: str, value: Operand) -> None:
        self.name = name
        self.value = value


class Label(Operand):
    def __init__(self, value: str) -> None:
        self.value = value
