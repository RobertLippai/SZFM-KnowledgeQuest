# Fizikai rendszerterv - szoftverarchitektúra


### Rendszerelemek:
1. GameState
2. TimerManager
3. ScoreManager
4. QuestionBank
5. Flask Webserver

### Flask Webserver
Az egész webesalkalmazás erre épül. Fogadja, teljesíti, feldogozza a http kéréseket. Összekapcsolja a megjelenítési, logikai, adat elérési rétegeket. Az alkalmazás moduljait egybefogja. 
A GameState alapján a megfelelő menürendszert megjeleníti.
 
Háttérbeli folyamat hajt végre (visszaszámáló óra, pontszám), aminek az eredményét a felhasználói felület megtudja jeleníteni.

Webes erőforrásutvonalakkal rendelkezik amik egy részét a felhasználó, más részét a játékfolyamat használja.


A Flask web framework-öt használja, valamint a GameState, ScoreManager, TimerManager, QuestionBank modulokat. 

### GameState
A játékmenetet, játéklogikát vezérli. A konstruktorban egy témát megkap, ami alapján a megfelelő témájú kérdéseket kéri le a kérdésbankból. Tárolja a már feltett kérdéseket, a játékos pontszámát, hátralévőidőt és a játék újrakezdését is ő végzi.

A ScoreManager, TimerManager modult használja, valamint a beépített Set típust.

### TimerManager
Az elindított kvíz során megjelenő visszaszámláló óráért felelős. Tárolja a hátralévő időt, visszaállítható játék újrakezdésekort, egyedi értékkel indítható.

A Flask Webserver-en egy saját elérési utvonala van, ami jQuery kérés segítségével másodpercenként megvan hívva, hogy frissítse a hátralévő időt. A meghívás során a GameState-en keresztül történik a kérés végrehajtása.

Nem használ semmilyen extra modult.


### ScoreManager
Ez a modul tárolja a játékos pontszmát. Tudja növelni a pontszámot, visszadja a jelenlegi pontszámot és vissza tudja állítani a pontszámot.

Nem használ semmilyen extra modult.

### QuestionBank
A JSON formátumban tárolt kérdések betöltéséért és rendszerezéséért felelős. A GameState rajta keresztül tud egy bizonoy témakörhöz kapcsolódó új kérdéseket kérni. Figyeli, hogy ugyanazt a kérdést ne adja és, hogy véletlenszerű sorrendbe legyenek a kérdések.

A Python JSON és Random moduljára támaszkodik, valamint a beépített Set típusra.