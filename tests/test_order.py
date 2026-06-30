"""
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
