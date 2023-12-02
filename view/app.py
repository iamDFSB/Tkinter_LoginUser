from tkinter import *
import pandas as pd
import pathlib,os

caminho_arquivo = pathlib.Path(os.path.dirname(__file__))
caminho_json = pathlib.Path('user_data.json')
caminho_main = caminho_arquivo / caminho_json

def get_dados() -> None:
    # dicio = {
    #     "Nome": inserir_nome.get(),
    #     "Telefone": inserir_telefone.get(),
    #     "Email": inserir_email.get(),
    #     "Descricao": inserir_description.get("1.0", END).strip(),
    # }
    df = pd.DataFrame({
        "Nome": [inserir_nome.get()],
        "Telefone": [inserir_telefone.get()],
        "Email": [inserir_email.get()],
        "Descricao": [inserir_description.get("1.0", END).strip()]
    })
    df.to_json(caminho_main,indent=3)

    return df

app = Tk()
# Configurando o titulo:
app.title("Dados Usuario")

# Tamanho da tela:
app.geometry("500x400")

# Configurações:
app.configure(background="#7D95BC")

# Escrevendo algo na tabela:
# Nome:
nome = Label(
    app,
    text="Insira seu nome:",
    background="#D4DCE9",
    foreground="#5171A5",
    anchor="center",
)
nome.place(x=180, y=10, width=130, height=30)
# Input nome:
inserir_nome = Entry(app)
inserir_nome.place(x=180, y=50, width=130, height=20)

# Telefone:
telefone = Label(
    app,
    text="Digite seu telefone:",
    background="#D4DCE9",
    foreground="#5171A5",
    anchor="center",
)
telefone.place(x=180, y=90, width=130, height=30)
# Input telefone:
inserir_telefone = Entry(app)
inserir_telefone.place(x=180, y=130, width=130, height=20)

# Email:
email = Label(
    app,
    text="Digite seu email:",
    background="#D4DCE9",
    foreground="#5171A5",
    anchor="center",
)

email.place(x=180, y=170, width=130, height=30)
# Input email:
inserir_email = Entry(app)
inserir_email.place(x=180, y=210, width=130, height=20)

# Descrição:
description = Label(
    app,
    text="Fale mais sobre você:",
    background="#D4DCE9",
    foreground="#5171A5",
    anchor="center",
)

description.place(x=180, y=250, width=130, height=30)
# Input descrição:
inserir_description = Text(app)
inserir_description.place(x=180, y=290, width=130, height=50)


# Botão:
button = Button(text="Enviar", command=get_dados)
button.place(x=180, y=350, width=130, height=34)

app.mainloop()
