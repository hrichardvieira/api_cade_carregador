from pydantic import BaseModel

class CitySchema(BaseModel) :
    """

    """
    id_city : int = 1
    name : str = ""