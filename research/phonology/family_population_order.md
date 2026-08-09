# Family analysis order by speaker exposure

> **Status:** research ordering only. This ranking does not define or alter genealogical weighting.

## Method

- Genealogical units are the represented top-level Glottolog 5.3 families/isolates in `family_inventory.json`.
- Speaker estimates come from the frozen baseline `SPEAKER_ESTIMATES`, which is CLDR-derived.
- For each unit, one estimate is counted per distinct sampled Glottolog language; duplicate source records do not multiply the estimate.
- CLDR-style fluent-speaker estimates can include L1 and L2 populations and overlap across languages, so the sum is a **speaker-exposure proxy**, not a unique human headcount.
- Population affects **analysis order only**. It must not determine the eventual genealogical `F` weight.
- Units with no available frozen estimate remain explicitly unranked rather than receiving guessed values.

## Coverage

- Represented genealogical units: **245**.
- Ranked units with at least one speaker estimate: **46**.
- Units with no speaker estimate and therefore currently unranked: **199**.
- Distinct sampled languages contributing an estimate: **381**.

## Ranked portion

| Rank | Unit | Type | Speaker-exposure proxy | Estimated sample languages | Sample languages | Coverage |
|---:|---|---|---:|---:|---:|---:|
| 1 | Indo-European (`indo1319`) | family | 4,958,269,053 | 98 | 140 | 70.0% |
| 2 | Sino-Tibetan (`sino1245`) | family | 1,531,886,716 | 23 | 97 | 23.7% |
| 3 | Afro-Asiatic (`afro1255`) | family | 526,958,069 | 19 | 104 | 18.3% |
| 4 | Austronesian (`aust1307`) | family | 487,578,528 | 34 | 109 | 31.2% |
| 5 | Atlantic-Congo (`atla1278`) | family | 366,087,356 | 85 | 406 | 20.9% |
| 6 | Dravidian (`drav1251`) | family | 267,507,015 | 9 | 32 | 28.1% |
| 7 | Turkic (`turk1311`) | family | 157,553,241 | 14 | 21 | 66.7% |
| 8 | Japonic (`japo1237`) | family | 121,249,490 | 1 | 3 | 33.3% |
| 9 | Austroasiatic (`aust1305`) | family | 104,273,769 | 9 | 40 | 22.5% |
| 10 | Tai-Kadai (`taik1256`) | family | 84,083,291 | 8 | 19 | 42.1% |
| 11 | Koreanic (`kore1284`) | family | 76,358,752 | 1 | 1 | 100.0% |
| 12 | Uralic (`ural1272`) | family | 21,528,947 | 16 | 31 | 51.6% |
| 13 | Mande (`mand1469`) | family | 18,514,733 | 8 | 43 | 18.6% |
| 14 | Quechuan (`quec1387`) | family | 11,437,628 | 2 | 22 | 9.1% |
| 15 | Nilotic (`nilo1247`) | family | 9,016,734 | 6 | 27 | 22.2% |
| 16 | Tupian (`tupi1275`) | family | 5,622,426 | 3 | 49 | 6.1% |
| 17 | Kartvelian (`kart1248`) | family | 4,475,632 | 3 | 4 | 75.0% |
| 18 | Songhay (`song1307`) | family | 3,717,748 | 3 | 4 | 75.0% |
| 19 | Aymaran (`ayma1253`) | family | 2,498,478 | 1 | 2 | 50.0% |
| 20 | Nakh-Daghestanian (`nakh1245`) | family | 2,146,701 | 5 | 13 | 38.5% |
| 21 | Mayan (`maya1287`) | family | 1,908,545 | 2 | 12 | 16.7% |
| 22 | Ta-Ne-Omotic (`gong1255`) | family | 1,583,154 | 1 | 10 | 10.0% |
| 23 | Abkhaz-Adyge (`abkh1242`) | family | 1,573,826 | 3 | 3 | 100.0% |
| 24 | Basque (`basq1248`) | isolate | 1,016,057 | 1 | 1 | 100.0% |
| 25 | Furan (`fura1235`) | family | 1,006,814 | 1 | 1 | 100.0% |
| 26 | Hmong-Mien (`hmon1336`) | family | 718,418 | 1 | 3 | 33.3% |
| 27 | Otomanguean (`otom1299`) | family | 407,025 | 1 | 17 | 5.9% |
| 28 | Maban (`maba1274`) | family | 369,165 | 1 | 2 | 50.0% |
| 29 | Mongolic-Khitan (`mong1349`) | family | 321,713 | 1 | 8 | 12.5% |
| 30 | Nubian (`nubi1251`) | family | 309,502 | 1 | 1 | 100.0% |
| 31 | Araucanian (`arau1255`) | family | 267,286 | 1 | 1 | 100.0% |
| 32 | Khoe-Kwadi (`khoe1240`) | family | 232,438 | 1 | 2 | 50.0% |
| 33 | Saharan (`saha1256`) | family | 190,176 | 1 | 4 | 25.0% |
| 34 | Athabaskan-Eyak-Tlingit (`atha1245`) | family | 171,003 | 2 | 10 | 20.0% |
| 35 | Arawakan (`araw1281`) | family | 129,351 | 1 | 42 | 2.4% |
| 36 | Nuclear-Macro-Je (`nucl1710`) | family | 58,022 | 2 | 18 | 11.1% |
| 37 | Eskimo-Aleut (`eski1264`) | family | 54,075 | 1 | 5 | 20.0% |
| 38 | Algic (`algi1248`) | family | 33,372 | 3 | 7 | 42.9% |
| 39 | Siouan (`siou1252`) | family | 27,885 | 1 | 3 | 33.3% |
| 40 | Iroquoian (`iroq1247`) | family | 24,583 | 1 | 4 | 25.0% |
| 41 | Muskogean (`musk1252`) | family | 10,536 | 1 | 4 | 25.0% |
| 42 | Pama-Nyungan (`pama1250`) | family | 2,204 | 1 | 204 | 0.5% |
| 43 | Salishan (`sali1255`) | family | 1,279 | 1 | 10 | 10.0% |
| 44 | Seri (`seri1257`) | isolate | 838 | 1 | 1 | 100.0% |
| 45 | Wakashan (`waka1280`) | family | 746 | 1 | 2 | 50.0% |
| 46 | Pano-Tacanan (`pano1259`) | family | 90 | 1 | 25 | 4.0% |

