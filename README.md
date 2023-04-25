# ExpireApp

Tällä sovelluksella voi pitää kirjaa elintarvikkeiden vanhentumisesta ja tilasta. Voit lisätä tuotteen jääkaappiin, pakastimeen tai kaappiin ja merkitä, kun se on joko käytetty tai vanhentunut.
// **En vielä kirjoita asioita, jotka eivät ole ohjelmassa**

## Dokumentaatio
[ Changelog ](dokumentaatio/changelog.md) ⋆｡°✩ [ Tuntikirjanpito ](dokumentaatio/tuntikirjanpito.md) ₊˚✩ [ Vaatimusmäärittely ](dokumentaatio/vaatimusmaarittely.md) ✩°｡⋆ [ Arkkitehtuuri ](dokumentaatio/arkkitehtuuri.md) 

## Asennus
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
