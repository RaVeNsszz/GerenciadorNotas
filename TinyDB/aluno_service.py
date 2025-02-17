import aluno_repository

def registrar_nota(nome, disciplina, nota):
    if not isinstance(nota, (int, float)) or nota < 0 or nota > 10:
        raise ValueError("A nota deve ser um número entre 0 e 10.")
    aluno_repository.inserir_aluno(nome, disciplina, nota)


def consultar_notas(nome):
    notas = aluno_repository.buscar_notas_por_aluno(nome)
    return notas if notas else None


def consultar_nota_disciplina(disciplina):
    return aluno_repository.buscar_notas_por_disciplina(disciplina)


def atualizar_nota(nome, disciplina, nova_nota):
    if not isinstance(nova_nota, (int, float)) or nova_nota < 0 or nova_nota > 10:
        raise ValueError("A nova nota deve ser um número entre 0 e 10.")
    return aluno_repository.atualizar_nota_aluno(nome, disciplina, nova_nota)


def remover_nota(nome, disciplina):
    return aluno_repository.remover_nota_aluno(nome, disciplina)
