from pydantic import BaseModel

class StatusSchema(BaseModel) :
    """

    """
    id_status : int = 1
    name : str = ""