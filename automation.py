import pyautogui as pygui
import pandas as pd

# 1 - Abrir o sistema para realizar o login e cadastrar os produtos

pygui.PAUSE = 2

pygui.press("win")
pygui.write("edge")
pygui.press("enter")
pygui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pygui.press("enter")

# 2 - Fazer o login

pygui.moveTo(503,396, 3)
pygui.click()
pygui.write("emailautomacao@email.com")
pygui.press("tab")
pygui.write("senhaemail")
pygui.press("enter")

# 3 - Importar a base dos produtos

products = pd.read_csv("products.csv")

# 4 - Cadastrar 1 produto

for product in products.index:
    # 5 - Repetir o processo de cadastrar 1 produto até que todos sejam cadastrados
    pygui.moveTo(505,279)
    pygui.click() # Primeiro campo dentro do formulário
     # pegar da tabela o valor do campo que a gente quer preencher
    codigo = products.loc[product, "codigo"]
    # preencher o campo
    pygui.write(str(codigo))
    # passar para o proximo campo
    pygui.press("tab")
    # preencher o campo
    pygui.write(str(products.loc[product, "marca"]))
    pygui.press("tab")
    pygui.write(str(products.loc[product, "tipo"]))
    pygui.press("tab")
    pygui.write(str(products.loc[product, "categoria"]))
    pygui.press("tab")
    pygui.write(str(products.loc[product, "preco_unitario"]))
    pygui.press("tab")
    pygui.write(str(products.loc[product, "custo"]))
    pygui.press("tab")
    obs = products.loc[product, "obs"]
    if not pd.isna(obs):
        pygui.write(str(products.loc[product, "obs"]))
    pygui.press("tab")
    pygui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pygui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim

