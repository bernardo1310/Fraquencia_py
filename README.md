# frequencia_idades.py

Programa simples que coleta idades digitadas pelo usuario e mostra uma analise estatistica basica dessas idades.

---

## O que ele faz

Voce digita quantas idades quiser, uma por vez. Quando terminar, digita `fim`. O programa entao mostra:

- **Rol** — todas as idades que voce digitou em ordem crescente
- **Frequencia absoluta** — quantas vezes cada idade apareceu
- **Frequencia acumulada** — a soma progressiva das frequencias
- **Frequencia relativa** — a porcentagem que cada idade representa no total
- **Frequencia relativa acumulada** — a soma progressiva das porcentagens

---

## Como rodar

Precisa ter Python 3 instalado. Depois e so:

```
python3 frequencia_idades.py
```

Digite as idades uma por uma e quando quiser encerrar, escreva `fim`.

---

## Como foi pensado o desenvolvimento

A ideia era deixar o codigo organizado em responsabilidades bem separadas, sem misturar o que cada parte faz.

Por isso foram criadas 4 classes:

**Coletor** — unica responsabilidade e falar com o usuario. Fica num loop pedindo idades, valida se o que foi digitado e um numero de verdade, e so termina quando o usuario digitar `fim`.

**Estatisticas** — recebe a lista de idades e faz todos os calculos. Quando o objeto e criado, ja sai calculando o rol, a contagem de cada valor e todas as frequencias. Tem um metodo auxiliar `_acumulada` que serve tanto pra frequencia absoluta quanto pra relativa, evitando repetir codigo.

**Exibidor** — so exibe. Recebe o objeto de estatisticas pronto e formata tudo na tela. Nao calcula nada, so mostra.

**Programa** — e o maestro. Chama o Coletor, passa o resultado pras Estatisticas, passa o resultado pro Exibidor. Tres linhas, uma responsabilidade.

Essa separacao foi proposital: se amanha voce quiser mudar como os dados sao coletados, mexe so no Coletor. Se quiser mudar como aparece na tela, mexe so no Exibidor. Nada interfere no outro.

---

## Requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa, tudo da biblioteca padrao do Python
