# Unisermo — Benchmark di espressività generale (100 frasi)

**Data:** 14 novembre 2026. **Baseline canonica:** `main` commit `708d186337b8ac77dfc78e73d0fc299a839ab9de`.

## Disegno sperimentale

100 frasi italiane **distinte**, dieci per dominio, selezionate intenzionalmente; il campione non è casuale né rappresentativo della frequenza d'uso. L'esercizio misura **copertura espressiva proposta**, non comprensione spontanea di parlanti o LLM.

**Fedeltà** è un giudizio dell'analista sui contenuti, non un risultato del parser. **Parziale** indica perdita di informazione o un significato più forte/diverso. **Lacuna** indica che non è stata prodotta una traduzione fedele con le forme ratificate esaminate. Occorrono giudizi indipendenti prima di usare queste percentuali come statistica pubblicabile.

Il **parser** riconosce o rifiuta la sintassi delle proposte; non garantisce che il significato italiano sia identico. Le proposte sono state riviste dopo gli esiti CI iniziali: il risultato finale non è una valutazione cieca.

## Risultati aggiornati dopo revisione critica

| Esito semantico proposto | Numero |
|---|---:|
| Fedele | 64 |
| Parziale | 11 |
| Lacuna | 25 |

**Parser:** 75/75 forme candidate accettate, zero rigetti nell'esecuzione successiva alle correzioni ([CI #43597515871](https://github.com/andreabenetton/unisermo/actions/runs/43597515871)). Le 25 lacune non hanno una candidata da analizzare.

**Revisione approfondita:** [`REVIEW_38.md`](REVIEW_38.md) documenta le 38 criticità originarie, due delle quali risolte riutilizzando genitivo/quantità e riferimento nominale. Rimangono **36** casi problematici, non 36 radici mancanti.

## Distribuzione per dominio

| Dominio | Fedele | Parziale | Lacuna | Candidati accettati dal parser |
|---|---:|---:|---:|---:|
| Trasporto e mobilità | 5 | 4 | 1 | 9 |
| Oggetti e azioni quotidiane | 7 | 2 | 1 | 9 |
| Spazio e direzione | 6 | 1 | 3 | 7 |
| Tempo e sequenza | 6 | 1 | 3 | 7 |
| Famiglia e relazioni sociali | 5 | 2 | 3 | 7 |
| Conoscenza e comunicazione | 6 | 0 | 4 | 6 |
| Volontà, possibilità e obbligo | 9 | 0 | 1 | 9 |
| Quantità e misure | 5 | 1 | 4 | 6 |
| Qualità, stati ed emozioni | 7 | 0 | 3 | 7 |
| Logica, causa e astrazione | 8 | 0 | 2 | 8 |

## Principali conclusioni

1. **Esistono soluzioni composizionali trascurate.** `biks bis roda esan` collega due ruote alla bicicletta tramite il genitivo e la copula; E074 passa a fedele. In E091 la ripetizione di `trenem` conserva il referente e il contenuto, pur differendo stilisticamente dall'anafora italiana.
2. **Alcuni problemi sono di classificazione/valenza, non di nuovi lessemi.** `stru` già significa costruire ma manca il ruolo verbale nell'inventario eseguibile; `dok` insegna ma il ruolo dell'allievo come argomento necessita specificazione.
3. **La parentela produttiva evita un nuovo nome.** `filadel` = figlio di fratello/sorella (nipote nel senso di nephew/niece) è già parsato.
4. **Unità di misura e composizione numerica sono più forti di quanto apparisse.** 3 minuti = `senotodek sekun` (180 secondi); 100 tonnellate metriche = `sen megagram` (100 Mg). Mancano i frame che associano durata o massa alla proposizione, non necessariamente le unità.
5. **Attestazione non equivale a ratifica.** `amik` è `example_only`; `omni` è `decision_attested_not_indexed`. Evitare di usarli come vocaboli pienamente canonici in test di fedeltà.
6. **Le lacune semantiche rilevanti** riguardano direzione relativa, ritorno/arrivo a destinazione, stato persistente di immobilità, collegamento tra misure e oggetti, quantificazione con eccezioni, complemento interrogativo indiretto e reciprocità.

