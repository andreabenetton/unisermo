# Unisermo — Expressivity-100

**Data:** 14 novembre 2026. **Baseline canonica:** `main` al commit `708d186337b8ac77dfc78e73d0fc299a839ab9de`.

## Metodo

100 frasi italiane distinte, distribuite in dieci domini da 10 casi ciascuno. Nessuna radice o regola non ratificata è stata introdotta per costruire le traduzioni.
Giudizio semantico proposto dall'analista: **fedele**, **parziale** oppure **lacuna**. La sintassi delle espressioni proposte viene verificata indipendentemente con il parser ufficiale.
Non è una prova di comprensione umana e non è un campione casuale rappresentativo: le percentuali sono descrittive del corpus, non della lingua nel suo complesso.

## Risultato

| Semantica proposta | Casi |
|---|---:|
| Fedele | 62 |
| Parziale | 13 |
| Lacuna | 25 |

**Parser:** 75/75 proposte accettate, nessuna analisi tentata per le lacune. [CI verificata — GitHub Actions 43596418583](https://github.com/andreabenetton/unisermo/actions/runs/43596418583). L'accettazione grammaticale non dimostra fedeltà semantica.

## Distribuzione per dominio

| Dominio | Fedele | Parziale | Lacuna |
|---|---:|---:|---:|
| Trasporto e mobilità | 5 | 4 | 1 |
| Oggetti e azioni quotidiane | 7 | 2 | 1 |
| Spazio e direzione | 6 | 1 | 3 |
| Tempo e sequenza | 6 | 1 | 3 |
| Famiglia e relazioni sociali | 5 | 2 | 3 |
| Conoscenza e comunicazione | 6 | 0 | 4 |
| Volontà, possibilità e obbligo | 9 | 0 | 1 |
| Quantità e misure | 4 | 2 | 4 |
| Qualità, stati ed emozioni | 7 | 0 | 3 |
| Logica, causa e astrazione | 7 | 1 | 2 |

## Risultati qualitativi

**Punti forti:** coniugazione e tempi, movimento e forza fisica, negazioni, domande dirette, sapere/credere, intenzione, obbligo, permesso, condizionali, coordinazioni e causalità. Le costruzioni proposte sono state verificate senza modifiche alla grammatica.

**Lacune prioritarie:**

- **Trasporto e servizi:** fermata, stazione, conducente, passeggero, guidare, traffico, biglietto, ritardo, sosta/parcheggio.
- **Vita quotidiana:** riparare, ascoltare, messaggio e alcune relazioni topologiche precise.
- **Tempo e misure:** ieri, mattina, frequenza calendariale, attribuzione di massa, distanze percorse.
- **Relazioni ed emozioni:** amicizia, aiutare reciprocamente, ringraziare, felicità, nervosismo e pericolosità.
- **Distinguere lessico e categoria/valenza:** `stru` è una radice canonica col senso di costruire/struttura, ma non è classificata come verbo nel parser. E014/E017 adottano `fak` con perdita semantica; non serve necessariamente un'altra radice.
- **Possesso, anafora e parti:** E074 riproduce soltanto l'esistenza di due ruote, E091 ripete il nome anziché usare il pronome italiano 'lo'. Verificare come sfruttare genitivo e sintassi delle parti prima di creare nuovi lessemi.

## Limiti di interpretazione

La selezione è intenzionale, e le valutazioni sono formulate da un solo analista. Gli esempi coerenti con il lessico conosciuto sono sovrarappresentati rispetto a un dialogo spontaneo. Il 75/75 è stato ottenuto anche correggendo alcune formulazioni candidate dopo il primo controllo: non è un risultato cieco né una misura dell'accuratezza su input arbitrari.
Il parser è un riconoscitore strutturale; non valuta verità, plausibilità, ruolo tematico sottinteso o equivalenza italiano/Unisermo.

## Corpus completo

### Trasporto e mobilità

| ID | Italiano | Unisermo proposto | Esito | Motivazione |
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

| ID | Italiano | Unisermo proposto | Esito | Motivazione |
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

| ID | Italiano | Unisermo proposto | Esito | Motivazione |
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

| ID | Italiano | Unisermo proposto | Esito | Motivazione |
|---|---|---|---|---|
| E031 | Ho visto un treno. | `viddi trenem` | Fedele | Passato semplice di vid con oggetto. |
| E032 | Prenderai un telefono. | `ferfu fonem` | Fedele | Futuro di fer in seconda persona. |
| E033 | L'autobus si stava muovendo. | `bus moveda` | Fedele | Progressivo passato. |
| E034 | Il treno iniziò a muoversi. | `tren admovda` | Fedele | Inizio del moto al passato. |
| E035 | Ieri avevo intenzione di muovermi. | `intdi mov` | Parziale | Non specifica ieri. |
| E036 | L'autobus si muove ogni mattina. | — | Lacuna | Mattina e frequenza calendariale assenti. |
| E037 | Il movimento del treno finisce prima che inizi quello dell'autobus. | `tren mova pretem bus mova` | Fedele | pretem richiede intervalli non sovrapposti. |
| E038 | La madre ha visto un telefono e il padre vedrà un treno. | `gene vidda fonem e geno vidfa trenem` | Fedele | Due clausole coordinate con tempi diversi. |
| E039 | Il conducente parcheggia per tre minuti. | — | Lacuna | Conducente, parcheggiare e minuto mancanti. |
| E040 | Il volo arriva alle dieci del mattino. | — | Lacuna | Volo-servizio, arrivo e fascia oraria mancanti. |

### Famiglia e relazioni sociali

| ID | Italiano | Unisermo proposto | Esito | Motivazione |
|---|---|---|---|---|
| E041 | Il padre vede la madre. | `geno vida geneem` | Fedele | Nomi familiari e accusativo. |
| E042 | La madre insegna al proprio figlio. | `gene doka filem` | Parziale | Il destinatario e il possesso non sono codificati esattamente. |
| E043 | Il fratello vede la sorella. | `adelo vida adeleem` | Fedele | Due radici familiari canoniche. |
| E044 | La nonna materna vede il padre. | `genegene vida genoem` | Fedele | Genegene è nonna materna. |
| E045 | La sorella insegna al cugino. | `adele doka filadelgenem` | Parziale | La valenza 'insegnare a' rimane distinta dall'accusativo. |
| E046 | Il padre sa che il figlio si muove. | `geno sap fil mova` | Fedele | sap con proposizione finita. |
| E047 | La madre vede un treno e il padre prende un telefono. | `gene vida trenem e geno fera fonem` | Fedele | Coordinazione con due soggetti e verbi diversi. |
| E048 | Un nipote ringrazia una zia. | — | Lacuna | Ringraziare e rapporto nipote insufficienti. |
| E049 | Due fratelli si aiutano reciprocamente. | — | Lacuna | Aiutare e reciproco mancanti. |
| E050 | Due amici conversano. | — | Lacuna | Amico e conversare mancanti. |

### Conoscenza e comunicazione

| ID | Italiano | Unisermo proposto | Esito | Motivazione |
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

| ID | Italiano | Unisermo proposto | Esito | Motivazione |
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

| ID | Italiano | Unisermo proposto | Esito | Motivazione |
|---|---|---|---|---|
| E071 | Due autobus trasportano persone. | `bis bus portaran wi umanem` | Fedele | Numerale nel soggetto, verbo plurale e oggetto plurale. |
| E072 | Cinque persone vedono un treno. | `kin uman vidan trenem` | Fedele | Soggetto quantificato con verbo plurale e oggetto. |
| E073 | Tre ruote cadono. | `ter roda kadan` | Fedele | Numerale ter con evento plurale. |
| E074 | La bicicletta possiede due ruote. | `bis roda esan` | Parziale | Due ruote esistono: quantità espressa, ma manca il vincolo di appartenenza alla bicicletta. |
| E075 | Il camion trasporta due carichi. | `kam portara bis kargem` | Fedele | Numerale nel sintagma accusativo. |
| E076 | Il carico ha massa di un chilogrammo. | — | Lacuna | Unità nota, predicazione della massa non attestata. |
| E077 | Il treno pesa cento tonnellate. | — | Lacuna | Peso e misura di tonnellata mancanti. |
| E078 | Quattro biciclette si muovono e due auto restano ferme. | `for bik movan e bis kar esan fiks` | Parziale | fiks è fissità, non solo assenza di movimento. |
| E079 | L'automobile percorre cinque chilometri. | — | Lacuna | Distanza e percorso non definiti. |
| E080 | Il minibus possiede quindici sedili. | — | Lacuna | Sedile e dotazione non definiti. |

### Qualità, stati ed emozioni

| ID | Italiano | Unisermo proposto | Esito | Motivazione |
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

| ID | Italiano | Unisermo proposto | Esito | Motivazione |
|---|---|---|---|---|
| E091 | Il fratello vede il treno e la sorella non lo vede. | `adelo vida trenem e adele no vida trenem` | Parziale | La seconda proposizione ripete 'treno' invece di riprendere il referente con 'lo'; significato pragmatico sostanzialmente simile, ma l'anafora non è codificata. |
| E092 | La madre vede un'auto oppure il padre vede un camion. | `gene vida karem o geno vida kamem` | Fedele | Disgiunzione inclusiva tra due osservazioni. |
| E093 | Se il camion si muove, allora il carico si muove. | `se kam mova alor karg mova` | Fedele | Condizionale di due eventi fisici, non causalità asserita. |
| E094 | Voglio muovermi, ma non posso muovermi. | `voli mov ma no poti mov` | Fedele | Desiderio coordinato avversativamente con mancanza di capacità. |
| E095 | È possibile che il telefono cada. | `pos fon kada` | Fedele | Possibilità proposizionale di caduta. |
| E096 | È necessario che la porta sia aperta. | `deb porta esa aper` | Fedele | Necessità proposizionale su uno stato espresso da una proposizione con copula finita. |
| E097 | Non è necessario che tu insegni. | `no deb u doku` | Fedele | Negazione della necessità proposizionale. |
| E098 | Il camion trasporta un carico perché il treno non si muove. | `kam portara kargem due tren no mova` | Fedele | Causalità fattuale; il mancato movimento del treno spiega il trasporto alternativo. |
| E099 | Tutti gli autobus tranne uno si muovono. | — | Lacuna | Quantificazione con eccezione di insieme non dimostrata. |
| E100 | Se l'autobus si guasta, tutti i passeggeri protestano. | — | Lacuna | Guasto, passeggeri e protesta non ratificati. |

## Riproduzione

Dal checkout del repository: `python -m benchmarks.expressivity100.run`. Il corpus è in [`cases.json`](cases.json), il runner in [`run.py`](run.py), l'esecuzione nella workflow [Expressivity-100](../../.github/workflows/expressivity100.yml).

**Stato:** benchmark proposto in PR draft; nessuna modifica a lessico, grammatica, parser o altri test.
