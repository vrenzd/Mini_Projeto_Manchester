from data_structures import NodoArvore

CORES = {
    "vermelho": "Emergência (atendimento imediato)",
    "laranja": "Muito urgente",
    "amarelo": "Urgente",
    "verde": "Pouco urgente",
    "azul": "Não urgente",
}


def montar_arvore():
    verde = NodoArvore(pergunta="Pouco urgente", cor="verde")
    amarelo = NodoArvore(pergunta="Urgente", cor="amarelo")
    laranja = NodoArvore(pergunta="Muito urgente", cor="laranja")
    vermelho = NodoArvore(pergunta="Emergência", cor="vermelho")

    dor_intensa = NodoArvore(
        pergunta="O paciente está com dor intensa?",
        filho_sim=amarelo,
        filho_nao=verde,
    )

    consciente = NodoArvore(
        pergunta="O paciente está consciente?",
        filho_sim=dor_intensa,
        filho_nao=laranja,
    )

    raiz = NodoArvore(
        pergunta="O paciente está respirando?",
        filho_sim=consciente,
        filho_nao=vermelho,
    )

    return raiz


def triagem_logica(arvore_raiz, respostas):
    nodo_atual = arvore_raiz

    # Mapeamento simplificado das perguntas para as chaves do dicionário de respostas
    mapeamento_perguntas = {
        "O paciente está respirando?": "respirando",
        "O paciente está consciente?": "consciente",
        "O paciente está com dor intensa?": "dor_intensa",
    }

    while nodo_atual and not nodo_atual.is_folha():
        pergunta = nodo_atual.pergunta
        chave_resposta = mapeamento_perguntas.get(pergunta)

        if chave_resposta is None:
            break

        resposta = respostas.get(chave_resposta, False)

        if resposta:
            nodo_atual = nodo_atual.filho_sim
        else:
            nodo_atual = nodo_atual.filho_nao

    if nodo_atual and nodo_atual.is_folha():
        return nodo_atual.cor
    return "azul"
