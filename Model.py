#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Model.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Date,ForeignKey
from sqlalchemy.orm import relationship,sessionmaker,Session

import time
from datetime import date

# Criação do banco de dados no sqlite
engine = create_engine("sqlite:///banco.db")

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

Base = declarative_base()

# Classe Cliente
class Client(Base):
    __tablename__ = "Client"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    cpf = Column(String)
    segment = Column(String)
    service = relationship("Service")

# Classe Produto
class Product(Base):
    __tablename__ = "Product"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)

# Classe Serviço
class Service(Base):
    __tablename__ = "Service"
    id = Column(Integer,primary_key=True)
    cliente_id = Column(Integer,ForeignKey("Client.id"))
    produto_id = Column(Integer,ForeignKey("Product.id"))
    request_date = Column(Date)
    cancel_date = Column(Date)
    client = relationship("Client")
    product = relationship("Product")

if __name__ == "__main__":    
    try:
        Base.metadata.create_all(engine)
		# Cliente
        dexter = Client(name="XPTO3",cpf="000.000.000/0002-00",segment="Logistica")

        # Produtos
        intranet = Product(name="Intranet",description="Intranet da XPTO",image="intranet")
        website = Product(name="Website",description="Website da XPTO",image="website")
        backup = Product(name="Backup",description="Backup da XPTO",image="backup")

        service1 = Service()
        service1.request_date = date.today()
        service1.product = intranet
        dexter.service.append(service1)

        service2 = Service()
        service2.request_date = date.today()
        service2.product = website
        dexter.service.append(service2)

        service3 = Service()
        service3.request_date = date.today()
        service3.product = backup
        dexter.service.append(service3)

        session.add(dexter)
        session.add(intranet)
        session.add(website)
        session.add(backup)
        session.add(service1)
        session.add(service2)
        session.add(service3)
        session.commit()

        # Vamos imprimir todos os resultados do banco de dados
        for c in session.query(Client).all():
            print c.id,c.name
        
        for c in session.query(Product).all():
            print c.id,c.name
        
    except Exception as e:
        print "Falhou ao salvar no BD ",e
        session.rollback()
