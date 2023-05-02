# Arkkitehtuurikuvaus
**Tulen uudistamaan molemmat kuvat lopulliseen työhön!**
## Rakenne

Ohjelman rakenne noudattelee kolmitasoista kerrosarkkitehtuuria. Tämä kuva näyttää pakkausrakenteen ja jokaisen pakkauksen sisällöt ovat mainituna tämän alla.

![Pakkausrakenne](./kuvat/Exp_alustava_pakkauskaavio.png)

Kyseiset pakkaukset sisältävät näiden alueiden koodit:

- ui = käyttöliittymä
- services = sovelluslogiikka
- repositories = pysyväistallennus
- entities = sovelluksen käyttämiä objekteja kuvaamaan tuotteita (myöhemmin myös käyttäjiä)

## Käyttöliittymä
**Tämä tulee muuttumaan käyttäjän lisäämisen myötä, joten en kirjoita paljoa**
- Product-lista
- Kalenteri

 
## Sovelluslogiikka

Sovelluslogiikka toimii seuraavasti luokkakaaviossa näytettyjen luokkien User ja Exp kanssa:

```mermaid
  classDiagram
    Exp "*" --> "1" User
    class Exp{
        - id
        - product
        - date
        - type
        add_product()
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

Itse toiminnallisuudesta vastaa ExpService, joka käyttää näitä luokkia. Luokkakaaviossa on näytetty joitakin kommentoja, joita molemmilla luokilla on mitä ExpService käyttää.

### Tulen varmaan vaihtamaan luokkakaavion sisältämään myös ExpServicen, koska itse Exp luokallahan ei ole kommentoja. Tämä siis muuttuu!!

## Repositories
**Tämäkin muuttuu...**
ExpRepository tallentaa tuotteet CSV-tiedostoon.

### Tiedostot

CVS-tiedostoon tallennetut tuotteet ovat seuraavaa formaattia:
```
a93eabc9-5b0a-40d6-8ac8-af2cfb8ee431;Testi;02-05-2023;0 
```
Sisältö vastaa seuraavaa: id ; tuotteen nimi ; vanhentumis päivämäärä ; tila (0 = jääkaappi, 1 = pakaste, 2 = kaappi, 3 = vanhentunut, 4 = käytetty) ; *tulevaisuudessa käyttäjä*

## Kokonaisuus

Tässä vielä luokka/pakkauskaavio, joka kuvastaa ohjelman kokonaisuutta:
![Pakkausrakenne](./kuvat/alustava_paakaavio.png)

## Päätoiminnallisuudet

### Paljon lisää tänne

### Tuotteen lisääminen

Tuotteen tietojen antamisen jälkeen painaen "Add Product" seuraava tapahtuu sovelluksessa sekvenssikaaviolla kuvattuna:

![Tuotteen lisäys](./kuvat/Exp_sekvenssikaavio.png)
