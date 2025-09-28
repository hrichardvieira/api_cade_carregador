from pydantic import BaseModel

class StateSchema(BaseModel) :
    """

    """
    id_state : int = 1
    name : str = ""
    fu : str = ""