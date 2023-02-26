#(pista: un enrollment representa un estudiante y un curso. junto su estado si aprobo o no)
from classes.DbMongo import DbMongo

class Enrollments:

    def __init__(self, student, course, status_course, id=""):
        self.student = student
        self.course = course
        self.status_course = status_course
        self.__id = id
        self.__collection = "enrollments_students"

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
        collection = db["enrollments_students"]
        filterToUse = {'_id': id}
        result = collection.find_one(filterToUse)

        return Enrollments(result["student"], result["_id"])

    @staticmethod
    def get_list(db):
        collection = db["enrollments_students"]
        enrollments = collection.find()

        list_enrollments = []
        for e in enrollments:
            temp_courses = Enrollments(
                e["student"]
                , e["_id"]
            )

            list_enrollments.append(temp_courses)
        return list_enrollments

    @staticmethod
    def get_dict(db):
        collection = db["enrollments_students"]
        enrollments = collection.find()

        dict_enrollments= {}
        for e in enrollments:
            dict_enrollments[e["student"]] = e["_id"]

        return dict_enrollments

    @staticmethod
    def delete_all(db):
        lista_e = Enrollments.get_list(db)
        for e in lista_e:
            e.delete(db)