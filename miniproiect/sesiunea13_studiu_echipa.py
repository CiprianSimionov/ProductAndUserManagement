"""
EXERCITII WORKSHOP (Sesiunea 13)
"""

"""
CONTINUARE MINI PROIECT OOP GESTIONARE PRODUSE SI UTILIZATORI
"""

"""
5. Implementeaza clasa User:
- parametri constructor: user_id, name, email, password
- atribute pe obiect: user_id, name, email, password (ATRIBUT PRIVAT)

- implementeaza o metoda privata, numita validate_password, in care sa verifici:
    - daca parola contine cel putin o litera mare
    - daca parola contine cel putin un numar
    - daca parola contine cel putin 7 caractere
- apeleaza metoda de validate parola in constructor, astfel incat de fiecare data
cand se va crea un user nou, parola acestuia sa fie validata.
NOTA: Trateaza cazul in care parola nu poate fi validata (recomandare: utilizare exceptii)
"""


"""
6. Implementeaza clasa UsersRepository:
- va implementa interfata RepositoryInterface
- va avea in constructor un atribut pe obiect, numit users
! Acesta nu va primi valoare din constructor, ci va fi o lista goala.

- implementeaza metodele cerute de interfata implementata:
    - create():
        - primeste ca parametru un dictionar, care contine datele despre un user
        - creeaza un obiect din clasa User cu datele venite din dictionar
        ! Asigura-te ca id-ul user-ului il generezi tu, avand in vedere urmatoarea pozitie
ce o va ocupa in lista de utilizatori (users)
        - adauga obiectul creat in atributul users.
    - read():
        - primeste ca parametru id-ul user-ului pentru care dorim sa obtinem informatii
        - verifica daca user-ul se afla in lista de utilizatori:
            - daca da, afiseaza un mesaj in consola cu caracteristicile acestuia
            - daca nu, afiseaza un mesaj in consola "The user with id {id} is not available."
    - update():
        - primeste doi parametri: id-ul user-ului pe care dorim sa il actualizam si un dictionar
cu noile date
        - gaseste user-ul in lista de users, dupa id
        - daca user-ul a fost gasit, actualizeaza-l
        - trateaza si cazul in care user-ul nu a fost gasit.
    - delete():
        - primeste un parametru: id-ul user-ului pe care dorim sa il stergem
        - gaseste user-ul in lista de users, dupa id
        - daca user-ul a fost gasit, sterge-l
        - trateaza si cazul in care user-ul nu a fost gasit.
"""


"""
7. Creeaza o instanta din clasa UsersRepository si:
- adauga useri
- citeste detalii despre anumiti useri
- actualizeaza useri
- sterge useri
"""
