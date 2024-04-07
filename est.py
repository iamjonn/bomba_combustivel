def ab_preco(t, p):
    ab = 'preco'
    if t == 'gasolina':
        print(f'Abastecendo com gasolina a R$ {p:.2f}')
    elif t == 'alcool':
        print(f'Abastecendo com álcool a R$ {p:.2f}')
    elif t == 'diesel':
        print(f'Abastecendo com diesel a R$ {p:.2f}')
    else:
        print('Combustível inválido')
    return ab

def valor_comb(t, v):
    return {t: v}

def ab_litro(t, l):
    ab = 'litro'
    if t == 'gasolina':
        print(f'Abastecendo com {l:.2f} litros de gasolina')
    elif t == 'alcool':
        print(f'Abastecendo com {l:.2f} litros de álcool')
    elif t == 'diesel':
        print(f'Abastecendo com {l:.2f} litros de diesel')
    else:
        print('Combustível inválido')
    return ab

def ex_dados(valor_comb, ab):
    comb = list(valor_comb.keys())[0]
    preco_litro = valor_comb[comb]
    
    if ab == 'preco':
        valor_pago = float(input(f'Informe o valor pago por {comb}: '))
        litros_abastecidos = valor_pago / preco_litro
        valor_total = valor_pago
    elif ab == 'litro':
        litros_abastecidos = float(input(f'Informe a quantidade de litros de {comb} abastecidos: '))
        valor_total = litros_abastecidos * preco_litro
    else:
        print('Modo de abastecimento inválido')
        return
    
    print(f"Tipo de combustível: {comb}")
    print(f"Quantidade de litros: {litros_abastecidos:.2f}")
    print(f"Valor total: R$ {valor_total:.2f}")

def main():
    valor_comb = valor_comb('gasolina', 5.80)
    abastecimento = ab_preco('gasolina', 20)
    ex_dados(valor_comb, abastecimento)

if __name__ == "__main__":
    main()