## Corpus integrale

### Trasporto e mobilità

| ID | Italiano | Unisermo candidato | Semantica | Motivazione |
|---|---|---|---|---|
| E001 | Il treno si muove. | `tren mova` | Fedele | mov intransitivo. |
| E002 | L'autobus non si muove. | `bus no mova` | Fedele | Negazione dell'evento. |
| E003 | La motocicletta si muove verso la strada. | `moto mova karviaad` | Fedele | -ad indica destinazione, non arrivo. |
| E004 | Il treno riprende a muoversi. | `tren remova` | Fedele | re- indica la ripresa. |
| E005 | Il camion trasporta un carico. | `kam portara kargem` | Fedele | portar con carico accusativo. |
| E006 | Il minibus si allontana dalla strada. | `minibus mova karviade` | Parziale | L'origine non codifica necessariamente l'allontanamento. |
| E007 | La bicicletta svolta a sinistra. | `bik mova` | Parziale | Mancano svolta e sinistra. |
| E008 | L'autobus si ferma alla fermata. | `bus demova` | Parziale | La fermata fisica non è nominata. |
| E009 | Il treno parte dalla stazione. | `tren admova` | Parziale | La stazione d'origine non è nominata. |
| E010 | L'automobile rallenta a causa del traffico. | — | Lacuna | Mancano velocità e traffico. |

### Oggetti e azioni quotidiane

| ID | Italiano | Unisermo candidato | Semantica | Motivazione |
|---|---|---|---|---|
| E011 | Vedo un telefono. | `i vidi fonem` | Fedele | Vedere con accusativo. |
| E012 | Prendo fisicamente dell'acqua. | `i feri akwaem` | Fedele | fer non implica possesso. |
| E013 | Tieni una ruota. | `u tenu rodaem` | Fedele | ten come mantenimento del vincolo. |
| E014 | Una persona costruisce una porta. | `uman faka portaem` | Parziale | fak indica fare/produrre, non precisamente costruire; stru è attestata ma non tipizzata come verbo nel parser e richiede una decisione di valenza. |
| E015 | Una persona spinge una porta. | `uman pela portaem` | Fedele | pel non implica spostamento riuscito. |
| E016 | La porta è chiusa. | `porta klus` | Fedele | Copula zero al presente. |
| E017 | Costruisco una casa. | `i faki domem` | Parziale | fak indica fare/produrre, più generico di costruire; la radice stru non ha ancora ruolo verbale/valenza formalizzati. |
| E018 | Una persona tira una bicicletta. | `uman traka bikem` | Fedele | Trazione senza implicare spostamento. |
| E019 | Un telefono cade. | `fon kada` | Fedele | kad per cadere. |
| E020 | Riparo un telefono guasto. | — | Lacuna | Mancano riparare e guasto. |

### Spazio e direzione

| ID | Italiano | Unisermo candidato | Semantica | Motivazione |
|---|---|---|---|---|
| E021 | Salgo. | `altmovi` | Fedele | altmov indica moto ascendente, senza specificare meta. |
| E022 | La bicicletta scende. | `bik basmova` | Fedele | basmov per movimento discendente. |
| E023 | Sposto una ruota dalla strada. | `movi rodaem karviade` | Fedele | mov causativo con oggetto e luogo di origine. |
| E024 | L'auto si muove verso la strada. | `kar mova karviaad` | Fedele | Destinazione marcata con -ad. |
| E025 | La porta è dentro la casa. | `porta esa domin` | Fedele | Copula esplicita es col predicato locativo domin; la copula zero locativa non è ancora implementata nel parser. |
| E026 | Una persona si muove insieme al fratello. | `uman mova kun adelo` | Fedele | Accompagnamento tramite kun. |
| E027 | L'automobile rimane immobile. | `kar inesa fiks` | Parziale | fiks indica fissità, più forte dell'assenza di moto. |
| E028 | La bicicletta è vicino alla casa. | — | Lacuna | Manca la relazione 'vicino a'. |
| E029 | La ruota si trova sopra la porta. | — | Lacuna | Relazione nominale 'sopra' non definita. |
| E030 | Il treno torna alla stazione. | — | Lacuna | Stazione e ritorno a luogo mancanti. |

