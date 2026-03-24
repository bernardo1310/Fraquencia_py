"""
Analise estatistica de idades.
Coleta idades digitadas pelo usuario, organiza em rol e exibe as frequencias.
"""

from collections import Counter


class Coletor:
    """
    Responsavel por conversar com o usuario e pegar as idades que ele digitar.
    """

    def coletar(self):
        """
        Fica pedindo idades pro usuario ate ele digitar 'fim'.
        Cada idade digitada vai sendo guardada numa lista.
        Se o usuario digitar algo que nao seja numero, avisa e pede de novo.
        No final, devolve a lista com todas as idades coletadas.
        """
        idades = []
        print("Digite as idades. Para encerrar, digite 'fim'.")
        while True:
            entrada = input("Idade: ")

            # usuario quer parar
            if entrada == "fim":
                if len(idades) == 0:
                    print("Informe ao menos uma idade.")
                    continue
                break

            # usuario digitou algo que nao e numero
            if not entrada.isdigit():
                print("Digite um numero inteiro valido.")
                continue

            # tudo certo, adiciona na lista
            idades.append(int(entrada))

        return idades


class Estatisticas:
    """
    Recebe a lista de idades e faz todos os calculos estatisticos.
    Assim que a classe e criada, ja calcula tudo automaticamente.
    """

    def __init__(self, idades):
        """
        Aqui e onde tudo acontece assim que o objeto e criado.
        Recebe a lista de idades e ja calcula o rol e todas as frequencias.
        """
        self.total = len(idades)                    # quantas idades foram digitadas
        self.rol = sorted(idades)                   # idades em ordem crescente, com repeticao

        contagem = Counter(idades)                  # conta quantas vezes cada idade aparece
        self.valores = sorted(contagem.keys())      # lista dos valores unicos em ordem

        # frequencia absoluta: quantas vezes cada idade apareceu
        self.freq_abs = {v: contagem[v] for v in self.valores}

        # frequencia acumulada: soma progressiva da frequencia absoluta
        self.freq_acu = self._acumulada(self.freq_abs)

        # frequencia relativa: a fatia percentual de cada idade no total
        self.freq_rel = {v: contagem[v] / self.total for v in self.valores}

        # frequencia relativa acumulada: soma progressiva da frequencia relativa
        self.freq_rel_acu = self._acumulada(self.freq_rel)

    def _acumulada(self, freq):
        """
        Recebe qualquer dicionario de frequencias e transforma numa versao acumulada.
        Ou seja, cada linha passa a somar tudo que veio antes dela tambem.
        Funciona tanto pra frequencia absoluta quanto pra relativa.
        """
        acumulada = {}
        soma = 0
        for v in self.valores:
            soma += freq[v]
            acumulada[v] = soma
        return acumulada


class Exibidor:
    """
    Responsavel por pegar os resultados calculados e mostrar na tela de forma organizada.
    """

    def __init__(self, stats):
        """
        Recebe o objeto de estatisticas que ja tem tudo calculado.
        """
        self.stats = stats

    def exibir(self):
        """
        Mostra tudo na tela: primeiro o rol, depois a tabela de frequencias.
        Cada linha da tabela corresponde a uma idade unica que foi digitada.
        """
        s = self.stats

        # exibe o rol
        print("\nROL")
        print(", ".join(str(i) for i in s.rol))

        # exibe o cabecalho da tabela
        print("\nIdade  F.Abs  F.Acum  F.Rel   F.Rel.Acum")

        # exibe uma linha por valor unico
        for v in s.valores:
            print(
                f"{v:<7}{s.freq_abs[v]:<7}{s.freq_acu[v]:<8}"
                f"{s.freq_rel[v]:<8.2%}{s.freq_rel_acu[v]:.2%}"
            )

        # exibe o total de idades informadas
        print(f"\nTotal de idades: {s.total}")


class Programa:
    """
    Classe principal que junta tudo e faz o programa rodar na ordem certa.
    """

    def executar(self):
        """
        Passo a passo do programa:
        1. Coleta as idades com o Coletor
        2. Calcula as estatisticas com a classe Estatisticas
        3. Exibe os resultados com o Exibidor
        """
        coletor = Coletor()
        idades = coletor.coletar()

        stats = Estatisticas(idades)

        Exibidor(stats).exibir()


# ponto de entrada: so roda se o arquivo for executado diretamente
if __name__ == "__main__":
    Programa().executar()