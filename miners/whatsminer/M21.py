from miners.btminer import BTMiner


class BTMinerM21(BTMiner):
    def __init__(self, ip: str) -> None:
        super().__init__(ip)

    def __repr__(self) -> str:
        return f"M21 - BTMiner: {str(self.ip)}"