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
