# Hello World !!


# Importação de bibliotecas.
from datetime import datetime

# Estruturando os dados para o sistema.
class Produto:
    def __init__(self, nome, categoria, quantidade, preco, localizacao):
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.localizacao = localizacao

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

class Movimentacao:
    def __init__(self, tipo, produto, quantidade, data):
        self.tipo = tipo  #  Definir se é entrada ou saida => 'entrada' ou 'saida'
        self.produto = produto
        self.quantidade = quantidade
        self.data = data

# Estrutura do sistema de gerenciamento.
class SistemaGerenciamentoEstoque:
    def __init__(self):
        self.produtos = []
        self.categorias = {}
        self.movimentacoes = []

    # Cadastro de novos produtos.
    def cadastrar_produto(self, nome, categoria, quantidade, preco, localizacao):
        if categoria not in self.categorias:
            self.categorias[categoria] = Categoria(categoria)
        novo_produto = Produto(nome, categoria, quantidade, preco, localizacao)
        self.categorias[categoria].produtos.append(novo_produto)
        self.produtos.append(novo_produto)
        print(f"Produto '{nome}' cadastrado com sucesso.")

    # Consulta dos produtos inseridos no sistema.
    def consultar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return vars(produto)
        return f"Produto '{nome}' não encontrado."

    # Atualização dos produtos.
    def atualizar_estoque(self, nome, quantidade, tipo_movimentacao):
        for produto in self.produtos:
            if produto.nome == nome:
                if tipo_movimentacao == "entrada":
                    produto.quantidade += quantidade
                    print(f"Entrada de {quantidade} unidades de '{nome}' registrada.")
                elif tipo_movimentacao == "saida":
                    if produto.quantidade >= quantidade:
                        produto.quantidade -= quantidade
                        print(f"Saída de {quantidade} unidades de '{nome}' registrada.")
                    else:
                        print("Quantidade insuficiente em estoque para realizar a saída.")
                        return
                self.registrar_movimentacao(tipo_movimentacao, produto, quantidade)
                return
        print(f"Produto '{nome}' não encontrado.")

    # Em caso de entrada ou saida registrar a movimentação.
    def registrar_movimentacao(self, tipo, produto, quantidade):
        data_atual = datetime.now()
        movimentacao = Movimentacao(tipo, produto, quantidade, data_atual)
        self.movimentacoes.append(movimentacao)

    # Geração dos relatorios de estoque.
    def gerar_relatorio_estoque(self):
        relatorio = {
            "baixo_estoque": [],
            "excesso_estoque": [],
            "movimentacoes": []
        }
        for produto in self.produtos:
            if produto.quantidade < 5:
                relatorio["baixo_estoque"].append(vars(produto))
            elif produto.quantidade > 100:
                relatorio["excesso_estoque"].append(vars(produto))
        for mov in self.movimentacoes:
            relatorio["movimentacoes"].append({
                "tipo": mov.tipo,
                "produto": mov.produto.nome,
                "quantidade": mov.quantidade,
                "data": mov.data.strftime("%Y-%m-%d %H:%M:%S")
            })
        return relatorio

# Exemplo de uma utilização do sistema.
sistema = SistemaGerenciamentoEstoque()

# Cadastrando produtos.
sistema.cadastrar_produto("Produto A", "Categoria 1", 10, 15.0, "Estante 1")
sistema.cadastrar_produto("Produto B", "Categoria 2", 200, 30.0, "Estante 2")

# Consultando produtos.
print(sistema.consultar_produto("Produto A"))

# Atualizando o estoque.
sistema.atualizar_estoque("Produto A", 5, "entrada")
sistema.atualizar_estoque("Produto A", 3, "saida")

# Gerando o relatório.
relatorio = sistema.gerar_relatorio_estoque()
print("Relatório de Estoque:")
print(relatorio)