### Tempo e sequenza

| ID | Italiano | Unisermo candidato | Semantica | Motivazione |
|---|---|---|---|---|
| E031 | Ho visto un treno. | `viddi trenem` | Fedele | Passato semplice di vid con oggetto. |
| E032 | Prenderai un telefono. | `ferfu fonem` | Fedele | Futuro di fer in seconda persona. |
| E033 | L'autobus si stava muovendo. | `bus moveda` | Fedele | Progressivo passato. |
| E034 | Il treno iniziò a muoversi. | `tren admovda` | Fedele | Inizio del moto al passato. |
| E035 | Ieri avevo intenzione di muovermi. | `intdi mov` | Parziale | Non specifica ieri. |
| E036 | L'autobus si muove ogni mattina. | — | Lacuna | Mattina e frequenza calendariale assenti. |
| E037 | Il movimento del treno finisce prima che inizi quello dell'autobus. | `tren mova pretem bus mova` | Fedele | pretem richiede intervalli non sovrapposti. |
| E038 | La madre ha visto un telefono e il padre vedrà un treno. | `gene vidda fonem e geno vidfa trenem` | Fedele | Due clausole coordinate con tempi diversi. |
| E039 | Il conducente parcheggia per tre minuti. | — | Lacuna | Il conducente e parcheggiare non sono canonici. Tre minuti possono essere misurati come senotodek sekun (180 s); manca però un frame di durata dell'evento. |
| E040 | Il volo arriva alle dieci del mattino. | — | Lacuna | Volo-servizio, arrivo e fascia oraria mancanti. |

### Famiglia e relazioni sociali

| ID | Italiano | Unisermo candidato | Semantica | Motivazione |
|---|---|---|---|---|
| E041 | Il padre vede la madre. | `geno vida geneem` | Fedele | Nomi familiari e accusativo. |
| E042 | La madre insegna al proprio figlio. | `gene doka genes filem` | Parziale | Il genitivo genes specifica 'il figlio della madre'; resta da ratificare la valenza di dok verso l'allievo/beneficiario (accusativo diretto non prova equivalenza a 'insegnare a'). |
| E043 | Il fratello vede la sorella. | `adelo vida adeleem` | Fedele | Due radici familiari canoniche. |
| E044 | La nonna materna vede il padre. | `genegene vida genoem` | Fedele | Genegene è nonna materna. |
| E045 | La sorella insegna al cugino. | `adele doka filadelgenem` | Parziale | La valenza 'insegnare a' rimane distinta dall'accusativo. |
| E046 | Il padre sa che il figlio si muove. | `geno sap fil mova` | Fedele | sap con proposizione finita. |
| E047 | La madre vede un treno e il padre prende un telefono. | `gene vida trenem e geno fera fonem` | Fedele | Coordinazione con due soggetti e verbi diversi. |
| E048 | Un nipote ringrazia una zia. | — | Lacuna | La relazione nipote di zia/zio è già derivabile come filadel (figlio del fratello o della sorella), verificato dal parser; manca il verbo ringraziare. |
| E049 | Due fratelli si aiutano reciprocamente. | — | Lacuna | Aiutare e reciproco mancanti. |
| E050 | Due amici conversano. | — | Lacuna | amik è presente come attestazione example_only, non come lemma ratificato; manca una costruzione canonica per conversare reciprocamente (kundik significherebbe solo dire insieme). |

### Conoscenza e comunicazione

