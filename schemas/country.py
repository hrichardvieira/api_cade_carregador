from pydantic import BaseModel

class CountrySchema(BaseModel) :
    """

    """
    id_country : int = 1
    name : str = ""
    country_code : int = 55