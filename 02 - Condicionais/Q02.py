resposta = input("O programa funciona?\n")

if (resposta == "SIM"):
    resposta = input("Você entende o que fez?\n")
    if (resposta == "SIM"):
        print ("Ótimo. Então não mexe!")
    else:
        resposta = input ("Já foi na tutoria?\n")
        if (resposta == "SIM"):
            print ("Choremos!")
        else:
            print ("Temos um time a disposição!")
else:    
    resposta = input("Você sabe onde está o erro?\n")
    if (resposta == "SIM"):
        resposta = input ("Acha que pode solucionar sozinho?\n")
        if (resposta == "SIM"):
            print ("Então mão na massa!")
        else:
            resposta = input("Já pesquisou no Google?\n")
            if (resposta == "SIM"):
                resposta = input ("Já foi na tutoria?\n")
                if (resposta == "SIM"):
                    print ("Choremos!")
                else:
                    print ("Temos um time a disposição!")
            else:
                print ("Corre lá então!")
    else:
        resposta = input ("Já foi na tutoria?\n")
        if (resposta == "SIM"):
            print ("Choremos!")
        else:
            print ("Temos um time a disposição!")
