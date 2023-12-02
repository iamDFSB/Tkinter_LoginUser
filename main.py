from model.manipulate_dados import Integre_Banco
import json


caminho = r'C:\Users\daniel.sbatista\Documents\Estudo\Projetos_Python\Aprendendo Python\tkinter_project\view\user_data.json'

with open(caminho,'r') as arqv:
    arqv_dicio = json.load(arqv)
    nome = arqv_dicio['Nome']['0']
    telefone = arqv_dicio['Telefone']['0']
    email = arqv_dicio['Email']['0']
    description = arqv_dicio['Descricao']['0']
    
obj = Integre_Banco(nome=nome,telefone=telefone,email=email,description=description)
# obj.criar_banco()
obj.inserir_no_banco()