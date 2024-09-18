from pydantic import BaseModel

class Footprint(BaseModel):
    type: str
    electricity_unit : str
    electricity_value : float | int
    country : str