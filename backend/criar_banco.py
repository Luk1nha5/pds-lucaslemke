from app import app, db, Dono, Pet

with app.app_context():
    # Apaga as tabelas antigas para o script poder ser rodado de novo
    db.drop_all()
    db.create_all()

    donos = [
        Dono(nome="Ana Paula Ribeiro", telefone="45999110001"),
        Dono(nome="Bruno Cardoso", telefone="45999110002"),
        Dono(nome="Carla Meneghel", telefone="45999110003")
    ]

    db.session.add_all(donos)
    db.session.commit()

    # Os ids dos donos (1, 2, 3) ja foram gerados pelo commit
    pets = [
        Pet(nome="Rex", especie="cachorro", idade=4, dono_id=donos[0].id),
        Pet(nome="Mimi", especie="gato", idade=2, dono_id=donos[0].id),
        Pet(nome="Thor", especie="cachorro", idade=7, dono_id=donos[1].id),
        Pet(nome="Nina", especie="gato", idade=1, dono_id=donos[2].id),
        Pet(nome="Pingo", especie="passaro", idade=3, dono_id=donos[2].id)
    ]

    db.session.add_all(pets)
    db.session.commit()

    print("Banco criado com sucesso.")
    print(f"Foram inseridos {len(donos)} donos e {len(pets)} pets.")