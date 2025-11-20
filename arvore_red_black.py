# Classe para implementar um nó da Árvore Vermelho-Preta
class NoRB:
    # Construtor
    def __init__(self, valor, cor='vermelho'):
        self.valor = valor
        self.cor = cor
        self.esquerda = None
        self.direita = None
        self.pai = None

    # Função para obter o avô do nó
    def avo(self):
        if self.pai is None:
            return None
        return self.pai.pai

    # Função para obter o irmão do nó
    def irmao(self):
        if self.pai is None:
            return None
        if self == self.pai.esquerda:
            return self.pai.direita
        return self.pai.esquerda

    # Função para obter o tio do nó
    def tio(self):
        if self.pai is None:
            return None
        return self.pai.irmao()

# Função para implementar a Árvore Vermelho-Preta
class ArvoreVermelhoPreta:
    # Construtor para inicializar a árvore
    def __init__(self):
        self.raiz = None

    # Função para buscar um valor na Árvore
    def buscar(self, valor):
        no_atual = self.raiz
        while no_atual is not None:
            if valor == no_atual.valor:
                return no_atual
            elif valor < no_atual.valor:
                no_atual = no_atual.esquerda
            else:
                no_atual = no_atual.direita
        return None

    # Função para inserir um nó na Árvore, similar à inserção em BST (Árvore Binária de Busca)
    def inserir(self, valor):
        # Inserção regular
        novo_no = NoRB(valor)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            no_atual = self.raiz
            while True:
                if valor < no_atual.valor:
                    if no_atual.esquerda is None:
                        no_atual.esquerda = novo_no
                        novo_no.pai = no_atual
                        break
                    else:
                        no_atual = no_atual.esquerda
                else:
                    if no_atual.direita is None:
                        no_atual.direita = novo_no
                        novo_no.pai = no_atual
                        break
                    else:
                        no_atual = no_atual.direita
        self.corrigir_insercao(novo_no)

    # Função para corrigir as propriedades da Árvore após inserção
    def corrigir_insercao(self, novo_no):
        while novo_no.pai and novo_no.pai.cor == 'vermelho':
            if novo_no.pai == novo_no.avo().esquerda:
                tio = novo_no.tio()
                if tio and tio.cor == 'vermelho':
                    novo_no.pai.cor = 'preto'
                    tio.cor = 'preto'
                    novo_no.avo().cor = 'vermelho'
                    novo_no = novo_no.avo()
                else:
                    if novo_no == novo_no.pai.direita:
                        novo_no = novo_no.pai
                        self.rotacao_esquerda(novo_no)
                    novo_no.pai.cor = 'preto'
                    novo_no.avo().cor = 'vermelho'
                    self.rotacao_direita(novo_no.avo())
            else:
                tio = novo_no.tio()
                if tio and tio.cor == 'vermelho':
                    novo_no.pai.cor = 'preto'
                    tio.cor = 'preto'
                    novo_no.avo().cor = 'vermelho'
                    novo_no = novo_no.avo()
                else:
                    if novo_no == novo_no.pai.esquerda:
                        novo_no = novo_no.pai
                        self.rotacao_direita(novo_no)
                    novo_no.pai.cor = 'preto'
                    novo_no.avo().cor = 'vermelho'
                    self.rotacao_esquerda(novo_no.avo())
        self.raiz.cor = 'preto'

    # Função para remover um valor da Árvore
    def remover(self, valor):
        no_para_remover = self.buscar(valor)

        if no_para_remover is None:
            return

        if no_para_remover.esquerda is None or no_para_remover.direita is None:
            self._substituir_no(
                no_para_remover, no_para_remover.esquerda or no_para_remover.direita)
        else:
            sucessor = self._encontrar_minimo(no_para_remover.direita)
            no_para_remover.valor = sucessor.valor
            self._substituir_no(sucessor, sucessor.direita)

        self.corrigir_remocao(no_para_remover)

    # Função para corrigir as propriedades da Árvore após remoção
    def corrigir_remocao(self, x):
        while x != self.raiz and x.cor == 'preto':
            if x == x.pai.esquerda:
                irmao = x.irmao()
                if irmao.cor == 'vermelho':
                    irmao.cor = 'preto'
                    x.pai.cor = 'vermelho'
                    self.rotacao_esquerda(x.pai)
                    irmao = x.irmao()
                if (irmao.esquerda is None or irmao.esquerda.cor == 'preto') and (irmao.direita is None or irmao.direita.cor == 'preto'):
                    irmao.cor = 'vermelho'
                    x = x.pai
                else:
                    if irmao.direita is None or irmao.direita.cor == 'preto':
                        irmao.esquerda.cor = 'preto'
                        irmao.cor = 'vermelho'
                        self.rotacao_direita(irmao)
                        irmao = x.irmao()
                    irmao.cor = x.pai.cor
                    x.pai.cor = 'preto'
                    if irmao.direita:
                        irmao.direita.cor = 'preto'
                    self.rotacao_esquerda(x.pai)
                    x = self.raiz
            else:
                irmao = x.irmao()
                if irmao.cor == 'vermelho':
                    irmao.cor = 'preto'
                    x.pai.cor = 'vermelho'
                    self.rotacao_direita(x.pai)
                    irmao = x.irmao()
                if (irmao.esquerda is None or irmao.esquerda.cor == 'preto') and (irmao.direita is None or irmao.direita.cor == 'preto'):
                    irmao.cor = 'vermelho'
                    x = x.pai
                else:
                    if irmao.esquerda is None or irmao.esquerda.cor == 'preto':
                        irmao.direita.cor = 'preto'
                        irmao.cor = 'vermelho'
                        self.rotacao_esquerda(irmao)
                        irmao = x.irmao()
                    irmao.cor = x.pai.cor
                    x.pai.cor = 'preto'
                    if irmao.esquerda:
                        irmao.esquerda.cor = 'preto'
                    self.rotacao_direita(x.pai)
                    x = self.raiz
        x.cor = 'preto'

    

    # Função para rotação à esquerda
    def rotacao_esquerda(self, no):
        filho_direita = no.direita
        no.direita = filho_direita.esquerda

        if filho_direita.esquerda is not None:
            filho_direita.esquerda.pai = no

        filho_direita.pai = no.pai

        if no.pai is None:
            self.raiz = filho_direita
        elif no == no.pai.esquerda:
            no.pai.esquerda = filho_direita
        else:
            no.pai.direita = filho_direita

        filho_direita.esquerda = no
        no.pai = filho_direita

    # Função para rotação à direita
    def rotacao_direita(self, no):
        filho_esquerda = no.esquerda
        no.esquerda = filho_esquerda.direita

        if filho_esquerda.direita is not None:
            filho_esquerda.direita.pai = no

        filho_esquerda.pai = no.pai

        if no.pai is None:
            self.raiz = filho_esquerda
        elif no == no.pai.direita:
            no.pai.direita = filho_esquerda
        else:
            no.pai.esquerda = filho_esquerda

        filho_esquerda.direita = no
        no.pai = filho_esquerda

    # Função para substituir um nó antigo por um novo
    def _substituir_no(self, no_antigo, novo_no):
        if no_antigo.pai is None:
            self.raiz = novo_no
        else:
            if no_antigo == no_antigo.pai.esquerda:
                no_antigo.pai.esquerda = novo_no
            else:
                no_antigo.pai.direita = novo_no
        if novo_no is not None:
            novo_no.pai = no_antigo.pai

    # Função para encontrar o nó com valor mínimo em uma subárvore
    def _encontrar_minimo(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

    # Função para realizar o percurso em ordem (in-order)
    def _percurso_em_ordem(self, no):
        if no is not None:
            self._percurso_em_ordem(no.esquerda)
            print(no.valor, end=" ")
            self._percurso_em_ordem(no.direita)


# Código principal para teste
if __name__ == "__main__":
    arvore = ArvoreVermelhoPreta()
    arvore.inserir(10)
    arvore.inserir(20)
    arvore.inserir(30)
    arvore.inserir(40)
    arvore.inserir(50)
    arvore.inserir(25)

    print("Percurso em ordem da Árvore Vermelho-Preta:")
    arvore._percurso_em_ordem(arvore.raiz)
    print()

    arvore.remover(20)

    print("Percurso em ordem da Árvore Vermelho-Preta após remover 20:")
    arvore._percurso_em_ordem(arvore.raiz)
    print()