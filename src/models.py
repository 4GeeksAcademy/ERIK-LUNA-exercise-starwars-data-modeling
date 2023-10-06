import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String, nullable=False)
    skin_color = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    birth_year = Column(String, nullable=False)
    gender = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter= Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String, nullable=False)
    populations = Column(Integer, nullable=False)
    climate = Column(String, nullable=False)
    terrain = Column(String, nullable=False)
    surface_water = Column(Integer, nullable=False)
    

class Starship(Base):
    __tablename__ = 'starship'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String, nullable=False)
    starship_class = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(Integer(250), nullable=False)
    hyperdrive_rating = Column(Integer, nullable=False)
    MGLT = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(Integer, nullable=False)
    pilots = Column(Integer, nullable=False)
    


class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    starship_id = Column(Integer, ForeignKey('starship.id'))
    starship = relationship(Starship)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