## Unranked represented units

These units are genealogically represented in GlottoDelta but have no usable frozen CLDR-derived speaker estimate in the sampled languages. They remain in scope; their later ordering requires an explicit supplemental demographic source rather than inference.

Aewa (`abis1238`), Aikanã (`aika1237`), Ainu (`ainu1252`), Andoque (`ando1256`), Angan (`anga1289`), Arawan (`araw1282`), Baining (`bain1263`), Barbacoan (`barb1265`), Berta (`bert1248`), Bilua (`bilu1245`), Blue Nile Mao (`maoo1243`), Boran (`bora1262`), Border (`bord1247`), Bororoan (`boro1281`), Bunaban (`buna1274`), Burushaski (`buru1296`), Caddoan (`cadd1255`), Cahuapanan (`cahu1265`), Camsá (`cams1241`), Candoshi-Shapra (`cand1248`), Cariban (`cari1283`), Cayubaba (`cayu1262`), Central Sudanic (`cent2225`), Chapacuran (`chap1271`), Chibchan (`chib1249`), Chicham (`jiva1245`), Chimakuan (`chim1311`), Chimariko (`chim1301`), Chiquitano (`chiq1253`), Chocoan (`choc1280`), Chonan (`chon1288`), Chukotko-Kamchatkan (`chuk1271`), Chumashan (`chum1262`), Cochimi-Yuman (`coch1271`), Cofán (`cofa1242`), Dajuic (`daju1249`), Dizoid (`dizo1235`), Dogon (`dogo1299`), East Strickland (`east2433`), Eastern Daly (`east2374`), Eastern Jebel (`east2386`), Eleman (`nucl1580`), Fasu (`fasu1242`), Fulniô (`fuln1247`), Gaagudju (`gaga1251`), Garrwan (`garr1260`), Giimbiyu (`giim1238`), Great Andamanese (`grea1241`), Guahiboan (`guah1252`), Guaicuruan (`guai1249`), Guató (`guat1253`), Gumuz (`gumu1250`), Gunwinyguan (`gunw1250`), Hadza (`hadz1240`), Haida (`haid1248`), Harakmbut (`hara1260`), Heibanic (`heib1242`), Hibito-Cholon (`hibi1242`), Hoti (`yuwa1244`), Huavean (`huav1256`), Huitotoan (`huit1251`), Ijoid (`ijoi1239`), Irántxe-Münkü (`iran1263`), Itonama (`iton1250`), Iwaidjan Proper (`iwai1246`), Jarawa-Onge (`jara1244`), Jarrakan (`jarr1235`), Jicaquean (`jica1245`), Kadugli-Krongo (`kadu1256`), Kakua-Nukak (`kaku1242`), Kanoê (`kano1245`), Karuk (`karo1304`), Kawesqar (`kawe1237`), Keresan (`kere1287`), Kiowa-Tanoan (`kiow1265`), Kiwaian (`kiwa1251`), Klamath-Modoc (`klam1254`), Koiarian (`koia1260`), Kolopom (`kolo1268`), Koman (`koma1264`), Konda-Yahadian (`kond1302`), Kresh-Aja (`kres1240`), Kru (`krua1234`), Kuliak (`kuli1252`), Kunama (`kuna1268`), Kungarakany (`kung1259`), Kunimaipan (`kuni1270`), Kunza (`kunz1244`), Kuot (`kuot1243`), Kusunda (`kusu1250`), Kwaza (`kwaz1243`), Kxa (`kxaa1236`), Laragia (`lara1258`), Lavukaleve (`lavu1241`), Leco (`leco1242`), Limilngan-Wulna (`limi1242`), Lule (`lule1238`), Maiduan (`maid1262`), Mangarrayi-Maran (`mang1423`), Maningrida (`mani1293`), Marrku-Wurrugu (`marr1257`), Mataguayan (`mata1289`), Mato Grosso Arára (`mato1253`), Maybratic (`mayb1237`), Minkin (`mink1237`), Mirndi (`mirn1241`), Misumalpan (`misu1242`), Miwok-Costanoan (`miwo1274`), Mixe-Zoque (`mixe1284`), Mochica (`moch1259`), Molale (`mola1238`), Mor {Bomberai Peninsula} (`morb1239`), Mosetén-Chimané (`mose1249`), Movima (`movi1243`), Muniche (`muni1258`), Naduhup (`nada1235`), Nambiquaran (`namb1299`), Nara (`nara1262`), Narrow Talodi (`narr1279`), Ndu (`nduu1242`), Nimboranic (`nimb1257`), Nivkh (`nivk1234`), North Bougainville (`nort2933`), North Halmahera (`nort2923`), Northern Daly (`nort1547`), Nuclear Torricelli (`nucl1708`), Nuclear Trans New Guinea (`nucl1709`), Nyimang (`nyim1244`), Nyulnyulan (`nyul1248`), Palaihnihan (`pala1350`), Peba-Yagua (`peba1241`), Pirahã (`pira1253`), Pomoan (`pomo1273`), Puelche (`puel1244`), Puinave (`puin1248`), Pumé (`pume1238`), Puri-Coroado (`puri1261`), Páez (`paez1247`), Sahaptian (`saha1239`), Saliban (`sali1297`), Sandawe (`sand1273`), Savosavo (`savo1255`), Senagi (`sena1264`), Sentanic (`sent1261`), Sepik (`sepi1257`), Shabo (`shab1252`), Shastan (`shas1238`), Siamou (`siam1242`), Sko (`skoo1245`), South Bird's Head (`sout3418`), South Bougainville (`sout2948`), South Omotic (`sout2845`), Southern Daly (`sout2772`), Surmic (`surm1244`), Tamaic (`tama1329`), Tangkic (`tang1340`), Tarascan (`tara1323`), Taushiro (`taus1253`), Teberan (`tebe1251`), Temeinic (`teme1251`), Ticuna-Yuri (`ticu1244`), Timor-Alor-Pantar (`timo1261`), Tinigua (`tini1245`), Tiwi (`tiwi1244`), Tonkawa (`tonk1249`), Totonacan (`toto1251`), Trumai (`trum1247`), Tsimshian (`tsim1258`), Tucanoan (`tuca1253`), Tungusic (`tung1282`), Tunica (`tuni1252`), Tuu (`tuuu1241`), Umbugarla (`umbu1235`), Urarina (`urar1246`), Uru-Chipaya (`uruc1242`), Uto-Aztecan (`utoa1244`), Vilela (`vile1241`), Wadjiginy (`wadj1254`), Wageman (`wage1238`), Waorani (`waor1240`), Warao (`wara1303`), Washo (`wash1253`), Western Daly (`west2434`), Wintuan (`wint1258`), Worrorran (`worr1236`), Yana (`yana1271`), Yangmanic (`yang1287`), Yanomamic (`yano1268`), Yareban (`yare1250`), Yawa-Saweru (`yawa1259`), Yeniseian (`yeni1252`), Yuchi (`yuch1247`), Yukaghir (`yuka1259`), Yuki-Wappo (`yuki1242`), Yuracaré (`yura1255`), Yámana (`yama1264`), Zamucoan (`zamu1243`), Zaparoan (`zapa1251`), Zuni (`zuni1245`).
