Aula 17 — Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos — LocalEats

👥 Integrantes

NomeGitHubFelipe Ponciano@P0ncianoChristiano Dias Ferraz@ChristianoFerrazLucas Devantier Pinto@Devantier2002Anthony Martins de Castro@anthonymcastr

🔹 1. Repositório da Atividade

ItemDescriçãoNome do repositóriolocaleats-ci-aula17Link do repositóriohttps://github.com/P0nciano/localeats-ci-aula17

Estrutura de diretórios utilizada:

localeats-ci-aula17/
├── tests/
│   └── test_order.py
├── .github/
│   └── workflows/
│       └── quality.yml
├── order.py
├── pytest.ini
└── requirements.txt

🔹 2. Planejamento da Funcionalidade

ItemDescriçãoTítulo da IssueCalcular total do pedido com taxa de entregaObjetivo da funcionalidadeSomar o valor dos itens do pedido e aplicar a taxa de entrega (R$ 7,90), concedendo frete grátis para pedidos a partir de R$ 50,00.Link da Issuehttps://github.com/P0nciano/localeats-ci-aula17/issues/1

🔹 3. Teste Automatizado

ItemDescriçãoTipo de testeUnitárioObjetivo do testeValidar o cálculo do total do pedido em 4 cenários: frete padrão, frete grátis, pedido vazio (deve lançar erro) e item com preço negativo (deve lançar erro).Link para o arquivo do testehttps://github.com/P0nciano/localeats-ci-aula17/blob/main/tests/test_order.py

Código do teste:

python"""
Testes unitários para a funcionalidade de cálculo de total de pedido - LocalEats
"""

import pytest
from order import calcular_total_pedido


def test_total_com_frete_padrao():
    """Pedido abaixo de R$ 50,00 deve somar a taxa de entrega padrão."""
    itens = [15.00, 10.00]
    total = calcular_total_pedido(itens)
    assert total == 32.90  # 25.00 + 7.90


def test_total_com_frete_gratis():
    """Pedido igual ou acima de R$ 50,00 deve ter frete grátis."""
    itens = [30.00, 25.00]
    total = calcular_total_pedido(itens)
    assert total == 55.00


def test_pedido_vazio_lanca_excecao():
    """Pedido sem itens deve lançar ValueError."""
    with pytest.raises(ValueError):
        calcular_total_pedido([])


def test_item_com_preco_negativo_lanca_excecao():
    """Item com preço negativo deve lançar ValueError."""
    with pytest.raises(ValueError):
        calcular_total_pedido([10.00, -5.00])

🔹 4. Pipeline de Integração Contínua

ItemDescriçãoNome do workflowQuality CIEvento que dispara a execuçãopush e pull_request na branch mainLink para o arquivo do workflowhttps://github.com/P0nciano/localeats-ci-aula17/blob/main/.github/workflows/quality.ymlLink de uma execução do workflowhttps://github.com/P0nciano/localeats-ci-aula17/actions/runs/28476495244

Código do workflow:

yamlname: Quality CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout do código
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Instalar dependências
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Rodar testes
        run: pytest -v

🔹 5. Indicadores de Qualidade

IndicadorValorQuantidade de testes executados4Quantidade de testes aprovados4Quantidade de testes com falha0Status final do pipeline✅ Sucesso

🔹 6. Registro de Defeito

ItemDescriçãoTítulo do defeitoPedido com item de preço negativo não era validadoSeveridadeMédiaLink da Issuehttps://github.com/P0nciano/localeats-ci-aula17/issues/2

Descrição breve:
O defeito identificado foi a ausência de validação para itens com preço negativo no cálculo do total do pedido, o que poderia gerar valores incorretos para o cliente. Ele foi identificado durante a escrita dos testes automatizados, ao se pensar em casos de borda da função calcular_total_pedido. A correção foi feita adicionando uma verificação que lança uma exceção ValueError sempre que algum item possuir valor negativo. O teste test_item_com_preco_negativo_lanca_excecao cobre esse cenário e garante que o defeito não volte a ocorrer.
