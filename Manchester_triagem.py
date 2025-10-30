# SISTEMA DE TRIAGEM MANCHESTER
# o sistema vai definir de acordo com as respostas dos pacientes.
# também irá chamar os pacientes de acordo com sua prioridade.

class NodoArvore:
    def __init__(self, pergunta=None, cor=None, esquerda=None, direita=None):
        self.pergunta = pergunta
        self.cor = cor
        self.esquerda = esquerda
        self.direita = direita


class Fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if not self.vazia():
            return self.itens.pop(0)
        return None

    def vazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)


def montar_arvore():
    vermelho = NodoArvore(cor="Vermelho")
    laranja = NodoArvore(cor="Laranja")
    amarelo = NodoArvore(cor="Amarelo")
    verde = NodoArvore(cor="Verde")
    azul = NodoArvore(cor="Azul")

   
    febre_incomodo = NodoArvore("Tem febre alta (>39°C) ou incômodo persistente?", esquerda=azul, direita=amarelo)

    dor_intensa = NodoArvore("Está com dor intensa (p.ex. escala 8-10)?", esquerda=febre_incomodo, direita=amarelo)

    sinais_avc = NodoArvore("Apresenta sinais compatíveis com AVC (face caída / fala arrastada / fraqueza súbita)?", esquerda=dor_intensa, direita=vermelho)

    hemorragia = NodoArvore("Há hemorragia ativa que não está controlada (sangramento que não estanca)?", esquerda=sinais_avc, direita=vermelho)

    consciente = NodoArvore("Está consciente?", esquerda=laranja, direita=hemorragia)

    respirando = NodoArvore("O paciente está respirando?", esquerda=vermelho, direita=consciente)

    return respirando


def pergunta_simples(texto):
    while True:
        r = input(f"{texto} (s/n): ").strip().lower()
        if r in ("s", "n"):
            return r
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")


def pergunta_escala_dor():
    while True:
        resp = input("Em uma escala de 0 a 10, qual a intensidade da dor? ")
        resp = resp.strip()
        # validar dígito(s)
        if resp.isdigit():
            val = int(resp)
            if 0 <= val <= 10:
                return val
        print("Entrada inválida. Informe um número inteiro entre 0 e 10.")


def triagem(arvore):
    nodo_atual = arvore
    while nodo_atual.cor is None:
        texto = nodo_atual.pergunta
        if "dor intensa" in texto.lower():
            resposta = pergunta_simples(texto)
            if resposta == "s":
                escala = pergunta_escala_dor()
                if escala >= 8:
                    nodo_atual = nodo_atual.direita  
                else:
                    nodo_atual = nodo_atual.esquerda 
            else:
                nodo_atual = nodo_atual.esquerda
        else:
            r = pergunta_simples(texto)
            if r == "s":
                nodo_atual = nodo_atual.direita
            else:
                nodo_atual = nodo_atual.esquerda

    return nodo_atual.cor


def main():
    arvore = montar_arvore()

    filas = {
        "Vermelho": Fila(),
        "Laranja": Fila(),
        "Amarelo": Fila(),
        "Verde": Fila(),
        "Azul": Fila()
    }

    while True:
        print("\n SISTEMA DE TRIAGEM MANCHESTER ")
        print("1 - Cadastrar paciente")
        print("2 - Chamar paciente (será por prioridade)")
        print("3 - Mostrar status das filas dos pacientes")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            nome = input("Nome do paciente: ").strip()
            print("\nResponda às perguntas para triagem:")
            cor = triagem(arvore)
            filas[cor].enqueue(nome)
            print(f"\nCor atribuída: {cor}")
            print(f"Paciente {nome} adicionado à fila {cor}.")

        elif opcao == "2":
            ordem_prioridade = ["Vermelho", "Laranja", "Amarelo", "Verde", "Azul"]
            chamado = None
            fila_chamada = None
            for cor in ordem_prioridade:
                if not filas[cor].vazia():
                    chamado = filas[cor].dequeue()
                    fila_chamada = cor
                    print(f"\nChamando paciente da fila {cor}: {chamado}")
                    break
            if not chamado:
                print("\nNenhum paciente na fila!")

        elif opcao == "3":
            print("\n STATUS DAS FILAS ")
            for cor, fila in filas.items():
                print(f"{cor}: {fila.tamanho()} paciente(s)")

        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
