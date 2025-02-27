from tarjeta_credito import TarjetaCredito
from typing import Dict


class Usuario:

  
    def __init__(self, nombre, apellido, email,tarjetas_de_credito:  Dict[str, TarjetaCredito]):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.tarjetas_de_credito=tarjetas_de_credito

  
    def hacer_compra(self, monto,tarjeta):  #recibe como argumento el monto de la compra
       self.tarjetas_de_credito[tarjeta].compra(monto)
       return self
    
    def pagar_tarjeta(self, monto,tarjeta):
        self.tarjetas_de_credito[tarjeta].pago(monto)
        return self
      
    
    def mostrar_saldo_usuario(self):
        #self.tarjeta_credito.mostrar_info_tarjeta()
        print(f"Usuario: {self.nombre} {self.apellido}, Email: {self.email}")
        for tarjeta in self.tarjetas_de_credito.keys():
            print(f"Tarjeta: {tarjeta}")
            self.tarjetas_de_credito[tarjeta].mostrar_info_tarjeta()
        return self
       
    
    def transferir_deuda(self, otro_usuario, monto):
       pass
      
       
        
    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido}, Email: {self.email}, Límite de Crédito: {self.limite_credito}, Saldo a Pagar: {self.saldo_pagar}"
        
                

if __name__ =="__main__":
    tarjetas={
        "visa":TarjetaCredito(limite_credito=1000, intereses=0.2),
        "mastercard":TarjetaCredito(limite_credito=1500, intereses=0.1),
        "dinners":TarjetaCredito(limite_credito=2500, intereses=0.3)
    }
    usuario1=Usuario(nombre="juan", apellido="lopez", email="kdhjh@hormail.com", tarjetas_de_credito=tarjetas)
    
    usuario1.hacer_compra(1000,"visa")
    usuario1.mostrar_saldo_usuario()
    print("*****************")
    usuario1.pagar_tarjeta(500,"visa")
    usuario1.mostrar_saldo_usuario()
    
    tarjetas={
        "visa":TarjetaCredito(limite_credito=100, intereses=0.2),
        "mastercard":TarjetaCredito(limite_credito=1500, intereses=0.1),
    }
    print("*****************")
    usuario2=Usuario("Maria", "LOPEZ","EMAIL",tarjetas)
    usuario2.mostrar_saldo_usuario()
    
    
    
   
    
    
    
   