import random 

xptotal = 0
historico = []
nomeHeroi = input("Digite o nome do herói: ")
print("Bem-vindo, " + nomeHeroi + "!")

def classificar_nivel(xp):
    if xp < 1000:
        return "Ferro"
    elif xp < 2000:
        return "Bronze"
    elif xp < 5000:
        return "Prata"
    elif xp < 7000:
        return "Ouro"
    elif xp < 8000:
        return "Platina"
    elif xp < 9000:
        return "Ascendente"
    elif xp < 10000:
        return "Imortal"
    else:
        return "Radiante"
nivel = classificar_nivel(xptotal)

while True:
    batalhar = input("Você deseja batalhar? (s/n): ")
    if batalhar.lower() == 's':
        print("Você entrou em uma batalha!")
        print("Batalhando...")
        
        resultado = random.choice(["vencer", "perder"])

        if resultado == "vencer":
            xpganho = random.randint (50, 300)
            xptotal += xpganho
            print("Parabéns! Você venceu a batalha!")
            print("Você ganhou " + str(xpganho) + " pontos de experiência!")
        else: 
            resultado == "perder"
            xpganho = -random.randint (10, 50)
            xptotal += xpganho
            print("Você perdeu a batalha.") 
            print("Você perdeu " + str(-xpganho) + " pontos de experiência.")

        historico.append({
            "resultado": resultado,
            "xp": xpganho,
        })
    
    else:
        print("Você decidiu não batalhar. Até a próxima!")
        break

nivel = classificar_nivel(xptotal)
print("O herói de nome " + nomeHeroi + " está no nível " + classificar_nivel(xptotal) + ".")
print("\nHistórico de batalhas:")
for i, batalha in enumerate( historico, 1):
    status = "venceu" if batalha["xp"] > 0 else "perdeu"
    print(f"Batalha {i}: Você {status} e {'ganhou' if batalha['xp'] > 0 else 'perdeu'} {abs(batalha['xp'])} pontos de experiência.")
