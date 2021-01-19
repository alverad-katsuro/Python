def main():
    segundos_entrada = float(input ("""Quer saber quanto tempo vale os segundos?
\nDigite a quantidade de segundos: \n"""))

    horas = segundos_entrada // 3600
    minutos = segundos_entrada % 3600
    segundos = segundos_entrada % 60
    dias = horas // 24

    minutos1 = minutos // 60
    horas1 = (horas % 24)
    print("Vale ",int(dias),"dias", int(horas1),"horas",int(minutos1),"minutos e",int(segundos),"segundos")
    cont = "Sim"
    cont1 = "sim"
    cont2 = "s"
    sim = (input ("Deseja fazer outra conversão? \n Sim ou Não \n"))
    
    while sim == cont or sim == cont1 or sim == cont2:
        segundos_entrada = float(input ("""Quer saber quanto tempo vale os segundos?
\nDigite a quantidade de segundos: \n"""))
        horas = segundos_entrada // 3600
        minutos = segundos_entrada % 3600
        segundos = segundos_entrada % 60
        dias = horas // 24

        minutos1 = minutos // 60
        horas1 = (horas % 24)
        print("Vale ",int(dias),"dias", int(horas1),"horas",int(minutos1),"minutos e",int(segundos),"segundos")
        sim = (input ("Deseja fazer outra conversão? \n Sim ou Não \n"))

main()
