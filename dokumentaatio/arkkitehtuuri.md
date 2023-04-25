## Alustava pakkauskaavio

- Luultavasti molemmat alustavat kaaviot tulevat muuttumaan hieman. Ihan ulkonäön puolesta.

![Pakkausrakenne](./kuvat/Exp_alustava_pakkauskaavio.png)

## Alustava pakkaus/luokkakaavio
- ui jäänyt turha class osio. Tämäkin tulee muuttuumaan.

![Rakenne](./kuvat/alustava_paakaavio.png)

## Alustava luokkakaavio
- En tiedä lopullisia kommentojen nimiä :)
```mermaid
  classDiagram
    Exp "*" --> "1" User
    class Exp{
        - id
        - product
        - date
        - type
        add_Product()
        delete_product()
        set_expired()
        set_used()
     }
     class User{
        - username
        - password
        login(username, password)
        logout()
     }
```
## Sekvenssikaavio tuotteen lisäyksestä 

![Tuotteen lisäys](./kuvat/Exp_sekvenssikaavio.png)
