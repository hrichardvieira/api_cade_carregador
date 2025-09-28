from flask_openapi3 import Tag

from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError

from model import Session
from model import Charger

from schemas import ErrorSchema
from schemas import ChargerSchema
from schemas.charger import ChargerViewSchema
from schemas.charger import ChargerFindSchema
from schemas.charger import ChargerListSchema
from schemas.charger import ChargerDelSchema
from schemas.charger import ChargerUpdateSchema
from schemas.charger import show_charger
from schemas.charger import show_charger_list

charger_tag = Tag(name="Charger", description="Adição, Edição, Remoção e Visualização de Carregadores.")

def register_charger_route(app) :
    @app.post('/charger', tags=[charger_tag], responses={"200" : ChargerViewSchema, "409" : ErrorSchema, "400" : ErrorSchema})
    def add_charger(form: ChargerSchema) :
        """Adiciona um novo carregador ao banco de dados

        Retorna as informa do carregador cadastrado.
        """
        new_register = Charger(
            id_type = form.id_type,
            id_address = form.id_address,
            id_status = form.id_status,
            name = form.name,
        )

        #logger.debug()

        try :
            session = Session()
            session.add(new_register)
            session.commit()
            #logger.debug()
            return show_charger(new_register), 200
        
        except IntegrityError as integrityError :
            error_message = "Um carregador já foi cadastrado com esse nome!"
            #logger.warning()
            return {"message" : error_message}, 409
        
        except Exception as exception :
            print(exception)
            error_message = "Não foi possível salvar o carregador."
            #logger.warning()
            return {"message" : error_message}, 400

    @app.put('/charger', tags=[charger_tag], responses={"200" : ChargerViewSchema, "409" : ErrorSchema, "400" : ErrorSchema})
    def update_charger(form: ChargerUpdateSchema) :
        """Atualiza o carregador a partir do id selecionado
        
        Permite atualizar id_type, id_address, id_status e name
        """
        id_charger = form.id_charger
        #logger.debug()

        session = Session()
        charger = session.query(Charger).filter(Charger.id_charger == id_charger).first()

        if not charger :
            error_message = "O carregador selecionado não foi encontrado."
            #logger.warning()
            return {"message" : error_message}, 404
        
        if form.id_type is not None:
            charger.id_type = form.id_type
        if form.id_address is not None:
            charger.id_address = form.id_address
        if form.id_status is not None:
            charger.id_status = form.id_status
        if form.name is not None:
            charger.name = form.name

        try :
            session.commit()
            #logger.debug()
            return show_charger(charger), 200
        
        except IntegrityError as integrityError :
            session.rollback()
            error_message = "O carregador informado já foi cadastrado."
            #logger.warning()
            return {"message" : error_message}, 400
        
        except Exception as exception :
            session.rollback()
            error_message = "Houve um erro ao atualizar o carregador."
            #logger.warning()
            return {"message" : error_message}, 400

    @app.get('/charger', tags=[charger_tag], responses={"200" : ChargerViewSchema, "404" : ErrorSchema})
    def get_charger(query: ChargerFindSchema) :
        """Faz a busca do carregador com base no id
        
        Retorna o carregador cadastrado
        """

        charger_name = query.name
        #logger.debug()

        session = Session()
        charger = session.query(Charger).filter(Charger.name == charger_name).first()

        print(charger_name)
        print(charger)

        if not charger :
            error_message = "Carregador não encontrado!"
            #logger.warning()
            return {"message" : error_message}, 404
        else :
            #logger.debug()
            return show_charger(charger), 200

    @app.get('/chargers', tags=[charger_tag], responses={"200" : ChargerListSchema, "404" : ErrorSchema})
    def get_chargers() :
        """Faz a busca de todos os carregadores cadastrados

        Lista todos os carregadores cadastrados.
        """
        #logger.debug()

        session = Session()
        charger_list = session.query(Charger).all()

        if not charger_list :
            return {"chargers" : []}, 200
        else :
            # logger.debug()
            return show_charger_list(charger_list), 200

    @app.delete('/charger', tags=[charger_tag], responses={"200" : ChargerDelSchema, "404" : ErrorSchema})
    def remove_charger(form : ChargerFindSchema) :
        """

        """
        charger_name = unquote(unquote(form.name))
        # logger.debug()
        session = Session()
        count = session.query(Charger).filter(Charger.name == charger_name).delete()
        session.commit()

        if count :
            #logger.debug()
            return {"message" : "carregador removido", "id_charger" : charger_name}
        else :
            error_message = "O carregador não foi encontrado no banco de dados."
            #logger.warning()
            return {"message" : error_message}, 404