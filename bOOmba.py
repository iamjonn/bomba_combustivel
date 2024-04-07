class BombaCombustivel:
    def __init__(self):
        self.comb_preco = {}

    def cad_combustivel(self, tipo, valor):
        self.comb_preco[tipo] = valor

    def ab_preco(self, tipo, preco):
        if tipo not in self.comb_preco:
            print("Tipo de combustível não cadastrado.")
            return

        litros_abastecidos = preco / self.comb_preco[tipo]
        self.ultimo_abastecimento = (tipo, preco, litros_abastecidos, 'preco')
        return litros_abastecidos

    def ab_litro(self, tipo, litros):
        if tipo not in self.comb_preco:
            print("Tipo de combustível não cadastrado.")
            return

        valor_pago = litros * self.comb_preco[tipo]
        self.ultimo_abastecimento = (tipo, valor_pago, litros, 'litro')
        return valor_pago

    def ex_dados(self):
        if not hasattr(self, 'ultimo_abastecimento'):
            print("Nenhum abastecimento foi realizado ainda.")
            return

        tipo, valor_pago, quantidade, modo_abastecimento = self.ultimo_abastecimento
        if modo_abastecimento == 'preco':
            print(f"Tipo de combustível: {tipo}")
            print(f"Quantidade de litros: {quantidade:.2f}")
            print(f"Valor total: R$ {valor_pago:.2f}")
        elif modo_abastecimento == 'litro':
            print(f"Tipo de combustível: {tipo}")
            print(f"Quantidade de litros: {quantidade:.2f}")
            print(f"Valor total: R$ {valor_pago:.2f}")
        else:
            print('Modo de abastecimento inválido')


def main():
    bomba = BombaCombustivel()
    bomba.cad_combustivel('gasolina', 5.80)
    bomba.ab_preco('gasolina', 90)
    bomba.ex_dados()

if __name__ == "__main__":
    main()
