from typing import List
from pydantic import BaseModel
from model.charger import Charger

class ChargerSchema(BaseModel) :
    """ Define a estrutura de como um carregador deve ser registrado.
    """
    id_type : int = 1
    id_address : int = 1
    id_status : int = 1
    name : str = "Carregador do Extra"
    # timestamp  : str = "Tue, 23 Sep 2025 11:30:00 GMT"

class ChargerViewSchema(BaseModel) :
    """Define como a estrutura da tabela charger será retornado.
    """
    id_charger : int = 1
    id_type : int = 1
    id_address : int = 1
    id_status : int = 1
    name : str = "Tauste"
    timestamp : str = "Tue, 23 Sep 2025 10:00:00 GMT"

class ChargerFindSchema(BaseModel) :
    """ Definição da estrutura da busca.
        A busca será feita somente através do nome do carregador.
    """
    name : str = "Tauste"

class ChargerListSchema(BaseModel) :
    """ Definição da estrutura, em lista, que será retornada com os carregadores. 
    """
    chargers : List[ChargerSchema]

class ChargerDelSchema(BaseModel) :
    """ Definição de como será feita a estrutura do dado apresentado após 
        a requisição de remoção do dado do carregador.
    """
    message : str = ""
    name : str = ""

def show_charger(charger : Charger) :
    """ Retorna a apresentação da estrutura da tabela carregador.
    """
    return {
        "id_charger" : charger.id_address,
        "id_type" : charger.id_type,
        "id_address" : charger.id_address,
        "id_status" : charger.id_status,
        "name" : charger.name,
        "timestamp" : charger.timestamp
    }

def show_charger_list(chargers : List[Charger]) :
    """ Retorna a apresentação de uma lista com os dados de carregador.
    """
    charger_list = []
    for charger in chargers :
        charger_list.append({
            "id_type" : charger.id_type,
            "id_address" : charger.id_address,
            "id_status" : charger.id_status,
            "name" : charger.name,
            "timestamp" : charger.timestamp
        })
    
    return {"chargers" : charger_list}
