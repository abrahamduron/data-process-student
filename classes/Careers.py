from classes.DbMongo import DbMongo

class Careers:

    def __init__(self, carrera, id=""):
        self.carrera = carrera
        self.__id = id
        self.__collection = "career_students"

    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id = result.inserted_id
    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = {'_id': self.__id}
        collection.delete_one(filterToUse)

    @staticmethod
    def get_one(db, id):
        collection = db["career_students"]
        filterToUse = {'_id': id}
        result = collection.find_one(filterToUse)

        return Careers(result["carrera"], result["_id"])

    @staticmethod
    def get_list(db):
        collection = db["career_students"]
        courses = collection.find()

        list_courses = []
        for e in courses:
            temp_courses = Careers(
                e["carrera"]
                , e["_id"]
            )

            list_courses.append(temp_courses)
        return list_courses

    @staticmethod
    def get_dict(db):
        collection = db["career_students"]
        courses = collection.find()

        dict_courses= {}
        for e in courses:
            dict_courses[e["carrera"]] = e["_id"]

        return dict_courses

    @staticmethod
    def delete_all(db):
        lista_e = Careers.get_list(db)
        for e in lista_e:
            e.delete(db)