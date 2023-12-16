class Consulta:
    def __init__(self,nroregistro,nombre,apellido,tematica,orientacion,medida,precio):
        self.nroregistro = nroregistro
        self.nombre = nombre
        self.apellido = apellido
        self.tematica = tematica
        self.orientacion = orientacion
        self.medida = medida
        self.precio = precio
       
    def __str__(self):
        return f" [nroregistro : {self.nroregistro}, 
                  nombre: {self.nombre},
                  apellido: {self.apellido},
                  tematica: {self.tematica},
                  orientacion: {self.orientacion},
                  medida: {self.medida},
                  precio: {self.precio}]"

# MEDIDAS QUE MANDA EL FORMULARIO TIPO DE DATOS RADIO:
# ORIENTACION:
#   INDIVIDUAL: "orientacion1"
#   HORIZONTAL: "orientacion2"
#   VERTICAL: "orientacion3"
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
        case ("orientacion3","medida4"):
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
