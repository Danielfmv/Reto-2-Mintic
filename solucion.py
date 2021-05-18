def nomina(informacion:dict) -> dict:
    tarifa = float(informacion["tarifa"])
    numeroHoras = float(informacion["numeroHoras"])
    id = str(informacion["id"])

    if numeroHoras > 35:
        horasextra = numeroHoras - 35 
        tarifaextra = (tarifa * 1.5) * horasextra
        salarioBruto = round(((tarifa * 35) + tarifaextra),2) 
    else:
        salarioBruto = round((numeroHoras * tarifa),2)
    
    dineroextra = salarioBruto - 1500.00
    
    if salarioBruto > 1500.00 and dineroextra <= 500.00:
        impuestos = round(((dineroextra * 20)/100),2)
    else:
        if salarioBruto > 1500.00 and dineroextra > 500.00:
            impuestos = round(((dineroextra * 30)/100),2)
        else:
            impuestos = 0
    
    salarioNeto = round((salarioBruto - impuestos),2)

    diccionarioSalida = dict()
    diccionarioSalida ["id"] = id
    diccionarioSalida ["salarioBruto"] = float(salarioBruto)
    diccionarioSalida ["impuestos"] = impuestos
    diccionarioSalida ["salarioNeto"] = float(salarioNeto)

    return diccionarioSalida

informacion1 = {"id":1, "tarifa":50.5, "numeroHoras": 40}
print(nomina(informacion1))
