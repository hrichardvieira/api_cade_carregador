from flask_openapi3 import Tag

from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError

from model import Session
from model import Neighborhood

from schemas import ErrorSchema
from schemas import NeighborhoodSchema
from schemas.neighborhood import NeighborhoodViewSchema
from schemas.neighborhood import NeighborhoodFindSchema
from schemas.neighborhood import NeighborhoodDelSchema
from schemas.neighborhood import NeighborhoodUpdateSchema
from schemas.neighborhood import show_neighborhood

neighborhood_tag = Tag(name="Neighborhood", description="Adição, Edição, Remoção e Visualização de Bairro.")

def register_neighborhood_route(app) :
    @app.post('/neighborhood', tags=[neighborhood_tag], responses={"200" : NeighborhoodViewSchema, "409" : ErrorSchema, "400" : ErrorSchema})
    def add_neighborhood(form: NeighborhoodSchema) :
        """Adiciona um novo endereço ao banco de dados

        Retorna as informa do endereço cadastrado.
        """
        new_register = Neighborhood(
            name = form.name,
            id_city = form.id_city
        )

        #logger.debug()

        try :
            session = Session()
            session.add(new_register)
            session.commit()
            #logger.debug()
            return show_neighborhood(new_register), 200
        
        except IntegrityError as integrityError :
            error_message = "Um endereço já foi cadastrado com esse nome!"
            #logger.warning()
            return {"message" : error_message}, 409
        
        except Exception as exception :
            print(exception)
            error_message = "Não foi possível salvar o endereço."
            #logger.warning()
            return {"message" : error_message}, 400

    @app.put('/neighborhood', tags=[neighborhood_tag], responses={"200" : NeighborhoodViewSchema, "409" : ErrorSchema, "400" : ErrorSchema})
    def update_neighborhood(form: NeighborhoodUpdateSchema) :
        """Atualiza o endereço a partir do id selecionado
        
        Permite atualizar id_type, id_address, id_status e name
        """
        id_neighborhood = form.id_neighborhood
        #logger.debug()

        session = Session()
        neighborhood = session.query(Neighborhood).filter(Neighborhood.id_neighborhood == id_neighborhood).first()

        if not neighborhood :
            error_message = "O endereço selecionado não foi encontrado."
            #logger.warning()
            return {"message" : error_message}, 404
        
        if form.name is not None:
            neighborhood.name = form.name
        if form.id_city is not None:
            neighborhood.id_city = form.id_city

        try :
            session.commit()
            #logger.debug()
            return show_neighborhood(neighborhood), 200
        
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

    @app.get('/neighborhood', tags=[neighborhood_tag], responses={"200" : NeighborhoodViewSchema, "404" : ErrorSchema})
    def get_neighborhood(query: NeighborhoodFindSchema) :
        """Faz a busca do endereço com base no id
        Retorna o endereço cadastrado
        """

        neighborhood_name = query.name
        #logger.debug()

        session = Session()
        neighborhood = session.query(Neighborhood).filter(Neighborhood.name == neighborhood_name).first()

        if not neighborhood :
            error_message = "endereço não encontrado!"
            #logger.warning()
            return {"message" : error_message}, 404
        else :
            #logger.debug()
            return show_neighborhood(neighborhood), 200

    @app.delete('/neighborhood', tags=[neighborhood_tag], responses={"200" : NeighborhoodDelSchema, "404" : ErrorSchema})
    def remove_neighborhood(query: NeighborhoodFindSchema) :
        """

        """
        neighborhood_name = unquote(unquote(query.name))
        # logger.debug()
        session = Session()
        count = session.query(Neighborhood).filter(Neighborhood.name == neighborhood_name).delete()
        session.commit()

        if count :
            #logger.debug()
            return {"message" : "endereço removido", "id_address" : neighborhood_name}
        else :
            error_message = "O endereço não foi encontrado no banco de dados."
            #logger.warning()
            return {"message" : error_message}, 404