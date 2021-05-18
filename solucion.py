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
        impuestos = ((dineroextra * 20)/100)
    elif salarioBruto > 2000.00 and dineroextra > 500.00:
        impuestos = (((salarioBruto-2000)*30)/100) + (((500.00)*20)/100)
    else:
        impuestos = 0
    
    
    salarioNeto = round((salarioBruto - impuestos),2)

    diccionarioSalida = dict()
    diccionarioSalida ["id"] = id
    diccionarioSalida ["salarioBruto"] = salarioBruto
    diccionarioSalida ["impuestos"] = round(impuestos,2)
    diccionarioSalida ["salarioNeto"] = salarioNeto

    return diccionarioSalida

informacion1 = {"id":1, "tarifa":40, "numeroHoras": 40}
