# Käyttöohje

## Ohjelman käynnistäminen

1. Ladattuasi tiedoston koneelle, siirry terminaalissa tämän hakemistoon ja asenna riippuvuudet komennolla:

```
poetry install
```
2. Ja käynnistä ohjelma komennolla:
```
poetry run invoke start
```
## Käyttäjät

Käyttäjät toimivat varsin yksinkertaisesti. Eli voit lisätä käyttäjän ja lisättyäsi valita sen listasta ja mennä tuote näkymään. Käyttäjän voi myös poistaa.

## Tuotteiden lisäys

Voit lisätä tuotteen "Add Product:" osiosta näin:

- Kirjoita tuotteen nimi kohtaan "Product:"

- Valitse onko se jääkaappi-, pakastin- vai kaappi tavaraa kohdasta "Type:".

- Anna tuotteen parasta ennen/viimeinen käyttöpäivä kohdassa "Expiry date:".
  - Kohta avaa kalenteri osuuden, josta valitset päivän ja painat "Submit".
  
- Ja paina vielä "Add Product".

## Tuotteiden muu käsittely

- Voit merkata tuotteen vanhetuneeksi valitsemalla tuotteen listasta ja painamalla "Product Expired".

- Voit merkata tuotteen käytetyksi valitsemalla tuotteen listasta ja painamalla "Product Used".

- Voit poistaa tuotteen kokonaan valitsemalla tuotteen listasta ja painamalla "Delete Product".
  - HOX! Nämä 3 kommentoa voi tehdä monelle tuotteelle, jos ne valitaan shiftin avulla.
 
- Qty toimii seuraavasti: Voit valita haluatko, että jokaista tuotetta käytetään kaikki "All", jolloin ohjelma ei huomioi qty:n laitettua määrää, "Each", jolloin jokaiselta valitulta tuotteelta lähtee haluttu määrä ja "Total" jolloin tämä miinustaa ylhäältä alas niin monta kertaa yhteensä, eli voi käyttää jonkin tuotteen kokonaan ja toisen ei yhtään.

- **Jos lista on pidempi, kuin tämän ikkuna** voit liikkua listassa ylös ja alas käyttämällä näppäimistön nuolinäppäimiä.

- Voit myös editoida tuotteita valitsemalla se listasta ja painamalla "Edit Product"

## Komentorivitoiminnot

- Ohjelma suoritetaan komennolla:
```
poetry run invoke start
```
- Ohjelman testit suoritetaan komennolla:
```
poetry run invoke test
```
- Ohjelman testikattavuuden saat generoitua komennolla, joka generoi raportin htmlcov-hakemistoon:
```
poetry run invoke coverage-report
```
- Pylint tarkistukset saat komennolla:
```
poetry run invoke lint
```

