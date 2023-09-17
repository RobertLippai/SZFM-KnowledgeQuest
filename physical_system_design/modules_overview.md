# Fizikai rendszerterv - programspecifikációk (modulvázak)

###  Flask Web Server
Erre épül a webesalkalmazás. A bejövő kéréseket a megfelelő erőforrásutvonalakra irányítja és válaszokat közvetíti.

HTTTP kéréseket fogad amikre HTTP válaszokat ad. A válaszokat JSON formátumban közvetíti. Rendering templates segítségével pedig a felhasználói felületet megjeleníti.

**Elérési utvonalak:**

* check_answer: ellenőrzi a kérdésre adott válasz helyességét. Helyes válasz esetén a GameState-en keresztül növeli a pontszámot. JSON válasszal tér vissza. 

* display_score: Amint lejárt az idő vagy elfogytak a kérdések ide irányítódik át a játék. A renderer template segítsével megjeleníti a pontszámot, és lehetőséget ad a kvíz újrakezdésére.

* get_question: A QuestionBank-ból lekér egy véletlenszerű kérdést a jelenegi témakörből. A lekért kérdést pedig JSON válaszként vissza adja.  

* _timer: A Gamestat-en keresztül a hátralévő időt csökkenti. Az új hátralévő időt pedig JSON válaszként visszadja. Ez az utvonala egy jQuery kérés segítségével másodpercenként van meghívva.

* game_menu: A renderer template segítségével megjeleníti magát a játékot (kérdés, válaszok, hátralévő idő, pontszám). 

* main_menu: A / default elérési utvonal. Bármikor amikor el van érve, a jelenegi játékot megszakítja, visszaállítja a pontszámot, hátralévő időt, törli a kérdezett kérdéseket, a kiválasztott témát. A renderer template segítségével lehetőséget ad téma válaszra és a játék elkezdésére.

### GameState
A játéklogikáját vezérli, tárolja a kiválasztott témakört, a feltett kérdéseket. Vezérli a ScoreManager-t, TimeManager-t.

**Függvények / Eljárások**

*  get_topic: Visszadja a jelenlegi témakört.

*  get_questions_asked: Visszadja az eddig feltett kérdéseket. 

*  get_score: A ScoreManager-en keresztül visszadja a játékos pontszámát.

*  increment_score: A ScoreManager-en keresztül megnöveli a pontszámot. Helyes válasz esetén ezt hívja a Flask Webserver check_answer elérési utvonala.

*  get_timer: A TimerManager-en keresztül visszadja a hátralévő időt. 

*  add_question: Hozzáadja a feltett kérdést a halmazhoz, hogy elkerülje az ismételt kérdésfeltevést.

*  reset_game: Lenulláza a pontszámot, a visszaszámáló órát visszaállítja és kiüriti a feltett kérdések halmazát. Így megkezdőthet az újabb játékmenet. A default elérési utvonal (Azaz /) valamint a /score elérési utvonalból hívódhat meg. 

A játékmenetet, játéklogikát vezérli. A konstruktorban egy témát megkap, ami alapján a megfelelő témájú kérdéseket kéri le a kérdésbankból. Tárolja a már feltett kérdéseket, a játékos pontszámát, hátralévőidőt és a játék újrakezdését is ő végzi.

A ScoreManager, TimerManager modult használja, valamint a beépített Set típust.



### ScoreManager
A játékos jelenegi pontszámát tárolja. A pontszám növelését és visszaállítását is végzi.

**Függvények / Eljárások**

* increment_score: A jelenlegi pontszámhoz hozzáad egyet.

* get_score: Visszadja a jelenlegi pontszámot.

* reset_score: Lenulláza a jelenlegi pontszámot.

A metódusait fel vannak használva helyes válasz ellenőrzésnél, és a játék végén a pontszám kijelzésére.



### QuestionBank
Ő felelős a JSON formátumban tárolt kérdések feldolgozásáért, betöltéséért. Számontartja a már feltett kérdéseket, hogy többször ne fordulhasson elő ugyanaz.

Egy témanevet megadva, csak ahhoz a témakörhöz tartozó kérdéseket jeleníti meg.

**Függvények / Eljárások**

* get_random_question: Egy megadott témakörből választ véletlenszerűen, még nem feltett kérdést.

* reset_used_questions: segítségével a már feltett kérdéseket “kinullázza” így az új játékban újra előfordulhat bármelyik kérdés az adott témakörből. A játék végén vagy a default elérési utvonalból (Azaz /) van meghívva.


### TimerManger
A játék közben megjelenített vissazstámáló óráért felelős. A constrouctor-ban be kell állítani, hogy mennyi időről számoljon vissza.

Rendelkezik egy saját @app.route-al is, amit elérve lefut a decrement metódus. Erre az utvonalra jQuery segítségével másodpercenként intézünk kérés, ha a kvíz játék fut.

**Függvények / Eljárások**

* decrement: Minden egyes hívás esetén levon egy másodpercet a hátralévő időből és visszadja, a hátralévő időt.

* reset: Visszaállítja a hátralévő időt. A játék végén, vagy a default elérési utvonalból (Azaz /) hívődik meg.
