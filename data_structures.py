from collections import deque


class NodoArvore:
    def __init__(self, pergunta, filho_sim=None, filho_nao=None, cor=None):
        self.pergunta = pergunta
        self.filho_sim = filho_sim
        self.filho_nao = filho_nao
        self.cor = cor

    def is_folha(self):
        return (
            self.filho_sim is None and self.filho_nao is None and self.cor is not None
        )


class Fila:
    def __init__(self):
        self._dados = deque()

    def enfileirar(self, item):
        self._dados.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self._dados.popleft()
        return None

    def esta_vazia(self):
        return len(self._dados) == 0

    def __len__(self):
        return len(self._dados)

    def __repr__(self):
        return f"Fila(tamanho={len(self)})"
