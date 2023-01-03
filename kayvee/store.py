from typing import Dict, Optional, List


class Store:
    def __init__(self) -> None:
        self.store: Dict[str, bytes] = {}

    def set(self, key: str, value: bytes):
        self.store[key] = value

    def get(self, key: str) -> Optional[bytes]:
        return self.store.get(key)

    def keys(self) -> List[str]:
        return list(self.store.keys())
