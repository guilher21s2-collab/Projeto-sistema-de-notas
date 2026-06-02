# Sistema de Notas - IFB Asa Sul

## Descrição

O Sistema de Notas é um programa desenvolvido em Python com o objetivo de cadastrar alunos, registrar disciplinas, notas e faltas, calcular a média final e gerar um relatório informando a situação do estudante (aprovado ou reprovado).

O sistema foi desenvolvido utilizando conceitos fundamentais da programação, como funções, listas, dicionários, estruturas de repetição e estruturas condicionais.

---

## Funcionalidades

* Cadastro do nome do aluno;
* Cadastro do nível de ensino (Fundamental II ou Médio);
* Cadastro de múltiplas disciplinas;
* Registro de notas e faltas para cada disciplina;
* Cálculo da média geral das notas;
* Cálculo do total de faltas;
* Geração de relatório final;
* Verificação automática da situação do aluno.

---

## Regras de Aprovação

O aluno será considerado **Aprovado** quando:

* Média final maior ou igual a 6,0;
* Total de faltas inferior a 16.

O aluno será considerado **Reprovado** quando:

* Média final menor que 6,0;
* Ou possuir quantidade de faltas acima do limite permitido.

---

## Estrutura do Programa

### cadastrar_dados()

Responsável por:

* Receber o nome do aluno;
* Receber o nível de ensino;
* Solicitar a quantidade de disciplinas;
* Cadastrar nome, nota e faltas de cada disciplina;
* Armazenar os dados em uma lista de dicionários.

### calcular_notas(disciplinas)

Responsável por:

* Somar as notas cadastradas;
* Calcular a média geral do aluno.

### calcular_faltas(disciplinas)

Responsável por:

* Somar todas as faltas registradas nas disciplinas.

### gerar_relatorio_final()

Responsável por:

* Exibir os dados do aluno;
* Mostrar as disciplinas cadastradas;
* Mostrar média final e total de faltas;
* Informar a situação final do aluno.

---

## Tecnologias Utilizadas

* Python 3
* Funções
* Listas
* Dicionários
* Estruturas de repetição (`for`)
* Estruturas condicionais (`if`, `elif`, `else`)

---

## Exemplo de Uso

```text
Digite o nome do aluno: João
Qual nível de ensino? [Fundamental II / Médio]: Médio
Quantas matérias deseja cadastrar? 2

Disciplina 1
Digite o nome da disciplina: Matemática
Nota final: 8
Quantidade de faltas: 3

Disciplina 2
Digite o nome da disciplina: Português
Nota final: 7
Quantidade de faltas: 4
```

### Saída

```text
-----==== Relatório Final ====-----

Aluno: João
Nível de escolaridade: Médio

Disciplinas Cadastradas:

Matemática | Nota: 8.0 | Faltas: 3
Português | Nota: 7.0 | Faltas: 4

Média Final: 7.50

Total de faltas: 7

Aprovado!
```

---

## Objetivo Educacional

Este projeto foi desenvolvido com fins educacionais para praticar conceitos básicos e intermediários da linguagem Python, especialmente o uso de funções, estruturas de dados e lógica de programação.
