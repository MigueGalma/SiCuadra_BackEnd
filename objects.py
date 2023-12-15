class contacto:
    def __init__(self,nombre,apellido,email,direccion,localidad,provincia,codigopostal,codigo):
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.direccion=direccion
        self.localidad=localidad
        self.provincia=provincia
        self.codigopostal=codigopostal
        self.codigo=codigo
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email} {self.localidad} {self.provincia} {self.codigopostal} {self.codigo}"
      

# MEDIDAS QUE MANDA EL FORMULARIO TIPO DE DATOS RADIO:
# ORIENTACION:
#   INDIVIDUAL: "opcion1"
#   HORIZONTAL: "opcion2"
#   VERTICAL: "opcion3"
# MEDIDAS:
#   90 CM X 60 CM: "medida1"
#   75 CM X 70 CM: "medida2"
#   100 CM X 70 CM: "medida3"
#   150 CM X 70 CM: "medida4"     


def generarCodigo (orientacion,contacto):
    condiciones = (orientacion,contacto)
    match condiciones:
        case ("orientacion1","medida1"):
            codigo = 1090060
        case ("orientacion2","medida2"):
            codigo = 2075070
        case ("orientacion2","medida3"):
            codigo = 2100070
        case ("orientacion2","medida4"):
            codigo = 2150070
        case ("orientacion3","medida2"):
            codigo = 3075070
        case ("orientacion3","medida3"):
            codigo = 3100070
        case ("orientacion","medida4"):
            codigo = 3150070
    print("Tu codigo es: ", codigo)
    return codigo

"""
def ingresardatos():
    nombre = input('Ingresa tu nombre: ')
    apellido = input('Ingresa tu apellido: ')
    email = input('Ingresa tu email: ')
    direccion = input('Ingresa tu direccion: ')
    localidad = input('Ingresa tu localidad: ')
    provincia = input('Ingresa tu provincia: ')
    codigopostal = input('Ingresa tu codigo postal: ')
    orientacion = input('Ingresa tu orientacion: ')
    medidas = input('Ingresa tu medida: ')
    codigo = generarCodigo(orientacion,medidas)
    datos = contacto(nombre,apellido,email,direccion,localidad,provincia,codigopostal,codigo)
    print (datos)

"""
