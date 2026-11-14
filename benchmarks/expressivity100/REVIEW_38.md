# Unisermo — Revisione critica delle 38 frasi problematiche

**Data:** 14 novembre 2026. **Sorgenti:** lessico canonico, grammatica, parser di `main` alla baseline `708d186337b8ac77dfc78e73d0fc299a839ab9de`; benchmark `cases.json` nella PR #96.

## Risultato e metodologia

Questo documento ricontrolla **tutte le 38** frasi originariamente classificate parziali (13) o lacunose (25). Distinguere il **significato linguistico** da un fatto di **implementazione del parser** è necessario: l'accettazione del parser non verifica che la traduzione sia equivalente, e una radice con significato attestato non è automaticamente tipizzata per tutte le funzioni.

**Due casi sono stati corretti a 'fedele' senza alcuna nuova radice né grammatica:** E074 (genitivo e quantità delle ruote) ed E091 (ripetizione esplicita dello stesso treno). Il quadro aggiornato è **64 fedeli, 11 parziali, 25 lacune**, quindi **36 casi ancora problematici**.

Le altre 36 voci non vanno confuse con 36 nuove radici necessarie: molte condividono un singolo problema riutilizzabile, per esempio la valenza di `dok`, un predicato di misura o la nozione di durata. Classificazione primaria e non esclusiva:

| Classe | Significato | Casi |
|---|---|---:|
| **R** | Risolto con la grammatica esistente | 2 |
| **P** | Formalizzazione di radice/valenza già disponibile | 4 |
| **L** | Lacuna soprattutto lessicale | 12 |
| **S** | Lacuna soprattutto di sintassi/semantica | 8 |
| **M** | Mista (lessico + sintassi/semantica) | 12 |

## Riscontri verificati sul parser

- `biks bis roda esan`: riconosciuta come proposizione copulare con soggetto `bis roda` e possessore genitivo `biks`, numerale 2. Non impone un conteggio **esclusivo** di esattamente due ruote oltre alle normali implicature linguistiche.
- `filadel` e `filadelem`: analizzati come parentela produttiva `fil + adel` (figlio di un fratello o di una sorella).
- `gene doka genes filem`: analizzata come frase SVO con genitivo `genes`. Il parser non decide se l'accusativo di `dok` codifichi propriamente l'allievo.
- `uman strua portaem`: rifiutata; `stru` è canonica col senso 'costruire/struttura', ma rimane indicizzata come `root`, non come verbo.
- `bis kar no movan`: accettata, senza l'eccesso semantico di `fiks`; non significa di per sé 'continuano a restare ferme'.
- `omni`: registrato in indice come `decision_attested_not_indexed`, **non** `confirmed_lexicon`. `amik`: `example_only`. `ekse`: confermato, ma la sintassi generale di esclusione quantificata non è completamente ratificata.
- `senotodek` è 180 e `sekun` è l'unità di durata: tre minuti si possono rendere quantitativamente con 180 secondi. `sen megagram` equivale a 100 tonnellate metriche: manca associare la misura a un'entità, non l'unità.

