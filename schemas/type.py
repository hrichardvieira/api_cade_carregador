from pydantic import BaseModel

class TypeSchema(BaseModel) :
    """

    """
    id_type : int = 1
    line : str = ""
    output_current : str = ""
    charging_voltage : str = ""
    maximum_power : str = ""
    number_of_outlets : str = ""
    model : str = ""