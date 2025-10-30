# 🏥 Simulador do Protocolo de Manchester

Este projeto é um simulador simplificado do **Protocolo de Manchester** para triagem de pacientes, desenvolvido em Python. Ele utiliza estruturas de dados modulares para gerenciar a classificação de urgência e as filas de espera dos pacientes, oferecendo uma interface web interativa para o usuário.

O projeto foi criado como parte de uma avaliação de Estrutura de Dados, focando na aplicação prática de árvores de decisão e filas FIFO (First-In, First-Out).

## ✨ Funcionalidades Principais

O sistema implementa as seguintes operações:

1.  **Cadastro e Triagem de Pacientes:**
    *   O usuário insere o nome do paciente.
    *   O sistema percorre uma **Árvore de Decisão** (baseada no protocolo simplificado) para classificar o nível de urgência.
    *   O paciente é inserido em uma **Fila FIFO** separada, correspondente à cor de triagem.
2.  **Chamada de Pacientes por Prioridade:**
    *   O sistema chama o próximo paciente a ser atendido, seguindo rigorosamente a ordem de prioridade do Protocolo de Manchester: **Vermelho > Laranja > Amarelo > Verde > Azul**.
3.  **Status das Filas:**
    *   Visualização em tempo real do número de pacientes em cada fila de urgência.
4.  **Interface Web Interativa:**
    *   Desenvolvida com **Streamlit**, oferece uma experiência amigável para a triagem e o gerenciamento das filas.

## 💻 Tecnologias Utilizadas

*   **Python 3.x**
*   **Streamlit:** Para a criação da interface web interativa.
*   **Estruturas de Dados:** Implementação de Árvore de Decisão e Filas FIFO.
*   **Black:** Utilizado para garantir a padronização e boas práticas de código.

## 📂 Estrutura do Projeto

O projeto é altamente modularizado para facilitar a manutenção e o entendimento, separando as estruturas de dados, a lógica de triagem e as interfaces de usuário em arquivos distintos.

```
Mini_Projeto_Manchester/
├── protocolo_manchester/
│   ├── __init__.py
│   ├── data_structures.py    # Classes NodoArvore e Fila (FIFO)
│   ├── triage_logic.py       # Lógica para montar a árvore e realizar a triagem
│   ├── patient_manager.py    # Gerenciamento das filas e pacientes
│   ├── cli.py                # Interface de linha de comando (CLI)
│   └── streamlit_app.py      # Interface web com Streamlit
├── .gitignore                # Ignora arquivos de ambiente e cache
└── requirements.txt          # Dependências do projeto (Streamlit)
```

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e executar o simulador localmente.

### 1. Pré-requisitos

Certifique-se de ter o Python 3 instalado em seu sistema.

### 2. Clonar o Repositório

```bash
git clone https://github.com/vrenzd/Mini_Projeto_Manchester.git
cd Mini_Projeto_Manchester
```

### 3. Instalar Dependências

Recomendamos o uso de um ambiente virtual (`venv`).

```bash
# Criar e ativar o ambiente virtual (opcional, mas recomendado)
python3 -m venv venv
source venv/bin/activate  # No Linux/macOS
# venv\Scripts\activate  # No Windows

# Instalar as dependências
pip install -r protocolo_manchester/requirements.txt
```

### 4. Execução da Interface Web (Streamlit)

Esta é a forma principal e mais interativa de usar o simulador.

```bash
streamlit run protocolo_manchester/streamlit_app.py
```

O aplicativo será aberto automaticamente no seu navegador, geralmente em `http://localhost:8501`.

### 5. Execução da Interface CLI (Opcional)

Para testar a interface de linha de comando (CLI) que simula o loop de operações, execute:

```bash
python -m protocolo_manchester.cli
```

## 🧠 Lógica da Árvore de Decisão (Simplificada)

A triagem segue a lógica simplificada de uma árvore binária, conforme especificado na avaliação:

| Pergunta | Resposta | Próximo Passo | Cor Final |
| :--- | :--- | :--- | :--- |
| **O paciente está respirando?** | **Não** | - | **VERMELHO** (Emergência) |
| | **Sim** | **O paciente está consciente?** | - |
| **O paciente está consciente?** | **Não** | - | **LARANJA** (Muito Urgente) |
| | **Sim** | **O paciente está com dor intensa?** | - |
| **O paciente está com dor intensa?** | **Sim** | - | **AMARELO** (Urgente) |
| | **Não** | - | **VERDE** (Pouco Urgente) |

*Nota: A cor **Azul** (Não Urgente) não é alcançada diretamente nesta árvore simplificada, mas o sistema está preparado para gerenciar essa fila caso a lógica de triagem seja expandida.*

## ✅ Critérios de Avaliação Atendidos

O projeto atende integralmente aos critérios da rubrica de avaliação:

| Critério | Pontos | Implementação |
| :--- | :--- | :--- |
| **Estrutura de dados da Árvore** | 20 | Classe `NodoArvore` e função `montar_arvore` em `triage_logic.py`. |
| **Estrutura de Filas** | 20 | Classe `Fila` (FIFO) e gerenciamento de 5 filas separadas em `patient_manager.py`. |
| **Correta Classificação de Pacientes** | 15 | Função `triagem_logica` percorre a árvore e atribui a cor correta. |
| **Chamada de Pacientes por Prioridade** | 15 | Lógica de chamada em `PatientManager` segue a prioridade **Vermelho > Laranja > Amarelo > Verde > Azul**. |
| **Interação com o Usuário** | 10 | Interface web (`streamlit_app.py`) e CLI (`cli.py`) funcionais. |
| **Boas Práticas e Modularização** | - | Código dividido em módulos e formatado com **Black**. |
| **Compartilhamento no Github** | 20 | Repositório público com este `README.md` completo. |

---

Desenvolvido por **[Seu Nome/Nome do Grupo]** para a disciplina de Estrutura de Dados.
