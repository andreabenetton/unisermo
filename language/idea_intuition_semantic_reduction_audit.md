# Audit di riduzione semantica: «idea» e «intuizione»

**Stato:** analisi, non ratifica. 14 novembre 2026. In risposta alla richiesta
di minimizzare le radici nuove usando le famiglie esistenti, i casi e la
derivazione prima di approvare qualunque candidato.

**Documenti confrontati:** `language/derivation.md`,
`language/verb_specification.md`, `language/copula.md`,
`language/noun_case_system.md`, `language/word_order.md`,
`formalization/data/valency_frames.json`,
`formalization/data/lexicon_index.json`,
`language/idea_intuition_semantic_map.md`.

## 1. Le tre operazioni che NON vanno confuse

1. **Famiglia verbale di fase** `ad-` (entrare nello stato/iniziare
   l'evento), `in-` (continuare), `de-` (cessare), `re-`
   (riprendere). Esempi canonici `adsap` acquisire conoscenza,
   `adkap` cominciare a comprendere, `adpens` cominciare a pensare.
   Nessuno di essi implica *come* la comprensione sia stata raggiunta.
2. **Casi nominali** `-ad` destinazione/destinatario, `-de`
   origine/fonte, `-in` luogo o dominio concreto/astratto. Questi
   configurano **ruoli di argomenti** soltanto con un predicato che li
   licenzia, e non derivano da soli nuovi eventi cognitivi. Distinguere
   `ad-` da `-ad`.
3. **Derivazioni nominali** `-it` risultato di un verbo,
   `-kon` concetto della radice, `-itat` proprietà astratta,
   `-or` agente, `-ia` luogo/dominio e `-al` relazione
   aggettivale. Non trasformare `pensit` in "proposta" per semplice
   abitudine italiana: in assenza di uno speciale significato ratificato
   significa soltanto il pensato/risultato del pensare.
   `sapkon` è il concetto di sapere, non una previsione.

Un'estensione **sensata ma non ancora ratificata** per alcune famiglie è
un complemento `SOURCE-de` che indichi la fonte informativa o
`DEST-ad` che indichi il destinatario di un atto comunicativo. È
necessario definire la valenza di quel verbo; non si può applicare
automaticamente `-de` o `-ad` a `sap`, `kap`, `dik`.

## 2. Analisi delle otto radici candidate

| Candidato | Nucleo semantico richiesto | Copertura già disponibile | Resto NON coperto | Decisione |
| --- | --- | --- | --- | --- |
| `propoz` | Presentare un contenuto a qualcuno affinché lo valuti o lo accolga | `dik` esprimere/dire, `-ad` destinatario **se la valenza è ratificata**, `int` finalità intenzionale | Lo specifico atto di **sottoporre a valutazione** non segue da dire + destinatario | **Sospendere**: prima decidere se serve un predicato autonomo o un costrutto di scopo `dik ... fin ...` con valenza verificata |
| `program` | Struttura di azioni ordinate con fini e vincoli | `int` intenzione, `-kon` concetto, `pretem/postem` ordine degli intervalli di eventi **delimitati**, `fak` fare | Rappresentazione strutturata di **azioni pianificate ma non ancora realizzate** e loro dipendenze; `pretem` non designa un piano | **Sospendere**: il bisogno può essere nominale/relazionale anziché una radice verbale |
| `solv` | Trovare una risposta *valida* che soddisfa vincoli di un problema | `adkap` ingresso nella comprensione, `adsap` ingresso nella conoscenza, `fakit` esito di fare | Correttezza della **risposta al problema**: capire X non è dimostrare/soddisfare i vincoli | **Candidato residuale forte**, una volta definita la nozione di problema/criterio di correttezza |
| `imagin` | Costruire o mantenere una rappresentazione *percettiva* interna non percepita direttamente | `pens` elaborazione mentale, `kon` concetto | Contenuto **visivo/sensoriale figurativo** vs concetto astratto; pensare X non implica visualizzarlo | **Candidato residuale forte**, ma specificare se visivo soltanto o ogni modalità sensoriale |
| `supoz` | Assumere P provvisoriamente come premessa di un ragionamento, senza affermare P | `kred` credenza, `pos P` possibilità, `se P alor Q` condizionale | L'**atto di adottare** P come premessa senza crederlo vero; `se` permette già inferenza condizionata ma non marca l'impegno del soggetto | **Candidato residuale condizionale**: prima provare la costruzione `se P alor Q`; se serve l'atto metacognitivo, radice specifica |
| `previs` | Formulare una previsione su futuro evento, usando elementi giustificativi | `kred` credenza, `lik` probabilità, futuro verbale `-f`, `nam` giustificazione evidenziale | Il fatto che l'**agente produca una previsione** come atto, anziché credere già un futuro P | **Per ora eliminabile** da inventario minimo, a meno che il dominio richieda un verbo tecnico di forecasting/emettere previsioni |
| `presag` | Anticipare un evento senza ragioni articolate | `kred` credenza, `lik` grado di probabilità, futuro `-f` | La **sensazione non argomentata** / connotazione emotiva; l'assenza di evidenze non è deducibile dalla loro mancata menzione | **Sospendere**: verificare se l'assenza di ragionamento sia davvero una categoria lessicale, invece di un modificatore di modalità |
| `intui` | Arrivare a riconoscere una relazione senza ragionamento cosciente passo-passo | `adkap` inizio comprensione, `adsap` acquisire sapere, `imedi` immediatezza **solo in specifiche relazioni temporali ratificate** | Il **modo di acquisizione non discorsivo** non è codificato da `ad-`; `imedi` non è un generico avverbio | **Eliminare come radice generica**: eventualmente definire un modificatore di maniera (non un secondo verbo della conoscenza) |

## 3. Test di contrasto semantico: non collassare

Le proposizioni seguenti forniscono **controesempi di equivalenza**;
non sono nuove formulazioni Unisermo verificate dal parser.

- Posso `adsap` dopo ore di studio: dunque acquisire conoscenza
  NON implica intuizione immediata.
- Posso `adkap` una dimostrazione errata nel senso di capire
  ciò che l'autore intendeva: non ho necessariamente risolto il problema.
- Posso avere `kred` che domani piova senza formulare una previsione
  destinata ad altri: credenza su P-futuro NON implica atto di previsione.
- Posso usare `se P alor Q` come ragionamento ipotetico senza credere
  P vero: questa funzione di *supponiamo che P* è già composizionale,
  se non interessa affermare l'atto personale di assumere una premessa.
- Posso `pens` a una ruota senza visualizzarla: `pens` non comporta
  raffigurazione percettiva.
- Posso `dik` una preferenza a qualcuno senza chiedergli di valutarla
  formalmente: comunicare non equivale a proporre.
- Un'intuizione immediata può essere **falsa** (congettura non argomentata),
  oppure riguardare una comprensione corretta; imporre una singola radice
  che significhi entrambe reintroduce l'ambiguità proibita.
- `-in` specifica dominio, non «in mente» con automatica implicazione
  di immagine percettiva; `-de` origine, non «senza evidenze»;
  `-ad` destinatario, non l'atto di sottoporre a valutazione.

## 4. Inventario minimo risultante

**Già espresso**, senza radici nuove:
`kon` (concetto), `kred` (credenza), `int` (intenzione),
`pens` (pensare), `kap/adkap` (capire/iniziare a capire),
`sap/adsap` (sapere/acquisire sapere), `pos` (possibilità),
`lik` (probabilità), `se ... alor ...` (ipotesi condizionale),
con collocazioni temporali ratificate nei loro ambiti specifici.

**Due differenze da testare prioritariamente** con radici nuove
specifiche: (1) soluzione **valida** di problema → candidato `solv`;
(2) raffigurazione percettiva mentale → candidato `imagin`.
Né la grafia né la valenza sono ratificate.

**Una possibile terza differenza**: assumere deliberatamente P come premessa
senza affermarne la verità → candidato `supoz`, ma solo se la
costruzione condizionale già esistente non è sufficiente per lo scopo.

**Non ratificare per ora** `propoz`, `program`, `previs`,
`presag` o `intui`: prima cercare costruzioni di scopo,
struttura di eventi, assegnazione di dominio, argomenti dichiarativi e
modificatori di modalità. Qualsiasi decisione deve restare falsificabile
con coppie minime italiane che distinguano i significati.

## 5. Implicazioni per il parser

- Parser che accetta `adkap` non prova che significhi "intuire".
- Parser che riconosce `-ad/-de/-in` morfologicamente NON conferma
  l'attaccamento a qualsiasi verbo: la valenza va ratificata per testa.
- `-it` nomina un esito, ma non promette il tipo dell'esito senza
  lessicalizzazione.
- `-kon` è concetto-di-X e non un contenitore per qualunque idea.
- Il linguaggio informale del report non è una licenza di frase:
  tutte le nuove frasi vanno provate contro grammatica e parser separatamente.

**Nessuna regola nuova né radice viene ratificata da questa analisi.**
