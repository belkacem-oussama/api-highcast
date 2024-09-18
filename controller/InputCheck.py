from typing import Any, Dict

class InputCheck:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.data = data

    def is_kwh(self, field: str) -> bool|str :
        value = self.data.get(field)
        if not value == "kwh" : 
            return f"Le champ 'electricty_value' doit être 'kwh'."
        return True

    def is_electricity(self, field: str) -> bool|str :
        value = self.data.get(field)
        if not value == "electricity" : 
            return f"Le champ 'type' doit être 'electricity'."
        return True

    def is_positive_number(self, field: str) -> bool | str:
        value = self.data.get(field)
        if not isinstance(value, (int, float)):
            return f"Le champ '{field}' doit être un chiffre."
        if value <= 0:
            return f"Le champ '{field}' doit être supérieur à 0."
        return True