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


def generarCodigo (contacto.orientacion, contacto.medidas):
    condiciones = (contacto.orientacion,contacto.medidas)
    match condiciones:
        case ("opcion1","medida1"):
            codigo = 1090060
        case ("opcion2","medida2"):
            codigo = 2075070
        case ("opcion2","medida3"):
            codigo = 2100070
        case ("opcion2","medida4"):
            codigo = 2150070
        case ("opcion3","medida2"):
            codigo = 3075070
        case ("opcion3","medida3"):
            codigo = 3100070
        case ("opcion3","medida4"):
            codigo = 3150070
    return codigo




