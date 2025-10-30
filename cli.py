from patient_manager import PatientManager
from triage_logic import CORES


def obter_respostas_cli():
    respostas = {}

    while True:
        resp = input("O paciente está respirando? (S/N): ").upper()
        if resp in ["S", "N"]:
            respostas["respirando"] = resp == "S"
            break
        print("Resposta inválida. Digite S ou N.")

    if not respostas["respirando"]:
        return respostas

    while True:
        resp = input("O paciente está consciente? (S/N): ").upper()
        if resp in ["S", "N"]:
            respostas["consciente"] = resp == "S"
            break
        print("Resposta inválida. Digite S ou N.")

    if not respostas["consciente"]:
        return respostas

    while True:
        resp = input("O paciente está com dor intensa? (S/N): ").upper()
        if resp in ["S", "N"]:
            respostas["dor_intensa"] = resp == "S"
            break
        print("Resposta inválida. Digite S ou N.")

    return respostas


def menu_principal():

    manager = PatientManager()

    print("=" * 30)
    print("SISTEMA DE TRIAGEM MANCHESTER")
    print("=" * 30)

    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar paciente")
        print("2 - Chamar paciente")
        print("3 - Mostrar status das filas")
        print("0 - Sair")

        escolha = input("Escolha: ")

        if escolha == "1":
            nome = input("Nome do paciente: ")
            if not nome:
                print("Nome não pode ser vazio.")
                continue

            respostas = obter_respostas_cli()
            paciente, cor = manager.cadastrar_paciente(nome, respostas)

            print("-" * 30)
            print(f"Paciente {paciente.nome} adicionado à fila.")
            print(f"Cor atribuída: {paciente.cor.upper()} - {paciente.descricao}")
            print("-" * 30)

        elif escolha == "2":
            paciente_chamado = manager.chamar_proximo_paciente()
            if paciente_chamado:
                print("-" * 30)
                print(
                    f"Chamando paciente da fila {paciente_chamado.cor.upper()}: {paciente_chamado.nome}"
                )
                print("-" * 30)
            else:
                print("-" * 30)
                print("Não há pacientes nas filas.")
                print("-" * 30)

        elif escolha == "3":
            status = manager.status_filas()
            print("-" * 30)
            print("STATUS DAS FILAS:")
            for cor, tamanho in status.items():
                descricao = CORES[cor]
                print(f"- {cor.upper()} ({descricao}): {tamanho} paciente(s)")
            print("-" * 30)

        elif escolha == "0":
            print("Saindo do sistema. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()
