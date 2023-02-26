from classes.DbMongo import DbMongo

class Courses:

    def __init__(self, course, id=""):
        self.course = course
        self.__id = id
        self.__collection = "course_students"

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
        collection = db["course_students"]
        filterToUse = {'_id': id}
        result = collection.find_one(filterToUse)

        return Courses(result["course"], result["_id"])

    @staticmethod
    def get_list(db):
        collection = db["course_students"]
        courses = collection.find()

        list_courses = []
        for e in courses:
            temp_courses = Courses(
                e["course"]
                , e["_id"]
            )

            list_courses.append(temp_courses)
        return list_courses

    @staticmethod
    def get_dict(db):
        collection = db["course_students"]
        courses = collection.find()

        dict_courses= {}
        for e in courses:
            dict_courses[e["course"]] = e["_id"]

        return dict_courses

    @staticmethod
    def delete_all(db):
        lista_e = Courses.get_list(db)
        for e in lista_e:
            e.delete(db)