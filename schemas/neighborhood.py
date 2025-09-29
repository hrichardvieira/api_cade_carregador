from pydantic import BaseModel
from model.neighborhood import Neighborhood

class NeighborhoodSchema(BaseModel) :
    """ Define a estrutura de como um bairro deve ser registrado.
    """
    name : str = ""
    id_city : int = 1

class NeighborhoodViewSchema(BaseModel) :
    """Define como a estrutura da tabela bairro será retornado.
    """
    id_neighborhood : int = 1
    name : str = ""
    id_city : int = 1

class NeighborhoodFindSchema(BaseModel) :
    """ Definição da estrutura da busca.
        A busca será feita somente através do nome do bairro.
    """
    name : str = ""

def show_neighborhood(neighborhood : Neighborhood) :
    """ Retorna a apresentação da estrutura da tabela bairro.
    """
    return {
        "id_neighborhood" : neighborhood.id_neighborhood,
        "name" : neighborhood.name,
        "id_city" : neighborhood.id_city
    }