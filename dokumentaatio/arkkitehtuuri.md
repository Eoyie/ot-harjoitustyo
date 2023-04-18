## Alustava pakkauskaavio

![Pakkausrakenne](./kuvat/alustava_pakkauskaavio.png)

## Luokkakaavio

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
        expired_Product()
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
