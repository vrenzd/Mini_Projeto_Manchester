import streamlit as st
from patient_manager import PatientManager
from triage_logic import CORES

if "manager" not in st.session_state:
    st.session_state.manager = PatientManager()


def exibir_status_filas():
    st.subheader("Status das Filas de Triagem")

    status = st.session_state.manager.status_filas()

    cores_ordenadas = ["vermelho", "laranja", "amarelo", "verde", "azul"]

    colunas = st.columns(len(cores_ordenadas))

    for i, cor in enumerate(cores_ordenadas):
        descricao = CORES[cor]
        tamanho = status[cor]

        cor_css = {
            "vermelho": "#FF0000",
            "laranja": "#FF8C00",
            "amarelo": "#FFFF00",
            "verde": "#00FF00",
            "azul": "#0000FF",
        }.get(cor, "#CCCCCC")

        text_color = "#000000" if cor in ["amarelo", "verde"] else "#FFFFFF"

        colunas[i].markdown(
            f"""
            <div style="
                background-color: {cor_css}; 
                padding: 10px; 
                border-radius: 5px; 
                text-align: center;
                color: {text_color};
                height: 150px;
            ">
                <h4 style="margin: 0; color: inherit;">{cor.upper()}</h4>
                <p style="margin: 0; font-size: 12px; color: inherit;">{descricao}</p>
                <h1 style="margin: 0; color: inherit;">{tamanho}</h1>
                <p style="margin: 0; font-size: 12px; color: inherit;">paciente(s)</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def cadastrar_paciente_form():
    st.subheader("1. Cadastrar Novo Paciente")

    mensagem_placeholder = st.empty()

    with st.form("form_cadastro"):
        nome = st.text_input("Nome do Paciente:", key="nome_paciente")

        st.markdown("---")
        st.markdown("**Perguntas de Triagem (Responda 'Sim' ou 'Não'):**")

        respirando = st.radio(
            "O paciente está respirando?",
            options=["Sim", "Não"],
            key="resp_respirando",
            index=0,
        )

        respostas = {"respirando": (respirando == "Sim")}

        if respostas["respirando"]:
            consciente = st.radio(
                "O paciente está consciente?",
                options=["Sim", "Não"],
                key="resp_consciente",
                index=0,
            )
            respostas["consciente"] = consciente == "Sim"

            if respostas["consciente"]:

                dor_intensa = st.radio(
                    "O paciente está com dor intensa?",
                    options=["Sim", "Não"],
                    key="resp_dor_intensa",
                    index=1,
                )
                respostas["dor_intensa"] = dor_intensa == "Sim"

        submitted = st.form_submit_button("Realizar Triagem e Cadastrar")

        if submitted:
            if not nome:
                mensagem_placeholder.error("Por favor, insira o nome do paciente.")
            else:
                paciente, cor = st.session_state.manager.cadastrar_paciente(
                    nome, respostas
                )
                mensagem_placeholder.success(
                    f"Paciente **{paciente.nome}** cadastrado com sucesso!"
                )
                st.info(
                    f"Classificação: **{paciente.cor.upper()}** - {paciente.descricao}"
                )

                st.session_state.last_action = "cadastro"
                st.rerun()


def chamar_paciente_btn():
    st.subheader("2. Chamar Próximo Paciente")

    mensagem_placeholder = st.empty()

    if st.button("Chamar Paciente Mais Urgente"):
        paciente_chamado = st.session_state.manager.chamar_proximo_paciente()

        if paciente_chamado:
            mensagem_placeholder.warning(
                f"Chamando paciente da fila **{paciente_chamado.cor.upper()}** ({paciente_chamado.descricao}): {paciente_chamado.nome}"
            )
        else:
            mensagem_placeholder.info("Não há pacientes nas filas para chamar.")

        st.session_state.last_action = "chamada"
        st.rerun()


def main():
    st.set_page_config(page_title="Simulador Protocolo de Manchester", layout="wide")
    st.title("Simulador do Protocolo de Manchester")
    st.caption("Sistema de Triagem de Pacientes - FATEC")

    exibir_status_filas()

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        cadastrar_paciente_form()

    with col2:
        chamar_paciente_btn()

    st.markdown("---")
    st.subheader("Detalhes das Filas (Visualização)")

    status = st.session_state.manager.status_filas()

    for cor, descricao in CORES.items():
        fila = st.session_state.manager.filas[cor]
        if len(fila) > 0:
            pacientes_info = [p.to_dict() for p in fila._dados]
            st.markdown(
                f"**Fila {cor.upper()} ({descricao}) - {len(fila)} paciente(s):**"
            )
            st.dataframe(pacientes_info, hide_index=True)


if __name__ == "__main__":
    main()
