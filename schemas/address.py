from pydantic import BaseModel
from model.address import Address

class AddressSchema(BaseModel) :
    """ Define a estrutura de como um endereço deve ser registrado.
    """
    street : str = ""
    id_neighborhood : int = 1
    postal_code : str = ""
    coordinates : str = ""

class AddressViewSchema(BaseModel) :
    """Define como a estrutura da tabela endereço será retornado.
    """
    id_address : int = 1
    street : str = ""
    id_neighborhood : int = 1
    postal_code : str = ""
    coordinates : str = ""

class AddressUpdateSchema(BaseModel) :
    """ Define a estrutura de como um endereço deve ser registrado.
    """
    id_address : int = 1
    street : str = ""
    id_neighborhood : int = 1
    postal_code : str = ""
    coordinates : str = ""

class AddressFindSchema(BaseModel) :
    """ Definição da estrutura da busca.
        A busca será feita somente através do cep do endereço.
    """
    postal_code : str = ""

class AddressFindByIdSchema(BaseModel) :
    """ Definição da estrutura da busca.
        A busca será feita somente através do cep do endereço.
    """
    id_address : str = ""

class AddressDelSchema(BaseModel) :
    """ Definição de como será feita a estrutura do dado apresentado após 
        a requisição de remoção do dado do endereço.
    """
    message : str = ""
    postal_code : str = ""

def show_address(address : Address) :
    """ Retorna a apresentação da estrutura da tabela endereço.
    """
    return {
        "id_address" : address.id_address,
        "street" : address.street,
        "id_neighborhood" : address.id_neighborhood,
        "postal_code" : address.postal_code,
        "coordinates" : address.coordinates
    }