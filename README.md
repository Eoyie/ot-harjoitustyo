# ExpireApp

Tällä sovelluksella voi pitää kirjaa elintarvikkeiden vanhentumisesta. Voit lisätä tuotteen jääkaappiin, pakastimeen tai kaappiin ja merkitä, kun se on joko käytetty tai vanhentunut. Voit myös muokata tuotteita tai nähdä ne kalenterissa. Sovelluksessa pystyy käyttämään eri käyttäjiä ja luoda/poistaa niitä.

## Dokumentaatio
[ Changelog ](dokumentaatio/changelog.md) ⋆｡°✩ [ Tuntikirjanpito ](dokumentaatio/tuntikirjanpito.md) ₊˚✩ [ Vaatimusmäärittely ](dokumentaatio/vaatimusmaarittely.md) ✩°｡⋆ [ Arkkitehtuuri ](dokumentaatio/arkkitehtuuri.md) ₊˚✩ [ Releasit ](https://github.com/Eoyie/ot-harjoitustyo/releases) ⋆｡°✩ [ Käyttöohje ](dokumentaatio/kayttoohje.md) ✩°｡⋆

## Asennus
1. Ladattuasi tiedoston koneelle, siirry terminaalissa tämän hakemistoon ja asenna riippuvuudet komennolla:

```
poetry install
```
2. Käynnistä ohjelma komennolla:
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
