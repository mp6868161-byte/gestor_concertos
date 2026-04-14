# Lista para armazenar os artistas (substitui o GerenciadorArtistas)
artistas = []
proximo_id = 1


def criar_artista(nome, genero, nacionalidade, hora_concerto):
    global proximo_id
    # Criamos um dicionário para representar o artista
    novo_artista = {
        "id": proximo_id,
        "nome": nome,
        "genero": genero,
        "nacionalidade": nacionalidade,
        "hora_concerto": hora_concerto
    }
    artistas.append(novo_artista)
    proximo_id += 1
    print(f"'{nome}' adicionado ao lineup das {hora_concerto}!")


def listar_apenas_rock():
    print("\n--- LINEUP: PALCO ROCK ---")
    encontrou = False

    for artista in artistas:
        # Verificamos se 'rock' está na string do gênero
        if "rock" in artista["genero"].lower():
            # Formatação manual da string (substitui o __str__)
            print(f"[{artista['hora_concerto']}] ID: {artista['id']} | "
                  f"{artista['nome'].upper()} ({artista['genero']}) - "
                  f"{artista['nacionalidade']}")
            encontrou = True

    if not encontrou:
        print("Nenhum artista de Rock escalado ainda.")


# --- Execução ---

criar_artista("Jorge Ben Jor", "Samba-Rock", "Brasil", "21:00")
criar_artista("Arctic Monkeys", "Indie Rock", "UK", "23:30")
criar_artista("Daft Punk", "Eletrônica", "França", "01:00")
criar_artista("AC/DC", "Hard Rock", "Austrália", "22:00")

listar_apenas_rock()
