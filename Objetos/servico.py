
class Servico():
    
    def __init__(self, serviceOption: str, descricao: str, id_client: int, id_employee: int):
        self.__serviceOption = serviceOption
        self.__descricao = descricao
        self.__id_client = id_client
        self.__id_employee = id_employee
        

    @property
    def serviceOption(self):
            return self.__serviceOption
    @property
    def descricao(self):
            return self.__descricao
    @property
    def id_client(self):
            return self.__id_client
    @property
    def id_employee(self):
        return self.__id_employee
    
    
    @serviceOption.setter
    def serviceOption(self, value):
        self.__serviceOption = value
    
    @descricao.setter
    def descricao(self, value):
        self.__descricao = value
    
    @id_client.setter
    def id_client(self, value):
        self.__id_client = value
    
    @id_employee.setter
    def id_employee(self,value):
        self.__id_employee = value