**Evidenza eseguibile:** [GitHub Actions — probe run 43597407934](https://github.com/andreabenetton/unisermo/actions/runs/43597407934) e [`review_probes.py`](review_probes.py). Le prove non inseriscono nuove forme nel lessico.

## Revisione voce per voce

| ID | Esito attuale | Categoria | Cosa sappiamo | Intervento minimo |
|---|---|---|---|---|
| E006 | Parziale | S | `mov ... karviade` esprime provenienza, non distanza crescente dalla strada. | Relazione direzionale 'allontanarsi' verificabile, senza ridefinire `-de`. |
| E007 | Parziale | M | `bik mova` perde sia il cambio di direzione sia il lato sinistro. | Concetti destra/sinistra e predicato 'svoltare'; specificare la relazione di direzione. |
| E008 | Parziale | L | `demov` codifica già l'arresto del moto. | Una sola voce per il luogo di fermata designato; valutare formazione da movimento prima di altra radice. |
| E009 | Parziale | L | `admov` codifica partenza/inizio del moto e `-de` l'origine. | Voce per stazione; `tren admova STAZIONE-de` è schema da verificare dopo ratifica del nome. |
| E010 | Lacuna | M | La causalità `due` esiste, ma non la variazione negativa di velocità né il traffico. | Velocità/variazione nel tempo, traffico; non confondere `demov` con rallentare. |
| E014 | Parziale | P | `stru` è confermata con il significato 'costruire/struttura', ma indicizzata come `root`: `strua` non è analizzata. | Chiarire categoria verbale e valenza con oggetto; un nuovo sinonimo di costruire è superfluo. |
| E017 | Parziale | P | Stessa lacuna di E014: `fak` produce, ma non significa necessariamente costruire. | Formalizzare l'uso transitivo di `stru`, poi verificare `strui domem`. |
| E020 | Lacuna | L | La fase `re-` significa ripresa, non riparazione. | Radice per riparare e proprietà guasto/rotto; precisare differenza da rifare. |
| E027 | Parziale | S | `fiks` significa stabilmente fissato; `no mova` non esprime persistenza. | Esprimere permanenza di assenza di moto o stato 'immobile' senza inventare `ines no mov`. |
| E028 | Lacuna | S | Il locativo `-in` esprime luogo interno/situato, non vicinanza. | Relatore spaziale di prossimità e frame con secondo riferimento nominale. |
| E029 | Lacuna | S | `alt` è alto/su, non una preposizione già ratificata 'sopra X'. | Definire localizzazione relativa orientata (sopra/sotto) usando le radici esistenti dove possibile. |
| E030 | Lacuna | M | `re-` su `mov` significa riprendere il moto, non tornare a un luogo precedente. | Nome stazione e semantica di ritorno a destinazione precedentemente occupata. |
| E035 | Parziale | L | `intdi mov` esprime intenzione passata ma non il giorno precedente. | Deissi temporale di 'ieri' o regola produttiva giorno-1, senza confondere `pretem` con un giorno. |
| E036 | Lacuna | M | `omni` è attestato ma non pienamente confermato; non c'è mattina né quantificazione abituale di giorni. | Radice/composto per mattina e frame di frequenza 'ogni mattina'. |
| E039 | Lacuna | M | Tre minuti = 180 secondi: `senotodek sekun` è disponibile come misura; manca applicarla come durata. Conducente e parcheggiare assenti. | Verbo parcheggiare, agente conducente derivabile da un futuro verbo di guida, frame di durata. |
| E040 | Lacuna | M | `aerplan` = aeroplano fisico, non volo-servizio; `admov` non garantisce arrivo. | Nome volo/servizio, arrivo con raggiungimento della meta, tempo dell'orologio. |
| E042 | Parziale | P | `gene doka genes filem` è accettata dal parser: genitivo `genes` risolve 'proprio figlio'. | Documentare se l'accusativo di `dok` rappresenti la persona istruita e la relazione insegnare-a. |
| E045 | Parziale | P | `adele doka filadelgenem` è parsata; manca una decisione sui ruoli dell'oggetto di `dok`. | Come E042: specificare valenza di insegnamento, non aggiungere un secondo verbo senza motivo. |
| E048 | Lacuna | L | `filadel` (figlio di fratello/sorella) è già produttivo e parsato: niente nuova radice 'nipote'. | Solo radice per ringraziare; collegare il referente della zia se il testo lo richiede. |
| E049 | Lacuna | M | `kun-` = azione insieme, non aiutarsi in senso reciproco. | Radice aiutare e costruzione reciproca oppure due azioni con agenti invertiti. |
| E050 | Lacuna | L | `amik` esiste solo come `example_only`; `dik` = dire, non necessariamente dialogare. | Confermare/rigettare `amik`; chiarire verbo dialogare oppure composizione controllata di turni di parola. |
| E056 | Lacuna | L | `vok` è voce/chiamare come `root` generica, non ascoltare; manca messaggio come oggetto. | Radice ascoltare, nome messaggio e attributo vocale/sonoro (eventualmente derivabile da `vok`). |
| E058 | Lacuna | M | `dik` non implica annunciare pubblicamente; manca frame per riportare una proposizione finita. | Decidere valenza dichiarativa/comunicativa e interpretazione di strada 'chiusa al traffico'. |
| E059 | Lacuna | M | `kan` esprime 'quando?' diretto, non una domanda indiretta; manca chiedere e partenza come evento. | Verbo chiedere con interrogativa incorporata; verificare incassamento di `kan` e partenza. |
| E060 | Lacuna | L | `kap` significa già comprendere, ma passeggero, conducente e spiegazione mancano. | Denominare ruoli e contenuto esplicativo; conducente da guida+`-or` se il verbo verrà ratificato. |
| E070 | Lacuna | M | `pot`/`aut` non codificano da soli il controfattuale; mancano guida e documento patente. | Capacità condizionale non fattuale, guida, documento abilitante. |
| E074 | Risolto | R | `biks bis roda esan` è accettata con genitivo possessivo e numerale 2; riproduce le due ruote della bici. | Nessuna nuova radice o regola; traduzione migliorata nel corpus. |
| E076 | Lacuna | S | `uno kilogram` e l'unità di massa sono già canonici; manca predicazione del valore misurato. | Frame 'X ha massa M' o radice di misura con valenza; non cambiare `gram`. |
| E077 | Lacuna | S | 100 tonnellate metriche = 100 megagrammi: il sistema `mega+gram` è sufficiente per il valore. | Stesso predicato/frame di massa di E076; nessuna nuova unità 'tonnellata' necessaria. |
| E078 | Parziale | S | `bis kar no movan` evita il troppo forte `fiks`, ma non implica che le auto *restino* ferme. | Semantica di permanenza nello stato 'non in movimento', non mera negazione locale. |
| E079 | Lacuna | M | `mov` codifica movimento, non distanza effettivamente percorsa. | Unità di lunghezza (ad es. metro) e frame 'percorrere distanza D', senza inferirla da una meta. |
| E080 | Lacuna | L | Il genitivo + esistenziale usato in E074 può esprimere dotazione di oggetti contabili. | Voce per sedile; verificare conteggio dei sedili del minibus tramite genitivo/`es`. |
| E087 | Lacuna | L | `fil` significa discendente e non bambino per età; felicità non è una qualità ratificata. | Nominazione dell'età infantile e proprietà emotiva felice. |
| E088 | Lacuna | L | `dirig` = dirigere, non necessariamente guidare un veicolo; nervosismo manca. | Verbo guidare/condurre con `-or` per autista e proprietà nervoso. |
| E089 | Lacuna | L | `nelegal` esprime illegalità, non rischio/pericolo. | Qualità pericoloso o base rischio con derivazione semanticamente adeguata. |
| E091 | Risolto | R | Ripetere `trenem` nel secondo membro mantiene il referente e le condizioni di verità. | Nessuna nuova grammatica; anafora più compatta può restare un miglioramento stilistico. |
| E099 | Lacuna | S | `ekse` è ratificato ma il legame tra quantificatore e insieme delle eccezioni non lo è; `omni` è solo attestato. | Definire `tutti X tranne uno` con ambito preciso, confermando prima lo stato di `omni`. |
| E100 | Lacuna | M | Mancano guastarsi, passeggero, protestare; il quantificatore universale deve ancora essere chiarito. | Radici per guasto/protesta/ruolo passeggero e frame universale verificato. |

## Priorità strutturali: prima di ratificare nuove parole

1. **P0 — Allineare radici già disponibili e valenze** (E014, E017, E042, E045). `stru` = costruire/struttura è confermata come forma, ma il suo uso verbale non è nel sottoinsieme operativo. `dok` = insegnare è noto, ma il ruolo della persona cui si insegna deve essere dichiarato. Nessuna radice nuova prima di chiarirli.
2. **P1 — Componenti generalizzabili:** una costruzione per legare una misura a un soggetto (E076/E077), una per permanenza di non-movimento (E027/E078), una per posizioni relative fra due nomi (E028/E029), una per quantificazione con eccezioni (E099). Queste quattro aree spiegano diversi fallimenti senza nuovi nomi di oggetti.
3. **P1 — Vocabolario operativo riutilizzabile:** stazione, fermata, guidare, passeggero, parcheggiare, ascoltare, messaggio, riparare, sedile, rischio/pericolo, ringraziare. Specificare il minimo necessario per un dominio; non trasformare le proposte in canoniche senza ratifica.
4. **P2 — Calendario, durata e movimento telico:** ieri, mattina, ricorrenza, ritorno verso un luogo precedente, arrivo effettivo a destinazione, tempo dell'orologio. `admov` = avvio del moto e `remov` = ripresa del moto **non** devono essere ridefiniti come 'arrivare' o 'tornare'.
5. **P2 — Relazioni sociali ed emozioni:** amico (`amik` è solo esempio), aiutare reciprocamente, dialogare, felicità, nervosismo. Derivazioni come agente `V-or` e parentela `filadel` riducono il numero di radici nuove.

## Opportunità di risparmio lessicale

| Bisogno | Risorsa già presente | Cosa manca ancora |
|---|---|---|
| Fermarsi alla fermata | `demov` = cessare movimento | nome del luogo di fermata |
| Partire da stazione | `admov` + origine `-de` | nome stazione |
| Autista/conducente | suffisso agentivo `-or` | verbo di guida con valenza di veicolo |
| Nipote di zio/zia | `filadel` produttivo | solo verbo ringraziare per E048 |
| Due ruote della bici | `biks bis roda esan` | nulla per E074 |
| Tre minuti | `senotodek sekun` = 180 secondi | legame di durata dell'evento |
| Cento tonnellate metriche | `sen megagram` = 100 Mg | predicato di massa e suo frame |
| Proprietà di sedili | genitivo del minibus + esistenziale | radice sedile |
| 'Lo' riferito al treno | ripetizione `trenem` | nessuno per proposizione equivalente; anafora elegante opzionale |

## Decisioni ancora da sottoporre all'autore

- Se `stru` debba essere tipizzato come verbo transitivo (significato già attestato) e con quali oggetti.
- Se `dok X-em` abbia come argomento diretto l'allievo, il contenuto insegnato o entrambi con strutture distinte.
- Come rendere la continuità della *non-azione*, senza sovrapporre `fiks` e `no mov`.
- Se confermare `omni` e `amik` (attestati ma non canonici) e definire la sintassi di `ekse` con un quantificatore.
- In quale ordine introdurre il lessico minimo dei domini rimasti scoperti.

**Nessuna ratifica o modifica alla grammatica è stata compiuta in questa revisione.** I casi del benchmark sono stati corretti solo dove il materiale già approvato consente una traduzione migliore.
