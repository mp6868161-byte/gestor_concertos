def programa_concerto_escola():
    # Dados imutáveis do evento
    agenda = {
        "Bon Jovi": {"hora": "18:00", "info": "Hard Rock clássico /."},
        "AC/DC": {"hora": "20:00", "info": "Rock n' Roll puro /."},
        "Aerosmith": {"hora": "22:00", "info": "Blues-Rock /."},
        "Linkin Park": {"hora": "00:00", "info": "Rock Alternativo /."}
    }

    while True:
        print("\n" + "="*35)
        print("="*35)
        print("1. Informações dos Artistas")
        print("2. Horário das Atuações")
        print("3. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\n--- SOBRE OS ARTISTAS ---")
            for banda, dados in agenda.items():
                print(f"{banda}: {dados['info']}")

        elif opcao == "2":
            print("\n--- HORÁRIOS ---")
            for banda, dados in agenda.items():
                print(f"{dados['hora']} -> {banda}")

        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    programa_concerto_escola()
