# 🚀 Automação de Cadastro de Produtos (RPA)

Este projeto é uma automação desenvolvida para cadastrar produtos em um sistema web do evento da Hashtag Treinamentos de forma automatizada, utilizando a biblioteca **PyAutoGUI** para manipulação da interface do usuário e **Pandas** para manipulação de dados.

## 💻 Tecnologias Utilizadas

### 📊 Linguagem
- **Python**: Linguagem principal utilizada para desenvolver o script de automação.

### 🔧 Bibliotecas
- **PyAutoGUI**: Responsável por simular interações com o sistema operacional e aplicativos, como cliques e preenchimento de formulários.
- **Pandas**: Utilizada para manipulação da base de dados dos produtos, que está armazenada em um arquivo CSV.

## 🚀 Objetivo
Automatizar o cadastro de produtos em um sistema web, eliminando a necessidade de entrada manual de dados e aumentando a eficiência e precisão do processo.

## 🔬 Áreas Abordadas

- **Automação de Processos Repetitivos (RPA)**: Este projeto exemplifica o uso de RPA para realizar tarefas repetitivas e propensas a erros.
- **Manipulação de Dados**: Utilização da biblioteca Pandas para carregar, processar e acessar dados armazenados em um arquivo CSV.
- **Interação com Interfaces Gráficas**: Demonstra como controlar interfaces de usuário programaticamente para preencher formulários e navegar em aplicações web.

## 🔄 Fluxo do Programa

1. **Abrir o navegador e acessar o sistema:**
   - O script abre o navegador **Microsoft Edge** e acessa a página de login do sistema web fornecido.

2. **Realizar o login:**
   - Preenche os campos de e-mail e senha e autentica no sistema.

3. **Importar a base de dados:**
   - Lê os dados de produtos a partir de um arquivo `products.csv` usando a biblioteca Pandas.

4. **Cadastrar produtos:**
   - Para cada produto na base de dados:
     - Preenche os campos do formulário com os dados correspondentes do CSV (código, marca, tipo, categoria, preço unitário, custo, observações).
     - Submete o formulário e repete o processo até que todos os produtos sejam cadastrados.

## 🛠️ Configuração do Ambiente

1. 🔧 **Clone ou baixe o repositório do projeto:**
   ```bash
   git clone https://github.com/Robert-Cortez-Rudi/Automacao_cadastro_produtos
   cd Automacao_cadastro_produtos
   ```

2. 🪜 **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate # Linux/Mac
   .venv\Scripts\activate   # Windows
   ```

3. 🔄 **Instale as dependências necessárias:**
   ```bash
   pip install pyautogui pandas
   ```

4. 🔐 **Certifique-se de que o arquivo `products.csv` está configurado corretamente e na mesma pasta do script.**

5. 🔁 **Execute o script:**
   ```bash
   python automation.py
   ```

## 🖭 Observações

- É recomendável testar o script em um ambiente controlado antes de executá-lo em produção para evitar erros ou comportamentos inesperados.
- Ajuste os tempos de pausa (`pyautogui.PAUSE`) conforme a capacidade de resposta do sistema.
- Certifique-se de que as coordenadas usadas no script correspondem à resolução e layout do sistema usado.

## ✨ Possíveis Melhorias

- Implementar uma interface gráfica para facilitar a seleção e validação da base de dados.
- Utilizar OCR (reconhecimento óptico de caracteres) para capturar dados diretamente de imagens ou PDFs.
- Melhorar a segurança ao lidar com credenciais, utilizando bibliotecas como `keyring` para armazenar senhas com segurança.

## 📢 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## 👤 Autor

Desenvolvido por [Robert Cortez Rudi](https://github.com/Robert-Cortez-Rudi).


