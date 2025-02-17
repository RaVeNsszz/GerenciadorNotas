from tinydb import Query
from database import get_db

db = get_db()
Aluno = Query()

def inserir_aluno(nome, disciplina, nota):
    aluno_existente = db.search(Aluno.nome == nome)
    
    if aluno_existente:
        for aluno_db in aluno_existente:
            aluno_db["notas"][disciplina] = nota
            db.update(aluno_db, doc_ids=[aluno_db.doc_id])
    else:
        db.insert({"nome": nome, "notas": {disciplina: nota}})


def buscar_notas_por_aluno(nome):
    return db.search(Aluno.nome == nome)


def buscar_notas_por_disciplina(disciplina):
    return db.search(Aluno.notas[disciplina].exists())


def atualizar_nota_aluno(nome, disciplina, nova_nota):
    aluno_existente = db.search(Aluno.nome == nome)
    if aluno_existente:
        for aluno_db in aluno_existente:
            if disciplina in aluno_db["notas"]:
                aluno_db["notas"][disciplina] = nova_nota
                db.update(aluno_db, doc_ids=[aluno_db.doc_id])
                return True
    return False


def remover_nota_aluno(nome, disciplina):
    aluno_existente = db.search(Aluno.nome == nome)
    if aluno_existente:
        for aluno_db in aluno_existente:
            if disciplina in aluno_db["notas"]:
                del aluno_db["notas"][disciplina]
                db.update(aluno_db, doc_ids=[aluno_db.doc_id])
                return True
    return False
