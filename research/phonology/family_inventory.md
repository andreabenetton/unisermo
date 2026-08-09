# GlottoDelta family inventory

> **Scope:** inventory only. No phoneme-by-family scores or language-design decisions are calculated here.

## Source and methodological rule

The inventory is pinned to **Glottolog 5.3**, tag `v5.3`, commit `eb7d58221bea745a21cb7b96582118e990a295c2` (release 2026-03-02). It was re-verified as the current Glottolog release on 2026-08-09.

Primary assignment uses the official `tree_glottolog_newick.txt`: each GlottoDelta source Glottocode is assigned to the root of its Glottolog top-level tree. The companion `languages.csv` is secondary only: it supplies macroarea metadata, dialect-to-language normalization, and a diagnostic list of top-level administrative categories. Macroarea never affects weighting or genealogy.

The Newick forest contains 239 ordinary plurilingual family roots plus 183 isolate roots. The CLDF table contains 246 top-level `family` rows plus the same 183 isolates. The seven extra CLDF top-level family rows are all non-genealogical/administrative categories and are therefore excluded from the independent-family universe rather than counted as spoken-language families.

## Completeness

| Measure | Count / coverage |
|---|---|
| Frozen GlottoDelta source records | 2122 |
| With Glottocode | 2121 |
| Mapped to ordinary family/isolate | 2114 |
| Ordinary mapping among coded records | 99.67% |
| Pseudo/administrative-category records | 7 |
| Coded records classified, including pseudo categories | 100.00% |
| Ordinary genealogy completeness after pseudo exclusion | 100.00% |
| Without Glottocode | 1 |
| Unresolved obsolete/problematic Glottocodes | 0 |
| Distinct Glottolog languages in genealogical units | 2070 |
| Family-level source Glottocodes not forced into a language | 4 |

The 2,122 source-record denominator is intentionally preserved. Distinct-language counts differ because 109 source Glottocodes are dialect-level in Glottolog 5.3 and are normalized to their language-level parent; four source records point to family-level Glottocodes and are not guessed into a particular child language.

## Genealogical universe represented

| Unit type | Represented | Glottolog 5.3 universe | Absent |
|---|---|---|---|
| Ordinary plurilingual families | 174 | 239 | 65 |
| Isolates | 71 | 183 | 112 |
| Total independent genealogical units | 245 | 422 | 177 |

## Pseudo-genealogical / administrative categories

These are tracked explicitly but excluded from the ordinary genealogical-unit universe:

| Glottocode | Category | Sample records | Macroarea metadata |
|---|---|---|---|
| arti1236 | Artificial Language | 0 | Africa, Australia, Eurasia, North America, Papunesia |
| book1242 | Bookkeeping | 4 | Africa, Australia, Eurasia, North America, Papunesia, South America |
| mixe1287 | Mixed Language | 0 | Australia, Eurasia, South America |
| pidg1258 | Pidgin | 1 | Africa, Australia, Eurasia, North America, Papunesia, South America |
| spee1234 | Speech Register | 1 | Africa, Eurasia, Papunesia, South America |
| unat1236 | Unattested | 0 | Africa, Australia, Eurasia, North America, Papunesia, South America |
| uncl1493 | Unclassifiable | 1 | Africa, Australia, Eurasia, North America, Papunesia, South America |

### Source records in excluded categories

| Source name | ISO | Glottocode | Top-level category |
|---|---|---|---|
| Bandjigali | drl | band1337 | Bookkeeping |
| Bubia | bbx | bubi1249 | Bookkeeping |
| Callawaya | caw | call1235 | Speech Register |
| Karirí-Xocó | kzw | kari1255 | Unclassifiable |
| Katukína | kav | nucl1668 | Bookkeeping |
| Liberian English | lir | libe1240 | Pidgin |
| Samre | sxm | samr1245 | Bookkeeping |

## Records requiring explicit handling

### No Glottocode

| Source name | ISO | Treatment |
|---|---|---|
| Djindewal | mis | No genealogy guessed |

No coded source record remains unresolved after separating the seven pseudo/administrative categories.

### Source Glottocodes at Glottolog family level

These records can be assigned to a top-level family but are not counted as distinct Glottolog languages, because the source Glottocode itself is classified at family level in 5.3:

