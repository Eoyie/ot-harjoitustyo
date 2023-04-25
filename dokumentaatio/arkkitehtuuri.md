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
        - status
        add_Product()
        delete_Product()
        set_product_expired()
        get_Product_List()
        get_Usabled_Product_List()
        get_Spoiled_Product_List()
        get_Used_Product_List()
     }
     class User{
        - username
        - password
        login(username, password)
        logout()
     }
```
## Sekvenssikaavio tuotteen lisäyksestä 

![Tuotteen lisäys](./kuvat/Exp_Sekvenssikaavio.jpeg)
