from flask_openapi3 import Tag

from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError

from model import Session
from model import Address

from schemas import ErrorSchema
from schemas import AddressSchema
from schemas.address import AddressViewSchema
from schemas.address import AddressFindSchema
from schemas.address import AddressFindByIdSchema
from schemas.address import AddressDelSchema
from schemas.address import AddressUpdateSchema
from schemas.address import show_address

address_tag = Tag(name="Address", description="Adição, Edição, Remoção e Visualização de Endereços.")

def register_address_route(app) :
    @app.post('/address', tags=[address_tag], responses={"200" : AddressViewSchema, "409" : ErrorSchema, "400" : ErrorSchema})
    def add_address(form: AddressSchema) :
        """Adiciona um novo endereço ao banco de dados

        Retorna as informa do endereço cadastrado.
        """
        new_register = Address(
            street = form.street,
            id_neighborhood = form.id_neighborhood,
            postal_code = form.postal_code,
            coordinates = form.coordinates
        )

        #logger.debug()

        try :
            session = Session()
            session.add(new_register)
            session.commit()
            #logger.debug()
            return show_address(new_register), 200
        
        except IntegrityError as integrityError :
            error_message = "Um endereço já foi cadastrado com esse nome!"
            #logger.warning()
            return {"message" : error_message}, 409
        
        except Exception as exception :
            print(exception)
            error_message = "Não foi possível salvar o endereço."
            #logger.warning()
            return {"message" : error_message}, 400

    @app.put('/address', tags=[address_tag], responses={"200" : AddressViewSchema, "409" : ErrorSchema, "400" : ErrorSchema})
    def update_address(form: AddressUpdateSchema) :
        """Atualiza o endereço a partir do id selecionado
        
        Permite atualizar id_type, id_address, id_status e name
        """
        id_address = form.id_address
        #logger.debug()

        session = Session()
        address = session.query(Address).filter(Address.id_address == id_address).first()

        if not address :
            error_message = "O endereço selecionado não foi encontrado."
            #logger.warning()
            return {"message" : error_message}, 404
        
        if form.street is not None:
            address.street = form.street
        if form.id_neighborhood is not None:
            address.id_neighborhood = form.id_neighborhood
        if form.postal_code is not None:
            address.postal_code = form.postal_code
        if form.coordinates is not None:
            address.coordinates = form.coordinates

        try :
            session.commit()
            #logger.debug()
            return show_address(address), 200
        
        except IntegrityError as integrityError :
            session.rollback()
            error_message = "O endereço informado já foi cadastrado."
            #logger.warning()
            return {"message" : error_message}, 400
        
        except Exception as exception :
            session.rollback()
            error_message = "Houve um erro ao atualizar o endereço."
            #logger.warning()
            return {"message" : error_message}, 400

    @app.get('/address', tags=[address_tag], responses={"200" : AddressViewSchema, "404" : ErrorSchema})
    def get_address(query: AddressFindSchema) :
        """Faz a busca do endereço com base no id
        Retorna o endereço cadastrado
        """

        address_postal_code = query.postal_code
        #logger.debug()

        session = Session()
        address = session.query(Address).filter(Address.postal_code == address_postal_code).first()

        if not address :
            error_message = "endereço não encontrado!"
            #logger.warning()
            return {"message" : error_message}, 404
        else :
            #logger.debug()
            return show_address(address), 200
        

    @app.get('/addressId', tags=[address_tag], responses={"200" : AddressViewSchema, "404" : ErrorSchema})
    def get_address_by_id(query: AddressFindByIdSchema) :
        """Faz a busca do endereço com base no id
        Retorna o endereço cadastrado
        """

        id_address = query.id_address
        #logger.debug()

        session = Session()
        address = session.query(Address).filter(Address.id_address == id_address).first()

        if not address :
            error_message = "endereço não encontrado!"
            #logger.warning()
            return {"message" : error_message}, 404
        else :
            #logger.debug()
            return show_address(address), 200

    @app.delete('/address', tags=[address_tag], responses={"200" : AddressDelSchema, "404" : ErrorSchema})
    def remove_address(query: AddressFindSchema) :
        """

        """
        address_postal_code = unquote(unquote(query.postal_code))
        # logger.debug()
        session = Session()
        count = session.query(Address).filter(Address.postal_code == address_postal_code).delete()
        session.commit()

        if count :
            #logger.debug()
            return {"message" : "endereço removido", "id_address" : address_postal_code}
        else :
            error_message = "O endereço não foi encontrado no banco de dados."
            #logger.warning()
            return {"message" : error_message}, 404