| Source name | ISO | Glottocode | Glottolog 5.3 node |
|---|---|---|---|
| Mangghuer | mjg | tuuu1240 | Monguoric |
| Mongolian | mon | mong1331 | Mongolian |
| Dinka | din | dink1262 | Dinka |
| Caodeng rGyalrong | jya | jiar1240 | Northern Gyalrong |

## Represented families and isolates

| Top-level Glottocode | Family / isolate | Type | Source records | Distinct languages | Macroarea metadata |
|---|---|---|---|---|---|
| atla1278 | Atlantic-Congo | family | 408 | 406 | Africa, North America |
| pama1250 | Pama-Nyungan | family | 230 | 204 | Australia, Papunesia |
| indo1319 | Indo-European | family | 144 | 140 | Africa, Australia, Eurasia, North America, Papunesia, South America |
| aust1307 | Austronesian | family | 109 | 109 | Africa, Eurasia, Papunesia, South America |
| afro1255 | Afro-Asiatic | family | 104 | 104 | Africa, Eurasia |
| sino1245 | Sino-Tibetan | family | 98 | 97 | Eurasia |
| tupi1275 | Tupian | family | 50 | 49 | South America |
| araw1281 | Arawakan | family | 43 | 42 | North America, South America |
| mand1469 | Mande | family | 43 | 43 | Africa |
| aust1305 | Austroasiatic | family | 40 | 40 | Eurasia |
| drav1251 | Dravidian | family | 32 | 32 | Eurasia |
| ural1272 | Uralic | family | 31 | 31 | Eurasia |
| nilo1247 | Nilotic | family | 28 | 27 | Africa |
| nucl1709 | Nuclear Trans New Guinea | family | 28 | 28 | Papunesia |
| pano1259 | Pano-Tacanan | family | 25 | 25 | South America |
| cari1283 | Cariban | family | 24 | 24 | South America |
| quec1387 | Quechuan | family | 23 | 22 | South America |
| cent2225 | Central Sudanic | family | 22 | 22 | Africa |
| turk1311 | Turkic | family | 21 | 21 | Eurasia |
| nucl1710 | Nuclear-Macro-Je | family | 20 | 18 | South America |
| taik1256 | Tai-Kadai | family | 20 | 19 | Eurasia |
| tuca1253 | Tucanoan | family | 19 | 19 | South America |
| otom1299 | Otomanguean | family | 17 | 17 | North America |
| utoa1244 | Uto-Aztecan | family | 15 | 15 | North America |
| nakh1245 | Nakh-Daghestanian | family | 13 | 13 | Eurasia |
| maya1287 | Mayan | family | 12 | 12 | North America |
| chib1249 | Chibchan | family | 11 | 11 | North America, South America |
| krua1234 | Kru | family | 11 | 11 | Africa |
| mong1349 | Mongolic-Khitan | family | 11 | 8 | Eurasia |
| atha1245 | Athabaskan-Eyak-Tlingit | family | 10 | 10 | North America |
| nyul1248 | Nyulnyulan | family | 10 | 10 | Australia |
| sali1255 | Salishan | family | 10 | 10 | North America |
| gong1255 | Ta-Ne-Omotic | family | 10 | 10 | Africa |
| gunw1250 | Gunwinyguan | family | 9 | 9 | Australia |
| worr1236 | Worrorran | family | 8 | 7 | Australia |
| algi1248 | Algic | family | 7 | 7 | North America |
| sepi1257 | Sepik | family | 7 | 7 | Papunesia |
| choc1280 | Chocoan | family | 6 | 6 | South America |
| heib1242 | Heibanic | family | 6 | 6 | Africa |
| ijoi1239 | Ijoid | family | 6 | 6 | Africa |
| kadu1256 | Kadugli-Krongo | family | 6 | 6 | Africa |
| mixe1284 | Mixe-Zoque | family | 6 | 6 | North America |
| nucl1708 | Nuclear Torricelli | family | 6 | 6 | Papunesia |
| surm1244 | Surmic | family | 6 | 6 | Africa |
| west2434 | Western Daly | family | 6 | 6 | Australia |
| araw1282 | Arawan | family | 5 | 5 | South America |
| eski1264 | Eskimo-Aleut | family | 5 | 5 | Eurasia, North America |
| guai1249 | Guaicuruan | family | 5 | 5 | South America |
| mirn1241 | Mirndi | family | 5 | 5 | Australia |
| narr1279 | Narrow Talodi | family | 5 | 5 | Africa |
| tung1282 | Tungusic | family | 5 | 5 | Eurasia |
| yano1268 | Yanomamic | family | 5 | 5 | South America |
| barb1265 | Barbacoan | family | 4 | 4 | South America |
| jiva1245 | Chicham | family | 4 | 4 | South America |
| chuk1271 | Chukotko-Kamchatkan | family | 4 | 4 | Eurasia |
| guah1252 | Guahiboan | family | 4 | 4 | South America |
| huit1251 | Huitotoan | family | 4 | 4 | South America |
| iroq1247 | Iroquoian | family | 4 | 4 | North America |
| iwai1246 | Iwaidjan Proper | family | 4 | 4 | Australia |
| kart1248 | Kartvelian | family | 4 | 4 | Eurasia |
| kiow1265 | Kiowa-Tanoan | family | 4 | 4 | North America |
| koma1264 | Koman | family | 4 | 4 | Africa |
| mang1423 | Mangarrayi-Maran | family | 4 | 4 | Australia |
| mani1293 | Maningrida | family | 4 | 4 | Australia |
| mata1289 | Mataguayan | family | 4 | 4 | South America |
| musk1252 | Muskogean | family | 4 | 4 | North America |
| nada1235 | Naduhup | family | 4 | 4 | South America |
| namb1299 | Nambiquaran | family | 4 | 4 | South America |
| saha1256 | Saharan | family | 4 | 4 | Africa |
| song1307 | Songhay | family | 4 | 4 | Africa |
| zapa1251 | Zaparoan | family | 4 | 4 | South America |
| abkh1242 | Abkhaz-Adyge | family | 3 | 3 | Eurasia |
| bord1247 | Border | family | 3 | 3 | Papunesia |
| giim1238 | Giimbiyu | family | 3 | 3 | Australia |
| hmon1336 | Hmong-Mien | family | 3 | 3 | Eurasia |
| japo1237 | Japonic | family | 3 | 3 | Eurasia, Papunesia |
| kuli1252 | Kuliak | family | 3 | 3 | Africa |
| nduu1242 | Ndu | family | 3 | 3 | Papunesia |
| siou1252 | Siouan | family | 3 | 3 | North America |
| skoo1245 | Sko | family | 3 | 3 | Papunesia |
| sout2845 | South Omotic | family | 3 | 3 | Africa |
| tang1340 | Tangkic | family | 3 | 3 | Australia |
| toto1251 | Totonacan | family | 3 | 3 | North America |
| ayma1253 | Aymaran | family | 2 | 2 | South America |
| bora1262 | Boran | family | 2 | 2 | South America |
| boro1281 | Bororoan | family | 2 | 2 | South America |
| buna1274 | Bunaban | family | 2 | 2 | Australia |
| cadd1255 | Caddoan | family | 2 | 2 | North America |
| cahu1265 | Cahuapanan | family | 2 | 2 | South America |
| chap1271 | Chapacuran | family | 2 | 2 | South America |
| chon1288 | Chonan | family | 2 | 2 | South America |
| coch1271 | Cochimi-Yuman | family | 2 | 2 | North America |
| dogo1299 | Dogon | family | 2 | 2 | Africa |
| garr1260 | Garrwan | family | 2 | 2 | Australia |
| jarr1235 | Jarrakan | family | 2 | 2 | Australia |
| kaku1242 | Kakua-Nukak | family | 2 | 2 | South America |
| khoe1240 | Khoe-Kwadi | family | 2 | 2 | Africa |
| kres1240 | Kresh-Aja | family | 2 | 2 | Africa |
| kxaa1236 | Kxa | family | 2 | 2 | Africa |
| maba1274 | Maban | family | 2 | 2 | Africa |
| marr1257 | Marrku-Wurrugu | family | 2 | 2 | Australia |
| miwo1274 | Miwok-Costanoan | family | 2 | 2 | North America |
| nort2923 | North Halmahera | family | 2 | 2 | Papunesia |
| nyim1244 | Nyimang | family | 2 | 2 | Africa |
| peba1241 | Peba-Yagua | family | 2 | 2 | South America |
| pomo1273 | Pomoan | family | 2 | 2 | North America |
| sali1297 | Saliban | family | 2 | 2 | South America |
| sout2772 | Southern Daly | family | 2 | 2 | Australia |
| teme1251 | Temeinic | family | 2 | 2 | Africa |
| timo1261 | Timor-Alor-Pantar | family | 2 | 2 | Papunesia |
| tsim1258 | Tsimshian | family | 2 | 2 | North America |
| uruc1242 | Uru-Chipaya | family | 2 | 2 | South America |
| waka1280 | Wakashan | family | 2 | 2 | North America |
| yang1287 | Yangmanic | family | 2 | 2 | Australia |
| yuka1259 | Yukaghir | family | 2 | 2 | Eurasia |
| yuki1242 | Yuki-Wappo | family | 2 | 2 | North America |
| zamu1243 | Zamucoan | family | 2 | 2 | South America |
| abis1238 | Aewa | isolate | 1 | 1 | South America |
| aika1237 | Aikanã | isolate | 1 | 1 | South America |
| ainu1252 | Ainu | family | 1 | 1 | Eurasia |
| ando1256 | Andoque | isolate | 1 | 1 | South America |
| anga1289 | Angan | family | 1 | 1 | Papunesia |
| arau1255 | Araucanian | family | 1 | 1 | South America |
| bain1263 | Baining | family | 1 | 1 | Papunesia |
| basq1248 | Basque | isolate | 1 | 1 | Eurasia |
| bert1248 | Berta | isolate | 1 | 1 | Africa |
| bilu1245 | Bilua | isolate | 1 | 1 | Papunesia |
| maoo1243 | Blue Nile Mao | family | 1 | 1 | Africa |
| buru1296 | Burushaski | isolate | 1 | 1 | Eurasia |
| cams1241 | Camsá | isolate | 1 | 1 | South America |
| cand1248 | Candoshi-Shapra | isolate | 1 | 1 | South America |
| cayu1262 | Cayubaba | isolate | 1 | 1 | South America |
| chim1311 | Chimakuan | family | 1 | 1 | North America |
| chim1301 | Chimariko | isolate | 1 | 1 | North America |
| chiq1253 | Chiquitano | family | 1 | 1 | South America |
| chum1262 | Chumashan | family | 1 | 1 | North America |
| cofa1242 | Cofán | isolate | 1 | 1 | South America |
| daju1249 | Dajuic | family | 1 | 1 | Africa |
| dizo1235 | Dizoid | family | 1 | 1 | Africa |
| east2433 | East Strickland | family | 1 | 1 | Papunesia |
| east2374 | Eastern Daly | family | 1 | 1 | Australia |
| east2386 | Eastern Jebel | family | 1 | 1 | Africa |
| nucl1580 | Eleman | family | 1 | 1 | Papunesia |
| fasu1242 | Fasu | isolate | 1 | 1 | Papunesia |
| fuln1247 | Fulniô | isolate | 1 | 1 | South America |
| fura1235 | Furan | family | 1 | 1 | Africa |
| gaga1251 | Gaagudju | isolate | 1 | 1 | Australia |
| grea1241 | Great Andamanese | family | 1 | 1 | Eurasia |
| guat1253 | Guató | isolate | 1 | 1 | South America |
| gumu1250 | Gumuz | family | 1 | 1 | Africa |
| hadz1240 | Hadza | isolate | 1 | 1 | Africa |
| haid1248 | Haida | family | 1 | 1 | North America |
| hara1260 | Harakmbut | family | 1 | 1 | South America |
| hibi1242 | Hibito-Cholon | family | 1 | 1 | South America |
| yuwa1244 | Hoti | isolate | 1 | 1 | South America |
| huav1256 | Huavean | family | 1 | 1 | North America |
| iran1263 | Irántxe-Münkü | isolate | 1 | 1 | South America |
| iton1250 | Itonama | isolate | 1 | 1 | South America |
| jara1244 | Jarawa-Onge | family | 1 | 1 | Eurasia |
| jica1245 | Jicaquean | family | 1 | 1 | North America |
| kano1245 | Kanoê | isolate | 1 | 1 | South America |
| karo1304 | Karuk | isolate | 1 | 1 | North America |
| kawe1237 | Kawesqar | family | 1 | 1 | South America |
| kere1287 | Keresan | family | 1 | 1 | North America |
| kiwa1251 | Kiwaian | family | 1 | 1 | Papunesia |
| klam1254 | Klamath-Modoc | isolate | 1 | 1 | North America |
| koia1260 | Koiarian | family | 1 | 1 | Papunesia |
| kolo1268 | Kolopom | family | 1 | 1 | Papunesia |
| kond1302 | Konda-Yahadian | family | 1 | 1 | Papunesia |
| kore1284 | Koreanic | family | 1 | 1 | Eurasia |
| kuna1268 | Kunama | isolate | 1 | 1 | Africa |
| kung1259 | Kungarakany | isolate | 1 | 1 | Australia |
| kuni1270 | Kunimaipan | family | 1 | 1 | Papunesia |
| kunz1244 | Kunza | isolate | 1 | 1 | South America |
| kuot1243 | Kuot | isolate | 1 | 1 | Papunesia |
| kusu1250 | Kusunda | isolate | 1 | 1 | Eurasia |
| kwaz1243 | Kwaza | isolate | 1 | 1 | South America |
| lara1258 | Laragia | isolate | 1 | 1 | Australia |
| lavu1241 | Lavukaleve | isolate | 1 | 1 | Papunesia |
| leco1242 | Leco | isolate | 1 | 1 | South America |
| limi1242 | Limilngan-Wulna | family | 1 | 1 | Australia |
| lule1238 | Lule | isolate | 1 | 1 | South America |
| maid1262 | Maiduan | family | 1 | 1 | North America |
| mato1253 | Mato Grosso Arára | isolate | 1 | 1 | South America |
| mayb1237 | Maybratic | family | 1 | 1 | Papunesia |
| mink1237 | Minkin | isolate | 1 | 1 | Australia |
| misu1242 | Misumalpan | family | 1 | 1 | North America |
| moch1259 | Mochica | isolate | 1 | 1 | South America |
| mola1238 | Molale | isolate | 1 | 1 | North America |
| morb1239 | Mor {Bomberai Peninsula} | isolate | 1 | 1 | Papunesia |
| mose1249 | Mosetén-Chimané | isolate | 1 | 1 | South America |
| movi1243 | Movima | isolate | 1 | 1 | South America |
| muni1258 | Muniche | isolate | 1 | 1 | South America |
| nara1262 | Nara | isolate | 1 | 1 | Africa |
| nimb1257 | Nimboranic | family | 1 | 1 | Papunesia |
| nivk1234 | Nivkh | family | 1 | 1 | Eurasia |
| nort2933 | North Bougainville | family | 1 | 1 | Papunesia |
| nort1547 | Northern Daly | family | 1 | 1 | Australia |
| nubi1251 | Nubian | family | 1 | 1 | Africa |
| pala1350 | Palaihnihan | family | 1 | 1 | North America |
| pira1253 | Pirahã | isolate | 1 | 1 | South America |
| puel1244 | Puelche | isolate | 1 | 1 | South America |
| puin1248 | Puinave | isolate | 1 | 1 | South America |
| pume1238 | Pumé | isolate | 1 | 1 | South America |
| puri1261 | Puri-Coroado | family | 1 | 1 | South America |
| paez1247 | Páez | isolate | 1 | 1 | South America |
| saha1239 | Sahaptian | family | 1 | 1 | North America |
| sand1273 | Sandawe | isolate | 1 | 1 | Africa |
| savo1255 | Savosavo | isolate | 1 | 1 | Papunesia |
| sena1264 | Senagi | family | 1 | 1 | Papunesia |
| sent1261 | Sentanic | family | 1 | 1 | Papunesia |
| seri1257 | Seri | isolate | 1 | 1 | North America |
| shab1252 | Shabo | isolate | 1 | 1 | Africa |
| shas1238 | Shastan | family | 1 | 1 | North America |
| siam1242 | Siamou | isolate | 1 | 1 | Africa |
| sout3418 | South Bird's Head | family | 1 | 1 | Papunesia |
| sout2948 | South Bougainville | family | 1 | 1 | Papunesia |
| tama1329 | Tamaic | family | 1 | 1 | Africa |
| tara1323 | Tarascan | family | 1 | 1 | North America |
| taus1253 | Taushiro | isolate | 1 | 1 | South America |
| tebe1251 | Teberan | family | 1 | 1 | Papunesia |
| ticu1244 | Ticuna-Yuri | family | 1 | 1 | South America |
| tini1245 | Tinigua | isolate | 1 | 1 | South America |
| tiwi1244 | Tiwi | isolate | 1 | 1 | Australia |
| tonk1249 | Tonkawa | isolate | 1 | 1 | North America |
| trum1247 | Trumai | isolate | 1 | 1 | South America |
| tuni1252 | Tunica | isolate | 1 | 1 | North America |
| tuuu1241 | Tuu | family | 1 | 1 | Africa |
| umbu1235 | Umbugarla | isolate | 1 | 1 | Australia |
| urar1246 | Urarina | isolate | 1 | 1 | South America |
| vile1241 | Vilela | isolate | 1 | 1 | South America |
| wadj1254 | Wadjiginy | isolate | 1 | 1 | Australia |
| wage1238 | Wageman | isolate | 1 | 1 | Australia |
| waor1240 | Waorani | isolate | 1 | 1 | South America |
| wara1303 | Warao | isolate | 1 | 1 | South America |
| wash1253 | Washo | isolate | 1 | 1 | North America |
| wint1258 | Wintuan | family | 1 | 1 | North America |
| yana1271 | Yana | isolate | 1 | 1 | North America |
| yare1250 | Yareban | family | 1 | 1 | Papunesia |
| yawa1259 | Yawa-Saweru | family | 1 | 1 | Papunesia |
| yeni1252 | Yeniseian | family | 1 | 1 | Eurasia |
| yuch1247 | Yuchi | isolate | 1 | 1 | North America |
| yura1255 | Yuracaré | isolate | 1 | 1 | South America |
| yama1264 | Yámana | isolate | 1 | 1 | South America |
| zuni1245 | Zuni | isolate | 1 | 1 | North America |

