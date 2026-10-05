# Entregável 1 — Aprendendo a ser um programador

**ENZO MONACO**

## Objetivo

Este projeto verifica se um robô possui bateria suficiente para realizar uma missão.

O programa recebe a bateria atual, a duração prevista da missão e o consumo de bateria por minuto. Em seguida, calcula o consumo total e informa se a missão pode ser concluída.

Quando a bateria é suficiente, o programa mostra a bateria restante. Quando não é suficiente, mostra quantos pontos percentuais de bateria faltam.

## Requisitos

- Python 3
- Terminal Linux

## Estrutura do projeto

```text
entregavel-1-enzo-monaco/
├── README.md
├── src/
│   └── missao.py
└── imagens/
    └── terminal.png
```

## Exemplo de execução

A partir da pasta principal do repositório:

```bash
>> python3 src/missao.py

Bateria atual (%): 80
Duração da missão (minutos): 10
Consumo por minuto (%): 3

>> Missão pode ser concluída. Bateria restante: 50.00%.
```