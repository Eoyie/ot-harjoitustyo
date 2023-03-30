## Osia joista en ole varma onko ne oikein:
- Jätin 1, * jne. käyttämättä, sillä en kunnolla ymmärtänyt niiden merkitystä.. Mutta olettaisin, että vain playerillä on numero
- Enkä ollut 100% mihin suuntaan laittaa nuolet netistä tutkiessani se vaihteli??
- Yleisesti en ole varma onko tässä niin tärkeää ja tarkkaa miten asiat on esitetty. Esim. Alussa pidin mukana int, bool, str kommentojen kohdalla, mutta poistin ne. Pääosin siitä syystä, että en ole edes varma pitikö ns. kommentoja kirjoittaa? Mutta yleisesti tein kaaviosta minulle helpompi ymmärtää, jonka uskon olevan pääasia (+ yleinen muoto)?
- En erikseen laittanut "Pelinappula sijaitsee aina yhdessä ruudussa.", koska ajattelin playerMovin hoitavan tämän?
- En tiennyt pitäisikö tile yhdistää vain boardin kautta vai myös pääluokan nyt on ns. molemmat.
- Tile luokassa jokaiselle checkTileClass vai kaikki samassa? Mielestäni yksi voisi palauttaa kaikki.
- Kaikille Tile luokille erikseen - kohdat? Laitoin vain kommennot.
- Income oletettu, että jokainen tile tietää omansa.

## Monopoly luokkakaavio
```mermaid
 classDiagram
      Player -->  Monopoly
      Monopoly <--  Board
      Monopoly <--  Dice
      Board <--  Tile
      Tile <-- StartTile
      Tile <-- Prison
      Tile <-- Chance
      Tile <-- CommunityChest
      Chance <-- Deck
      CommunityChest <-- Deck
      Tile <-- Tax
      Tile <-- Ownables
      Ownables <-- Street
      Ownables <-- Railroad
      Ownables <-- Utilities
      class Player{
          - username
          - piece
          - bank
          - cardList
          createPlayer()
          pickPiece()
      }
      class Monopoly{
          - playersList[2,8]
          - currentPlayer
          - playerPiece[1]
          - board[1]
          - dice
          - tile
          getNumOfPlayers()
          getPlayerPiece()
          getBoard()
          rollDice()
          checkTile()
          playerMove()
          checkMoney()
          useCard()
      }
      class Board{
          - board[40]
          - currentTile[name,pos,type]
          - neighbourTile
          makeBoard() #?
          getCurrentTile()
          getNeighbourTile()
      }
      class Dice{
          - Dices[2]
          roll()
      }
      class Tile{
          - tileName
          - tilePos
          - tileType
          checkTile()
      }
      class StartTile{
           startMoney()
           newRoundMoney()
      }
      class Prison{
           inPrisonRoll()
           visit()
           useCard()
      }
      class Chance{
           drawChance()
      }
      class CommunityChest{
           drawCommunityChest()
      }
      class Tax{
           payTax()
      }
      class Ownables{
           - price
           - owner
           makeContract()
           checkOwner()
      }
      class Street{
           - name
           - building[0,4]
           - hotel[1]
           - income[1,5]
           - value
           street()
           buy()
           build()
           sell()
           close()
           visitorPay()
      }
      class Railroad{
           - income[1,4]
           - value
           railroad()
           buy()
           sell()
           close()
           visitorPay()
      }
      class Utilities{
           - income[1,2]
           - value
           utilities()
           buy()
           sell()
           close()
           visitorPay()
      }
      class Deck{
           - cardType
           - cardPile
           draw()
           putBack()
      }
```
