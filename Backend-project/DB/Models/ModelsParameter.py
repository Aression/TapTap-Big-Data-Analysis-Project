#from DataBase import db

#Used in Database Modules, for example, Class User(db.Model,EntityBase)
#define entitybase to define json interface then we can use jsnotify
#it's defined for local database test and dont use jsonity, backend shuould use PyXXX which return object instead
class EntityBase(object):
    def to_json(self):
        fields = self.__dict__
        if "_sa_instance_state" in fields:
            del fields["_sa_instance_state"]
        return fields

#All images are stored in server



