class Artista:
    def __init__(self, id, nome, genero, nacionalidade, hora_concerto):
        self.id = id
        self.nome = nome
        self.genero = genero
        self.nacionalidade = nacionalidade
        self.hora_concerto = hora_concerto

    def __str__(self):
        return (f"[{self.hora_concerto}] ID: {self.id} | {self.nome.upper()} "
                f"({self.genero}) - {self.nacionalidade}")


class GerenciadorArtistas:
    def __init__(self):
        self.artistas = []
        self.proximo_id = 1

    def criar_artista(self, nome, genero, nacionalidade, hora_concerto):
        novo_artista = Artista(self.proximo_id, nome, genero, nacionalidade, hora_concerto)
        self.artistas.append(novo_artista)
        self.proximo_id += 1
        print(f" '{nome}' adicionado ao lineup das {hora_concerto}!")

    def listar_apenas_rock(self):
        print("\n---  LINEUP: PALCO  ---")
        encontrou = False
        # Filtra ignorando maiúsculas/minúsculas
        for artista in self.artistas:
            if "rock" in artista.genero.lower():
                print(artista)
                encontrou = True

        if not encontrou:
            print("Nenhum artista de Rock escalado ainda.")



crud = GerenciadorArtistas()

# Adicionando artistas com o novo campo de hora
crud.criar_artista("Jorge Ben Jor", "Samba-Rock", "Brasil", "21:00")
crud.criar_artista("Arctic Monkeys", "Indie Rock", "UK", "23:30")
crud.criar_artista("Daft Punk", "Eletrônica", "França", "01:00")
crud.criar_artista("AC/DC", "Hard Rock", "Austrália", "22:00")

crud.listar_apenas_rock()
