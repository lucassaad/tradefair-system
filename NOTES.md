# Notes

## SQLAlchemy
SQLAlchemy is a Python library that provides SQL and Object Relational Mapping features for database access.
### Object Relational Mapping
Mapeamento Objeto Relacional: 
- técnica que conecta sistemas orientados a objetos a banco de dados relacionais.
- Cria uma camada intermediária que traduz as operações realizadas em objetos para comandos SQL, simplificando o acesso e manipulação de dados
- Funciona mapeando classes e propriedades de objetos para tavelas e colunas do banco de dados.
### SQLAchemy.orm
- **.orm_registry**: maintains a set of classes that are mapped

## Pydantic
Data validation and settings management library for Python that leverages type hints to validate and serialize data schemas
### BaseModel
A base class for creating Pydantic models
### Field
- fornece metadados, validações adicionais e configurações para campos do modelo

## Alembic 
lightweight database migration tool for usage with the SQLAlchemy Database toolkit for Python

### Migrations 
- scripts que permitem gerenciar alterações no esquema de um banco de dados de forma sistemática e reprodutível 
- forma de criar uma "linha do tempo" de modificações feitas em um banco de dados 