| ID | Italiano | Unisermo candidato | Semantica | Motivazione |
|---|---|---|---|---|
| E051 | Penso. | `pensi` | Fedele | Attività pensare intransitiva. |
| E052 | So che l'autobus si muove. | `i sap bus mova` | Fedele | sap proposizionale, fattivo. |
| E053 | Credo che il camion si muova. | `i kred kam mova` | Fedele | kred proposizionale non fattivo. |
| E054 | So come muovermi. | `sapi mov` | Fedele | Conoscenza procedurale. |
| E055 | Imparo come insegnare. | `adsapi dok` | Fedele | Acquisizione della conoscenza procedurale. |
| E056 | Una persona ascolta un messaggio vocale. | — | Lacuna | Mancano ascoltare e messaggio, distinti da vedere o chiamare. |
| E057 | Vedi una bicicletta? | `ka u vidu bikem` | Fedele | In Unisermo la particella interrogativa ka è iniziale, non finale. |
| E058 | Annuncio che la strada è chiusa. | — | Lacuna | Annuncio proposizionale e chiusura viaria non definiti. |
| E059 | Chiedi quando partirà l'autobus. | — | Lacuna | Interrogativa indiretta temporale non definita. |
| E060 | Il passeggero comprende la spiegazione del conducente. | — | Lacuna | Ruoli e contenuto della spiegazione mancanti. |

### Volontà, possibilità e obbligo

| ID | Italiano | Unisermo candidato | Semantica | Motivazione |
|---|---|---|---|---|
| E061 | Posso muovermi perché ne ho la capacità. | `poti mov` | Fedele | pot è capacità, non opportunità. |
| E062 | Voglio vedere il treno. | `voli vid trenem` | Fedele | vol con azione dipendente e accusativo. |
| E063 | Intendo trasportare acqua. | `inti portar akwaem` | Fedele | int con azione dipendente e oggetto. |
| E064 | Ho l'obbligo di non muovermi. | `debi no mov` | Fedele | Obbligo di non muoversi. |
| E065 | Ho il permesso di prendere il telefono. | `auti fer fonem` | Fedele | aut con azione fisica dipendente. |
| E066 | In passato ho tentato di trasportare un carico. | `tentdi portar kargem` | Fedele | Tentativo passato con portare, senza successo implicito. |
| E067 | Non sono obbligato a muovermi. | `no debi mov` | Fedele | Negazione dell'obbligo. |
| E068 | Voglio che tu ti muova. | `i vol u movu` | Fedele | Proposizione con soggetto subordinato diverso. |
| E069 | So che ti sei mosso. | `i sap u movdu` | Fedele | sap proposizionale con subordinata passata. |
| E070 | Potrei guidare un autobus se avessi la patente. | — | Lacuna | Guidare, patente e controfattuale non coperti. |

### Quantità e misure

| ID | Italiano | Unisermo candidato | Semantica | Motivazione |
|---|---|---|---|---|
| E071 | Due autobus trasportano persone. | `bis bus portaran wi umanem` | Fedele | Numerale nel soggetto, verbo plurale e oggetto plurale. |
| E072 | Cinque persone vedono un treno. | `kin uman vidan trenem` | Fedele | Soggetto quantificato con verbo plurale e oggetto. |
| E073 | Tre ruote cadono. | `ter roda kadan` | Fedele | Numerale ter con evento plurale. |
| E074 | La bicicletta possiede due ruote. | `biks bis roda esan` | Fedele | Genitivo biks + bis roda + copula es plurale: esistono due ruote appartenenti alla bicicletta; sintassi e possesso analizzati dal parser. Non implica un vincolo esclusivo 'esattamente due'. |
| E075 | Il camion trasporta due carichi. | `kam portara bis kargem` | Fedele | Numerale nel sintagma accusativo. |
| E076 | Il carico ha massa di un chilogrammo. | — | Lacuna | La misura uno kilogram è già disponibile (unità di massa). Manca un predicato stabile di massa e il frame che associa misura e oggetto; non introdurre una nuova unità. |
| E077 | Il treno pesa cento tonnellate. | — | Lacuna | La massa di cento tonnellate metriche è esprimibile come sen megagram in una misura (equivalenza 100 Mg); manca il predicato 'pesare/avere massa' e la sintassi per applicare la misura al treno. Non serve una nuova unità tonnellata. |
| E078 | Quattro biciclette si muovono e due auto restano ferme. | `for bik movan e bis kar no movan` | Parziale | Esprime correttamente 'quattro bici si muovono e due auto non si muovono', ma omette la persistenza implicata da 'restano ferme'. Evita il più forte fiks ('fisso'). |
| E079 | L'automobile percorre cinque chilometri. | — | Lacuna | Distanza e percorso non definiti. |
| E080 | Il minibus possiede quindici sedili. | — | Lacuna | Mancano il nome 'sedile' e un frame possessivo/dotazione; kunten descrive contenimento fisico attuale, non posti installati o capacità omologata. |

