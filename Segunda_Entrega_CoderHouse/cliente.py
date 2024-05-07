class Cliente:
    def __init__(self, name, mail, address, phone):
        self.name = name
        self.email = mail
        self.address = address
        self.phone = phone
        self.last_purchase = None
        self.total_purchases = 0

    def register_purchase(self, buy):
        self.last_purchase = buy
        self.total_purchases += 1

    def __str__(self):
        return (f"Cliente {self.name}, Correo: {self.email}, Dirección: {self.address}, "
                f"Última Compra: {self.last_purchase}, Total de Compras: {self.total_purchases}")

    def __len__(self):
        return len(self.name)


