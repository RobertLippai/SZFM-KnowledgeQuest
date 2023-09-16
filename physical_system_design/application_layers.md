# Alkalmazás rétegei

### Megjelenítési réteg
Ez a réteg felelős a felhasználói felület megjelenítéséért. Ennek segítségével jelenítjük meg a kvíz témákat, kérdéseket. A kvíz kérdések esetén a hozzájuk tartozó válaszok, a pontszám és a hátralévő idő is látható. Emelett gombok segítstgével lehetőséget ad a felhasználónak, hogy választ adjon a kérdésre vagy éppen témát válasszon, amit majd a logikai réteg teljesít.

A felületek létrehozásához HTML-t használunk, ami majd Flask template-ként fog működni. A felület formázását CSS segítségével oldjuk meg.

A dinamikus elemek megjelenítését, mint például a kérdések, a pontszám és a hátralévő idő, JavaScript segítségével valósítjuk meg.


### Logikai réteg
Az alkalmazás logikáját Python segítségével valósítjuk meg. Ide tartozik a kérdések lekérdezése, a helyes válaszok ellenőrzése és a pontszám számítása is. Ezen felül a kvíz játékmenetét is ebben a rétegben kezeljük.

### Adat elérési réteg
Ez a réteg felelős a kérdések eléréséért a kérdésbankból. A kvízkérdések .json fájljait Python segítségével dolgozzuk fel és témánként csoportosítjuk őket. A könnyebb átláthatóság érdekében a kérdések témánként külön .json fájlban lesznek tárolva.