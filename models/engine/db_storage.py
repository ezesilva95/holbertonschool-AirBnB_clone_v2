#!/usr/bin/python3
"""
    Define class DatabaseStorage
"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base, BaseModel
from sqlalchemy.orm import Session


class DBStorage:
    """
    Db
    """
    __engine = None
    __session = None

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

    def __init__(self):
        """
        engine must be linked to the MySQL database
        """
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        envv = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      user, pwd, host, db), pool_pre_ping=True)

        if envv == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session
        """
        new_dict = {}
        if cls is None:
            for my_type in classes.keys():
                for obj in self.__session.query(classes[my_type]).all():
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        else:
            if isinstance(cls, str):
                cls = classes[cls]
            for obj in self.__session.query(cls).all():
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj

        return new_dict

    
    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        reload
        """
        Base.metadata.create_all(self.__engine)
        f = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(f)
        self.__session = Session

    def close(self):
        """
        """
        self.__session.close()