## Absent families and isolates

These ordinary Glottolog 5.3 genealogical units have no source record in the frozen GlottoDelta/PHOIBLE sample:

| Top-level Glottocode | Family / isolate | Type | Macroarea metadata |
|---|---|---|---|
| amto1249 | Amto-Musan | family | Papunesia |
| anim1240 | Anim | family | Papunesia |
| araf1243 | Arafundi | family | Papunesia |
| baib1250 | Baibai-Fas | family | Papunesia |
| bayo1259 | Bayono-Awbono | family | Papunesia |
| monu1249 | Bogia | family | Papunesia |
| bosa1245 | Bosavi | family | Papunesia |
| bula1259 | Bulaka River | family | Papunesia |
| char1238 | Charruan | family | South America |
| chin1490 | Chinookan | family | North America |
| coos1248 | Coosan | family | North America |
| daga1274 | Dagan | family | Papunesia |
| doso1238 | Doso-Turumsa | family | Papunesia |
| east1459 | East Bird's Head | family | Papunesia |
| east2499 | East Kutubu | family | Papunesia |
| east2503 | Eastern Trans-Fly | family | Papunesia |
| geel1240 | Geelvink Bay | family | Papunesia |
| kwer1242 | Greater Kwerba | family | Papunesia |
| hata1242 | Hatam-Mansim | family | Papunesia |
| huar1251 | Huarpean | family | South America |
| hurr1239 | Hurro-Urartian | family | Eurasia |
| kala1402 | Kalapuyan | family | North America |
| kama1371 | Kamakanan | family | South America |
| kamu1264 | Kamula-Elevala | family | Papunesia |
| katl1246 | Katla-Tima | family | Africa |
| katu1274 | Katukinan | family | South America |
| kaur1274 | Kaure-Kosare | family | Papunesia |
| kaya1327 | Kayagaric | family | Papunesia |
| kera1258 | Keram | family | Papunesia |
| kwal1257 | Kwalean | family | Papunesia |
| kwom1263 | Kwomtari-Nai | family | Papunesia |
| lake1255 | Lakes Plain | family | Papunesia |
| left1242 | Left May | family | Papunesia |
| lenc1239 | Lencan | family | North America |
| leng1261 | Lengua-Mascoy | family | South America |
| lepk1239 | Lepki-Murkim-Kembra | family | Papunesia |
| lowe1423 | Lower Sepik | family | Papunesia |
| mail1249 | Mailuan | family | Papunesia |
| mair1253 | Mairasic | family | Papunesia |
| manu1261 | Manubaran | family | Papunesia |
| momb1255 | Mombum-Koneraw | family | Papunesia |
| naml1239 | Namla-Tofanma | family | Papunesia |
| nort1442 | North-Eastern Tasmanian | family | Australia |
| otom1276 | Otomaco-Taparita | family | South America |
| paho1240 | Pahoturi | family | Papunesia |
| pauw1244 | Pauwasi | family | Papunesia |
| piaw1238 | Piawi | family | Papunesia |
| ramu1234 | Ramu | family | Papunesia |
| rash1249 | Rashad | family | Africa |
| sign1238 | Sign Language | family | Africa, Australia, Eurasia, North America, Papunesia, South America |
| sout1293 | South-Eastern Tasmanian | family | Australia |
| suki1244 | Suki-Gogodala | family | Papunesia |
| taul1250 | Taulil-Butam | family | Papunesia |
| tege1244 | Tegem | family | Africa |
| tequ1244 | Tequistlatecan | family | North America |
| toro1256 | Tor-Orya | family | Papunesia |
| tura1263 | Turama-Kikori | family | Papunesia |
| wali1264 | Walioic | family | Papunesia |
| west1493 | West Bird's Head | family | Papunesia |
| west2604 | West Bomberai | family | Papunesia |
| west1503 | Western Tasmanian | family | Australia |
| xinc1237 | Xincan | family | North America |
| more1255 | Yam | family | Papunesia |
| yoku1255 | Yokutsan | family | North America |
| yuat1252 | Yuat | family | Papunesia |
| abin1243 | Abinomn | isolate | Papunesia |
| abun1252 | Abun | isolate | Papunesia |
| adai1235 | Adai | isolate | North America |
| alse1251 | Alsea-Yaquina | isolate | North America |
| anda1286 | Andaqui | isolate | South America |
| anem1249 | Anem | isolate | Papunesia |
| arut1244 | Arutani | isolate | South America |
| suar1238 | Asabano | isolate | Papunesia |
| atac1235 | Atacame | isolate | South America |
| atak1252 | Atakapa | isolate | North America |
| bang1363 | Bangime | isolate | Africa |
| beot1247 | Beothuk | isolate | North America |
| beto1236 | Betoi-Jirara | isolate | South America |
| boga1247 | Bogaya | isolate | Papunesia |
| burm1264 | Burmeso | isolate | Papunesia |
| cani1243 | Canichana | isolate | South America |
| cayu1241 | Cayuse | isolate | North America |
| chit1248 | Chitimacha | isolate | North America |
| chon1248 | Chono | isolate | South America |
| coah1252 | Coahuilteco | isolate | North America |
| come1251 | Comecrudan | isolate | North America |
| coto1248 | Cotoname | isolate | North America |
| cuit1236 | Cuitlatec | isolate | North America |
| cull1235 | Culli | isolate | South America |
| dama1272 | Damal | isolate | Papunesia |
| demm1245 | Dem | isolate | Papunesia |
| dibi1240 | Dibiyaso | isolate | Papunesia |
| duna1248 | Duna | isolate | Papunesia |
| elam1244 | Elamite | isolate | Eurasia |
| else1239 | Elseng | isolate | Papunesia |
| esse1238 | Esselen | isolate | North America |
| etru1241 | Etruscan | isolate | Eurasia |
| fuyu1242 | Fuyug | isolate | Papunesia |
| guac1239 | Guachi | isolate | South America |
| guai1237 | Guaicurian | isolate | North America |
| guam1236 | Guamo | isolate | South America |
| gule1241 | Gule | isolate | Africa |
| hatt1246 | Hattic | isolate | Eurasia |
| hrus1242 | Hruso | isolate | Eurasia |
| iber1250 | Iberian | isolate | Eurasia |
| cent2045 | Jalaa | isolate | Africa |
| jira1235 | Jirajaran | isolate | South America |
| kaki1249 | Kaki Ae | isolate | Papunesia |
| kapo1250 | Kapori | isolate | Papunesia |
| kara1497 | Karami | isolate | Papunesia |
| kara1289 | Karankawa | isolate | North America |
| kari1254 | Kariri | isolate | South America |
| kehu1238 | Kehu | isolate | Papunesia |
| kena1236 | Kenaboi | isolate | Eurasia |
| kibi1239 | Kibiri | isolate | Papunesia |
| kimk1238 | Kimki | isolate | Papunesia |
| kolp1236 | Kol {Papua New Guinea} | isolate | Papunesia |
| kuja1239 | Kujarge | isolate | Africa |
| kute1249 | Kutenai | isolate | North America |
| laal1242 | Laal | isolate | Africa |
| mara1266 | Maratino | isolate | North America |
| moro1289 | Marori | isolate | Papunesia |
| mass1263 | Massep | isolate | Papunesia |
| mata1275 | Matanawí | isolate | South America |
| mawe1251 | Mawes | isolate | Papunesia |
| mero1237 | Meroitic | isolate | Africa |
| mimi1240 | Mimi-Gaudefroy | isolate | Africa |
| molo1262 | Molof | isolate | Papunesia |
| momu1241 | Momuna | isolate | Papunesia |
| mpur1239 | Mpur | isolate | Papunesia |
| guri1248 | Muno | isolate | Papunesia |
| mure1235 | Mure | isolate | South America |
| maku1246 | Máku | isolate | South America |
| natc1249 | Natchez | isolate | North America |
| niha1238 | Nihali | isolate | Eurasia |
| odia1239 | Odiai | isolate | Papunesia |
| omur1241 | Omurano | isolate | South America |
| bira1253 | Ongota | isolate | Africa |
| otii1244 | Oti | isolate | South America |
| oyst1235 | Oyster Bay-Big River-Little Swanport | isolate | Australia |
| pank1250 | Pankararú | isolate | South America |
| papi1255 | Papi | isolate | Papunesia |
| pawa1255 | Pawaia | isolate | Papunesia |
| paya1236 | Payagua | isolate | South America |
| pele1245 | Pele-Ata | isolate | Papunesia |
| puqu1242 | Puquina | isolate | South America |
| pura1257 | Purari | isolate | Papunesia |
| pyuu1245 | Pyu | isolate | Papunesia |
| rama1271 | Ramanos | isolate | South America |
| sali1253 | Salinan | isolate | North America |
| sape1238 | Sapé | isolate | South America |
| saus1247 | Sause | isolate | Papunesia |
| sech1236 | Sechuran | isolate | South America |
| shom1245 | Shom Peng | isolate | Eurasia |
| sius1254 | Siuslaw | isolate | North America |
| sulk1246 | Sulka | isolate | Papunesia |
| sume1241 | Sumerian | isolate | Eurasia |
| tabo1241 | Tabo | isolate | Papunesia |
| taia1239 | Taiap | isolate | Papunesia |
| take1257 | Takelma | isolate | North America |
| tall1235 | Tallán | isolate | South America |
| tamb1257 | Tambora | isolate | Papunesia |
| tana1288 | Tanahmerah | isolate | Papunesia |
| taru1236 | Taruma | isolate | South America |
| taua1242 | Tauade | isolate | Papunesia |
| timo1237 | Timote-Cuica | isolate | South America |
| timu1245 | Timucua | isolate | North America |
| touo1238 | Touo | isolate | Papunesia |
| tuxa1239 | Tuxá | isolate | South America |
| usku1243 | Usku | isolate | Papunesia |
| wiru1244 | Wiru | isolate | Papunesia |
| xuku1239 | Xukurú | isolate | South America |
| yale1246 | Yale | isolate | Papunesia |
| yele1255 | Yele | isolate | Papunesia |
| yera1243 | Yerakai | isolate | Papunesia |
| yetf1238 | Yetfa | isolate | Papunesia |
| yuru1243 | Yurumanguí | isolate | South America |

## Reproduce

```bash
python3 scripts/analyze_family_inventory.py
python3 scripts/test_family_inventory.py
```

The script reads only the frozen `baseline/original.html` plus the pinned research files under `research/phonology/vendor/glottolog-5.3/`. It does not modify production GlottoDelta data or semantics.
