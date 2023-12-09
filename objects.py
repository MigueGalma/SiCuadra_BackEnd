class contacto:
    def __init__(self,nombre,apellido,email,direccion,localidad,provincia,codigopostal,orientacion,medidas):
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.direccion=direccion
        self.localidad=localidad
        self.provincia=provincia
        self.codigopostal=codigopostal
        self.orientacion=orientacion
        self.medidas=medidas
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email} {self.localidad} {self.provincia} {self.codigopostal} {self.orientacion} {self.medidas}"
    def __del__(self):
        print("El registro se ha cargado en la base de datos")

