from typing import Dict
from block import Block
from procedure import Procedure


class CoreSystem:
    def __init__(self) -> None:
        self.blocks: Dict[str, Block] = {}
        self.procedures: Dict[str, Procedure] = {}

    def register_block(self, label: str, block: Block):
        self.blocks[label] = block

    def register_procedure(self, proc: Procedure):
        self.procedures[proc.name] = proc
