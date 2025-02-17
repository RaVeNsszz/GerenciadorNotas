import aluno_service

def main():
    # Adiciona notas
    aluno_service.registrar_nota("João", "Matemática", 7.5)
    aluno_service.registrar_nota("Maria", "Física", 9.0)

    # Consulta
    print("Notas de João:", aluno_service.consultar_notas("João"))
    print("Notas de Física:", aluno_service.consultar_nota_disciplina("Física"))

    # Atualiza
    aluno_service.atualizar_nota("João", "Matemática", 8.0)
    print("Notas de João após atualização:", aluno_service.consultar_notas("João"))

    # Remove
    aluno_service.remover_nota("Maria", "Física")
    print("Notas de Maria após remoção:", aluno_service.consultar_notas("Maria"))

if __name__ == "__main__":
    main()
