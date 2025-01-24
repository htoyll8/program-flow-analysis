from abc import ABC, abstractmethod
from operand import Operand


class Block(ABC):
    @abstractmethod
    def execute(self):
        pass


class ReturnBlock(Block):
    def __init__(self, operand: Operand):
        self.operand = operand


class JumpBlock(Block):
    def __init__(self, label: str):
        self.label = label


class BranchBlock(Block):
    def __init__(self,
                 left: Operand,
                 test: str,
                 right: Operand,
                 true_label: str,
                 false_label: str) -> None:
        self.left = left
        self.test = test
        self.right = right
        self.true_label = true_label
        self.false_label = false_label
