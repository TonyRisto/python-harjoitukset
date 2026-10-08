# Kylänkehityspeli

#### Tony Risto

## Pelin idea

Pelin ideana on kasvattaa ja kehittää kylää kestävän kehityksen periaatteiden mukaisesti.
Pelissä on useita eri resursseja ja mittareita, joita pelaajan kannattaa seurata ahkerasti ja
niiden avulla miettiä seuraavia valintojansa. Peli vaatii pelaajalta hieman mietiskelyä ja eri
numeroiden seuraamista, jotta peli päättyisi pelaajan kannalta hyvin.

## Pelin tavoite

Pelin tavoitteena on rakentaa kylä kestävän kehityksen tavoitteiden mukaisesti.

## Voitto ja häviö

### Voittomahdollisuudet
- Kestävä kylä voitto (vaatii 250 asukasta ja kaikki kestävyysmittarit vähintään 70 %)
- Ekologinen voitto (vaatii uusiutuvan energian ja ympäristön mittarit vähintään 75 %)
- Taloudellinen voitto (rahan määrä 1 100 000 €)

### Häviömahdollisuudet
- Kylän konkurssi (raha menee 0€)
- Kylän autioituminen (asukkaat menee 0)
- Kylän ympäristön tuhoutuminen ja asukkaiden onnettomuus (ympäristö ja onnellisuus menee 0)
- Ajan loppuminen kesken ja useita eri häviömahdollisuuksia, riippuen kestävyysmittareiden tilanteesta

## Toiminnallisuudet ja toiminta

### Toiminnallisuudet
- pelaajan nimi ja ikärajatarkastus
- uusi peli, ohjeet, jatka tallennettua peliä, lopeta
- pelin komennot ovat rakennukset, tilanne, kulutus,
  seuraava (pelissä vuosi eteenpäin), tallenna, paavalikko
- rakennusten katsominen ja niiden rakentaminen
- tilanteen ja kulutuksen/tuoton tarkastelu
- pelissä yhden vuoden eteenpäin siirtäminen
- tallentaminen ja lataaminen
- kolme voittoreittiä ja useita eri häviöitä

### Toimintaperiaatteet
- Asukkaat tuovat tuloja, rakennuksista maksetaan ylläpitoa
- ruoka ja energia kuluvat asukasluvun mukaan (vakiot asetettu näitä varten)
- väkiluku kasvaa, kun on asuntoja ja ruokaa tarpeeksi sekä onnellisuus on tarpeeksi korkealla
- energiapula laskee onnellisuutta ja tasa-arvoa
- kestävyysmittarit laskevat joka vuosi vakioiden perusteella, rakennukset nostavat niitä
- kestävyysmittarit pysyvät 0-100 välillä (edustavat prosenttimääriä)
- advanceYear laskee kaiken yhdellä kertaa

## Kestävän kehityksen näkökulma

Peli perustuu ajatukseen, että kestävä kehitys on tasapainoa ympäristön, ihmisten ja talouden välillä. Halpa ratkaisu rasittaa ympäristöä, ja kestävät ratkaisut maksavat enemmän. Mittarit myös rappeutuvat joka vuosi, joten kestävyys vaatii jatkuvaa työtä.

Peli toteuttaa erityisesti YK:n tavoitteita:

- **6 Puhdas vesi:** vesitornit pitävät veden laadun yllä.
- **7 Puhdas energia:** pelaaja valitsee halvan hakevoimalaitoksen ja kalliimpien uusiutuvien välillä.
- **4 Hyvä koulutus:** koulut nostavat koulutusta, mutta maksavat ylläpitoa.
- **3 Terveys ja hyvinvointi:** puisto ja terveysasema nostavat onnellisuutta.
- **10 Eriarvoisuuden vähentäminen:** seurakuntatalo ja terveysasema nostavat tasa-arvoa.

Taloudellinen voitto on mahdollinen, mutta se ei tarkoita kestävän kehityksen mukaista voittoa.