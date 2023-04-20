import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    planets = Column(String(2500), nullable=False)
    characters = Column(String(2500), nullable=False)
    created = Column(Integer, nullable=False)
    edited = Column(Integer, nullable=False)
    producer = Column(String(30), nullable=False)
    director = Column(String(30), nullable=False)
    realease_date = Column(Integer, nullable=False)
    opening_crawl = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)

    # name_id= Column(Integer, ForeignKey('planets.id'))
    # name = relationship(Planets)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(2500), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)

    # film_id= Column(Integer, ForeignKey('films.id'))
    # film = relationship(Films)

    # planets_id = Column(Integer, ForeignKey('films.id'))
    # planets = relationship(Films)

class PlanetsInFilms(Base):
    __tablename__ = 'planetsInFilms'
    id = Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    film_id = Column(Integer, ForeignKey('films.id'))
    film = relationship(Films)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(2500), nullable=False)
    model = Column(String(2500), nullable=False)
    vehicle_class = Column(String(2500), nullable=False)
    manufacturer = Column(String(2500), nullable=False)
    cost_in_credits = Column(String(2500), nullable=False)
    length = Column(Integer, nullable=False)
    crew = Column(String(2500), nullable=False)
    passangers = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(String(2500), nullable=False)

   
    # film_id= Column(Integer, ForeignKey('films.id'))
    # film = relationship(Films)


   
class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    hair_color = Column(String(30), nullable=False)
    eye_color = Column(String(30), nullable=False)
    birth_year = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)


class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship(Planets)
    film_id = Column(Integer, ForeignKey('films.id'))
    film = relationship(Films)
    person_id = Column(Integer, ForeignKey('people.id'))
    person = relationship(People)


class VehiclesInFilms(Base):
    __tablename__ = 'vehiclesInFilms'
    id = Column(Integer, primary_key=True)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)
    film_id = Column(Integer, ForeignKey('films.id'))
    film = relationship(Films)
   

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=True)

    def to_dict(self):
        return {}

        
class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    # username = Column(String(250), nullable=False)
    username_id = Column(String(250), ForeignKey('user.id'))
    username = relationship(User)
    fav_planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)
    fav_vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship(Films)
    fav_person_id = Column(Integer, ForeignKey('people.id'))
    person = relationship(People)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
