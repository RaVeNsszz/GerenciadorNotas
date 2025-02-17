from tinydb import TinyDB

db = TinyDB("desempenho_academico.json")

def get_db():
    return db