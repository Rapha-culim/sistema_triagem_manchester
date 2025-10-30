📄 Resumo README: Sistema de Triagem Manchester
Este projeto implementa uma simulação simplificada do Sistema de Triagem de Manchester em Python, utilizando uma estrutura de árvore de decisão para classificar a prioridade dos pacientes (cores) e filas para gerenciar a ordem de atendimento com base nessa prioridade.

🌟 **Funcionalidades Principais**
Triagem Baseada em Árvore de Decisão: O sistema utiliza uma árvore de perguntas sequenciais (classe NodoArvore) para guiar o usuário através do protocolo de triagem e determinar a cor de prioridade do paciente.

Priorização por Cor: A cor atribuída segue o padrão de prioridade do protocolo Manchester (Vermelho, Laranja, Amarelo, Verde, Azul).

Filas de Atendimento (FIFO): Pacientes são alocados em filas específicas para cada cor (classe Fila).

Chamar Paciente por Prioridade: A funcionalidade "Chamar paciente" sempre verifica e retira o paciente da fila de maior prioridade que não estiver vazia, garantindo o atendimento prioritário.

Entrada de Dados Validada: Possui funções (pergunta_simples, pergunta_escala_dor) para validar as respostas do usuário, especialmente a escala de dor (0 a 10).

💻 **Estrutura do Código**
NodoArvore:

Representa um nó na árvore de decisão.

Pode ser uma pergunta (nó interno, cor é None) ou uma cor final de prioridade (folha).

Possui links para esquerda (geralmente "Não") e direita (geralmente "Sim").

Fila:

Implementação simples de uma estrutura de dados de fila (FIFO - First-In, First-Out) usando listas Python.

Métodos: enqueue (adicionar), dequeue (remover), vazia, tamanho.

montar_arvore():

Função responsável por construir a árvore de decisão completa do protocolo, definindo a sequência de perguntas e os nós de cor final.

Funções de Interação:

pergunta_simples(texto): Pede uma resposta "s" (sim) ou "n" (não).

pergunta_escala_dor(): Pede um número inteiro de 0 a 10 para a escala de dor.

triagem(arvore):

Percorre a árvore de decisão interativamente.

Lida com a lógica especial para a pergunta da "dor intensa", onde a resposta "sim" exige uma verificação na escala de dor (≥8 para prioridade mais alta).

Retorna a cor final de prioridade.

main():

Controla o menu de interação principal do sistema.

Gerencia o dicionário de filas por cor.

Executa as opções de Cadastro, Chamada por Prioridade e Status das Filas.

🚀 **Como Usar (Menu)**
O programa roda em linha de comando e oferece as seguintes opções:

Cadastrar paciente: Inicia o processo de triagem (triagem()) para um novo paciente, atribui uma cor e o adiciona à fila correspondente.

Chamar paciente: Verifica as filas na ordem de prioridade (Vermelho → Laranja → Amarelo → Verde → Azul) e remove o primeiro paciente encontrado na fila de maior prioridade.

Mostrar status das filas dos pacientes: Exibe a contagem de pacientes em cada fila de cor.

Sair: Encerra o programa.

📝 **Observações**
O sistema é uma simulação funcional para fins didáticos e não deve ser usado em ambientes clínicos reais.

A ordem e a lógica das perguntas na árvore simulam uma parte do protocolo de Manchester para fins de classificação de risco.
