from classes.Careers import Careers
from classes.Courses import Courses

class Students:
    def __init__(self, numero_cuenta, nombre_completo, enrollment, edad, carrera, id=""):
        self.numero_cuenta = numero_cuenta
        self.nombre_completo = nombre_completo
        self.enrollment = enrollment
        self.edad = edad
        self.carrera = carrera
        self.__id = id
        self.__collection = "students"

    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id = result.inserted_id

    def update(self, db):
        collection = db[self.__collection]
        filterToUse = {'_id': self.__id}
        objStore = {'$set': self.__dict__}
        collection.update_one(filterToUse, objStore)

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = {'_id': self.__id}
        collection.delete_one(filterToUse)

    def get_one(db, id):
        collection = db["students"]
        filterToUse = {'_id': id}
        result = collection.find_one(filterToUse)

        return Courses(result["numero_cuenta"], result["_id"])

    def get_list(db):
        collection = db["students"]
        students = collection.find()

        list_students = []
        for e in students:
            temp_students = Students(
                e["numero_cuenta"]
                , e["nombre_completo"]
                , e["enrollment"]
                , e["edad"]
                , e["carreras"]
                , e["_id"]
            )

            list_students.append(temp_students)
        return list_students

    @staticmethod
    def delete_all(db):
        lista_e = Students.get_list(db)
        for e in lista_e:
            e.delete(db)