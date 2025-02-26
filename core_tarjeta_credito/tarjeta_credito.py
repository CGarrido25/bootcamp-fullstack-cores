class TarjetaCredito:

   #Incluye en este método valores por default

   def __init__(self, limite_credito, intereses,saldo_pagar=0):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses= intereses
       
       
   def compra(self, monto):
        if monto > (self.limite_credito-self.saldo_pagar):
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        else:
            self.saldo_pagar += monto
        return self
    
  

   def pago(self, monto):
       self.saldo_pagar -= monto
       return self
  

   def mostrar_info_tarjeta(self):
       print("Saldo a pagar: ", self.saldo_pagar)
       return self

  

   def cobrar_interes(self):
       self.saldo_pagar += self.saldo_pagar * self.intereses
       return self
   
   def __str__(self):
       return (f"*************\n"
                f"Saldo a pagar: {self.saldo_pagar}\n"
                f"Limite de credito: {self.limite_credito}\n"
                f"Intereses: {self.intereses}\n"
                f"Saldo disponible: {self.limite_credito - self.saldo_pagar}\n"
                f"*************")

if __name__ == "__main__":
    # crear una instancia de la clase TarjetaCredito
    tarjeta1 = TarjetaCredito(limite_credito=1000, intereses=0.2)
    tarjeta2 = TarjetaCredito(limite_credito=1500, intereses=0.1)
    tarjeta3 = TarjetaCredito(limite_credito=2500, intereses=0.3)
    
    tarjeta1.compra(500)
    tarjeta1.compra(300)
    tarjeta1.cobrar_interes()
    tarjeta1.mostrar_info_tarjeta()
    
    tarjeta2.compra(100).compra(200).compra(300).pago(100).pago(200).cobrar_interes().mostrar_info_tarjeta()
    
    tarjeta3.compra(500).compra(500).compra(500).compra(500).compra(501).mostrar_info_tarjeta()
    
    print(tarjeta1)
    print(tarjeta2)
    print(tarjeta3)