### Qualità, stati ed emozioni

| ID | Italiano | Unisermo candidato | Semantica | Motivazione |
|---|---|---|---|---|
| E081 | La porta è aperta. | `porta aper` | Fedele | Predicato qualitativo presente. |
| E082 | Il telefono è fisso. | `fon fiks` | Fedele | Proprietà fisica ratificata. |
| E083 | Il telefono è intelligente (tecnologicamente). | `fon smart` | Fedele | smart è funzionalità tecnologica. |
| E084 | La bicicletta è bella. | `bik bel` | Fedele | Qualità estetica. |
| E085 | L'automobile è buona. | `kar bon` | Fedele | Valutazione generale positiva. |
| E086 | La madre continua a essere buona. | `gene inesa bon` | Fedele | ines conserva stato qualitativo. |
| E087 | Il bambino è felice. | — | Lacuna | Bambino per età e felicità mancanti. |
| E088 | L'autista è nervoso. | — | Lacuna | Autista e nervosismo mancanti. |
| E089 | La strada è pericolosa. | — | Lacuna | Pericolo non coperto da nelegal. |
| E090 | Una persona è giusta. | `uman just` | Fedele | Giustizia come predicato. |

### Logica, causa e astrazione

| ID | Italiano | Unisermo candidato | Semantica | Motivazione |
|---|---|---|---|---|
| E091 | Il fratello vede il treno e la sorella non lo vede. | `adelo vida trenem e adele no vida trenem` | Fedele | Ripetere trenem in entrambe le proposizioni conserva le condizioni di verità con lo stesso referente definito; differisce solo l'economia anaforica dell'italiano ('lo'), non il contenuto proposizionale. |
| E092 | La madre vede un'auto oppure il padre vede un camion. | `gene vida karem o geno vida kamem` | Fedele | Disgiunzione inclusiva tra due osservazioni. |
| E093 | Se il camion si muove, allora il carico si muove. | `se kam mova alor karg mova` | Fedele | Condizionale di due eventi fisici, non causalità asserita. |
| E094 | Voglio muovermi, ma non posso muovermi. | `voli mov ma no poti mov` | Fedele | Desiderio coordinato avversativamente con mancanza di capacità. |
| E095 | È possibile che il telefono cada. | `pos fon kada` | Fedele | Possibilità proposizionale di caduta. |
| E096 | È necessario che la porta sia aperta. | `deb porta esa aper` | Fedele | Necessità proposizionale su uno stato espresso da una proposizione con copula finita. |
| E097 | Non è necessario che tu insegni. | `no deb u doku` | Fedele | Negazione della necessità proposizionale. |
| E098 | Il camion trasporta un carico perché il treno non si muove. | `kam portara kargem due tren no mova` | Fedele | Causalità fattuale; il mancato movimento del treno spiega il trasporto alternativo. |
| E099 | Tutti gli autobus tranne uno si muovono. | — | Lacuna | L'operatore ekse è confermato, omni ('tutti') è solo decision_attested_not_indexed; non esiste ancora sintassi ratificata per legare l'eccezione a un insieme quantificato ('tutti tranne uno'). |
| E100 | Se l'autobus si guasta, tutti i passeggeri protestano. | — | Lacuna | Guasto, passeggeri e protesta non ratificati. |

## Riproduzione

Dalla root del repository: `python -m benchmarks.expressivity100.run`. Sorgente: [`cases.json`](cases.json). Parser probe: [`review_probes.py`](review_probes.py). Esecuzione automatizzata: [workflow](../../.github/workflows/expressivity100.yml).

**Nessuna nuova ratifica grammaticale o lessicale discende dal benchmark.** I cambiamenti nella PR riguardano esclusivamente i materiali di analisi.
