# Käyttöohje

## Sisäänkirjautuminen (Tulevaisuudessa)

- 

## Ohjelman käynnistäminen

1. Ladattuasi tiedoston koneelle, siirry terminaalissa tämän hakemistoon ja asenna riippuvuudet komennolla:

```
poetry install
```

2. Alusta ohjelma käyttöä varten komennolla:
```
poetry run invoke build
```
3. Ja viimeisenä käynnistä ohjelma komennolla:
```
poetry run invoke start
```

## Tuotteiden lisäys

Voit lisätä tuotteen "Add Product:" osiosta näin:

- Kirjoita tuotteen nimi kohtaan "Product:"

- Valitse onko se jääkaappi-, pakastin- vai kaappi tavaraa kohdasta "Type:".

- Anna tuotteen parasta ennen/viimeinen käyttöpäivä kohdassa "Expiry date:".
  - Kohta avaa kalenteri osuuden, josta valitset päivän ja painat "Submit".
  
- Ja paina vielä "Add Product".

## Tuotteiden muu käsittely

**Tällä hetkellä**

- Voit merkata tuotteen vanhetuneeksi valitsemalla tuotteen listasta ja painamalla "Product Expired".

- Voit merkata tuotteen käytetyksi valitsemalla tuotteen listasta ja painamalla "Product Used".

- Voit poistaa tuotteen kokonaan valitsemalla tuotteen listasta ja painamalla "Delete Product".

- **Jos lista on pidempi, kuin tämän ikkuna** voit liikkua listassa ylös ja alas käyttämällä näppäimistön nuolinäppäimiä. (Luultavasti lisään myös scrollbarin)

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

