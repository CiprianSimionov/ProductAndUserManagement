from repository.products_repository import ProductsRepository
from repository.users_repository import UsersRepository



if __name__ == "__main__":
    product_repo = ProductsRepository()

#Adaugam/cream produse
    product_repo.create({"name": "Laptop",
                         "price": 5000,
                         "quantity": 3
                         })
    product_repo.create({"name": "Casti",
                         "price": 300,
                         "quantity": 5
                         })
    product_repo.create({"name": "Telefon",
                         "price": 2000,
                         "quantity": 20
                         })

    #Citim produse
    product_repo.read(0) #not available/ starting at index 1
    product_repo.read(1)
    product_repo.read(2)
    product_repo.read(3)

    #Actualizam produse
    product_repo.update(1,
        {
         "price": 700,
         "quantity": 5
         }
    )
    product_repo.update(3,
                        {
                         "quantity": 10
                         }
                        )

    #Stergem produse
    product_repo.delete(2)
    product_repo.read(2)

    # Adaugam/cream useri
    user_repo = UsersRepository()

    user_repo.create({
        "name": "user1",
        "email": "user1@yahoo.com",
        "password": "1234"
    })

    user_repo.create({
        "name": "user2",
        "email": "user2@yahoo.com",
        "password": "5678"
    })

    user_repo.create({
        "name": "user3",
        "email": "user3@yahoo.com",
        "password": "2468"
    })

    user_repo.read(1)
    user_repo.read(2)
    user_repo.read(3)

    # Actualizam useri
    user_repo.update(2,
                        {
                            "name": "user22",
                            "email": "user22@gmail.com"
                        }
                        )
    user_repo.update(3,
                        {
                            "name": "user33"
                        }
                        )

    user_repo.read(2)

    #Stergem useri

    user_repo.delete(3)
    user_repo.read(3)