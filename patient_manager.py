from data_structures import Fila
from triage_logic import montar_arvore, triagem_logica, CORES


class Paciente:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.descricao = CORES.get(cor, "Cor desconhecida")

    def __repr__(self):
        return f"Paciente(nome='{self.nome}', cor='{self.cor}', descricao='{self.descricao}')"

    def to_dict(self):
        """Retorna os dados do paciente em formato de dicionário."""
        return {"nome": self.nome, "cor": self.cor, "descricao": self.descricao}


class PatientManager:
    def __init__(self):
        self.filas = {
            "vermelho": Fila(),
            "laranja": Fila(),
            "amarelo": Fila(),
            "verde": Fila(),
            "azul": Fila(),
        }
        self.arvore_triagem = montar_arvore()
        # Ordem de prioridade para chamada de pacientes (Critério: Chamada de pacientes por prioridade)
        self.prioridade = ["vermelho", "laranja", "amarelo", "verde", "azul"]

    def cadastrar_paciente(self, nome, respostas_triagem):
        cor = triagem_logica(self.arvore_triagem, respostas_triagem)
        paciente = Paciente(nome, cor)
        self.filas[cor].enfileirar(paciente)
        return paciente, cor

    def chamar_proximo_paciente(self):
        for cor in self.prioridade:
            fila = self.filas[cor]
            if not fila.esta_vazia():
                return fila.desenfileirar()
        return None

    def status_filas(self):
        return {cor: len(fila) for cor, fila in self.filas.items()}
