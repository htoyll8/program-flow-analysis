from typing import Dict, List, Tuple
from block import Block
from operand import Var, Label


class Procedure:
    def __init__(self,
                 name: str,
                 vars: List[Var],
                 prologue: Label,
                 epilogue: Label) -> None:
        self.name = name
        self.vars: List[Var] = vars
        self.prologue: Label = prologue
        self.epilogue: Label = epilogue
        self.blocks: Dict[Tuple[Label, Block]] = {}

    def add_block(self, label: Label, block: Block) -> None:
        self.blocks.append((label, block))
