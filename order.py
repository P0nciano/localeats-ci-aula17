"""
Módulo de cálculo de pedido - LocalEats
Funcionalidade: calcular o valor total de um pedido, somando os itens
e aplicando a taxa de entrega. Pedidos acima de R$ 50,00 têm frete grátis.
"""

FRETE_PADRAO = 7.90
VALOR_MINIMO_FRETE_GRATIS = 50.00


def calcular_total_pedido(itens: list[float]) -> float:
    """
    Calcula o valor total de um pedido.

    Args:
        itens: lista com o preço de cada item do pedido.

    Returns:
        Valor total do pedido (itens + taxa de entrega, se aplicável).

    Raises:
        ValueError: se a lista de itens estiver vazia ou contiver valores negativos.
    """
    if not itens:
        raise ValueError("O pedido precisa ter pelo menos um item.")

    if any(preco < 0 for preco in itens):
        raise ValueError("Não é permitido item com preço negativo.")

    subtotal = sum(itens)

    if subtotal >= VALOR_MINIMO_FRETE_GRATIS:
        frete = 0.0
    else:
        frete = FRETE_PADRAO

    total = round(subtotal + frete, 2)
    return total
