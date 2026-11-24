# -*- coding: utf-8 -*-
"""Musterdefinitionen für scan_text.py.

Jedes Muster verweist über `id` auf einen Eintrag in
references/ai_language_patterns.md. Ein Treffer ist ein KANDIDAT, kein Befund:
Ob eine Formulierung problematisch ist, entscheidet erst die Kontextprüfung
(siehe SKILL.md, Schritt 4).

Felder:
  id        Verweis auf den Bibliothekseintrag
  label     Kurzbezeichnung
  regex     Python-Regex (case-insensitive, auf Satzebene angewendet)
  weight    1 = meist legitim, nur bei Häufung prüfen
            2 = oft entbehrlich, im Kontext prüfen
            3 = fast immer inhaltsleer oder fehleranfällig
  note      Prüffrage für die Kontextprüfung
"""

PATTERNS = [
    # --- E: Einleitungen -------------------------------------------------
    dict(id="E01", label="Zeitgeist-Einstieg", weight=3,
         regex=r"\b(in der heutigen (?:\w+ )?(?:zeit|welt|gesellschaft)|in (?:einer|unserer) (?:zunehmend|immer) \w+ (?:welt|gesellschaft)|im zeitalter (?:der|des))\b",
         note="Trägt der Einstieg eine fachliche Information? Sonst mit dem eigentlichen Gegenstand beginnen."),
    dict(id="E02", label="'spielt eine zentrale Rolle'", weight=2,
         regex=r"\bspiel(?:t|en|te|ten)\s+(?:[\w-]+\s+){0,8}?(?:eine?\s+)?(?:zentrale|entscheidende|wichtige|wesentliche|bedeutende|maßgebliche|große|tragende|fundamentale|essenzielle|herausragende|immer größere|zunehmend wichtige)\s+rolle\b",
         note="Welche Rolle genau? Durch die konkrete Funktion/Wirkung ersetzen (z. B. 'begrenzt', 'bestimmt', 'koppelt')."),
    dict(id="E03", label="Thema als 'faszinierend/vielschichtig'", weight=3,
         regex=r"\b(?:ein|eine)\s+(?:faszinierendes|faszinierende|vielschichtiges|vielschichtige|spannendes|spannende|facettenreiches|facettenreiche)\s+(?:thema|feld|gebiet|forschungsfeld|phänomen)\b",
         note="Wertung ohne Information; streichen oder durch konkrete Eigenschaft ersetzen."),
    dict(id="E04", label="'gewinnt zunehmend an Bedeutung'", weight=2,
         regex=r"\b(?:hat|haben|gewinnt|gewinnen|gewann)\b[^.]{0,40}\b(?:zunehmend|stetig|immer mehr|kontinuierlich)?\s*an\s+(?:bedeutung|relevanz|aufmerksamkeit|interesse)\s*(?:gewonnen)?\b",
         note="Ist die Bedeutungszunahme belegt (Quelle, Zahl)? Sonst Belegpflicht (Klasse B) oder streichen."),
    dict(id="E05", label="Übertriebene Ankündigung ('umfassend beleuchtet')", weight=2,
         regex=r"\b(?:umfassend|detailliert|eingehend|ausführlich|tiefgehend|genauer)\s+(?:beleuchtet|beleuchten|erörtert|betrachtet|analysiert|untersucht|dargelegt)\b|\bbeleucht(?:et|en|t)\b",
         note="Hält der Text die Ankündigung ein? 'beleuchten' ist Metapher; meist 'untersuchen', 'beschreiben', 'herleiten'."),
    dict(id="E06", label="'Um X zu verstehen, ist es wichtig …'", weight=3,
         regex=r"\bum\b[^.]{1,60}\bzu verstehen,\s+(?:ist es|muss|müssen|sollte|bedarf es)",
         note="Vorbereitungsfloskel; direkt mit Y beginnen."),
    dict(id="E07", label="'Im Rahmen der vorliegenden Arbeit'", weight=1,
         regex=r"\bim rahmen (?:der vorliegenden|dieser|unserer|der hier vorgestellten) (?:arbeit|untersuchung|studie|dissertation|thesis)\b",
         note="In Einleitung/Methodik legitim. Im laufenden Text meist entbehrlich: Es ist klar, dass von dieser Arbeit die Rede ist."),

    # --- U: Übergänge ----------------------------------------------------
    dict(id="U01", label="Additiver Konnektor am Satzanfang", weight=1,
         regex=r"^(?:darüber hinaus|des weiteren|desweiteren|außerdem|zudem|ferner|weiterhin|zusätzlich|überdies|ebenso)\b",
         note="Kommt wirklich eine NEUE, gleichrangige Information? Bei Häufung (>1 pro Absatz) Relation präzisieren oder Konnektor streichen."),
    dict(id="U02", label="'In diesem Zusammenhang'", weight=2,
         regex=r"\bin diesem zusammenhang\b|\bin diesem kontext\b",
         note="Welcher Zusammenhang genau (Ursache, Bedingung, Beispiel, Gegensatz)? Relation explizit machen."),
    dict(id="U03", label="'Vor diesem Hintergrund'", weight=1,
         regex=r"\bvor diesem hintergrund\b",
         note="Legitim, wenn der Hintergrund unmittelbar vorher steht und eine Folgerung kommt. Häufung prüfen."),
    dict(id="U04", label="'Dabei/Hierbei' als Universalanschluss", weight=1,
         regex=r"^(?:dabei|hierbei|hierzu|hierfür|diesbezüglich)\b",
         note="Ist der Bezug eindeutig (wobei? wozu?)? Bei Häufung Satzbezug explizit machen."),
    dict(id="U05", label="Vorschau-Überleitung", weight=1,
         regex=r"\bim (?:folgenden|nächsten|anschließenden) (?:abschnitt|kapitel|schritt)?\s*(?:wird|werden|soll|sollen)\b|\bim folgenden\b[^.]{0,40}\b(?:näher|genauer|eingehender)\b",
         note="Am Kapitelanfang legitim. Innerhalb eines Abschnitts meist entbehrlich."),
    dict(id="U06", label="Rückblick+Vorschau ('Nachdem … betrachtet wurde')", weight=2,
         regex=r"^nachdem\b[^.]{0,80}\b(?:betrachtet|erläutert|dargestellt|beschrieben|behandelt)\s+(?:wurde|wurden|worden)",
         note="Wiederholt die Überleitung nur Bekanntes? Dann durch inhaltlichen Anschluss ersetzen."),
    dict(id="U07", label="Konklusiver Konnektor", weight=1,
         regex=r"^(?:somit|damit|folglich|demnach|daher|deshalb|infolgedessen|dementsprechend|demzufolge)\b",
         note="Folgt der Satz logisch aus dem Vorherigen? Sonst Scheinkausalität (Klasse L)."),

    # --- S: Schlussformulierungen ----------------------------------------
    dict(id="S01", label="'Zusammenfassend lässt sich sagen'", weight=2,
         regex=r"\bzusammenfassend\s+(?:lässt sich|kann|können|ist|sei|bleibt)\b[^.]{0,30}\b(?:sagen|festhalten|feststellen|konstatieren|zusammenfassen|festzuhalten|festgehalten)\b|\bzusammenfassend\b",
         note="Am Kapitelende mit echter Verdichtung legitim; am Absatzende meist redundant."),
    dict(id="S02", label="'Abschließend lässt sich feststellen'", weight=2,
         regex=r"\babschließend\s+(?:lässt sich|kann|ist|sei|bleibt)\b",
         note="Folgt eine neue Schlussfolgerung oder nur Wiederholung?"),
    dict(id="S03", label="'Insgesamt zeigt sich'", weight=2,
         regex=r"\binsgesamt\s+(?:zeigt sich|lässt sich|wird deutlich|ergibt sich|kann)\b",
         note="Welches Ergebnis genau? Konkreten Befund nennen."),
    dict(id="S04", label="'unterstreicht/verdeutlicht die Bedeutung'", weight=3,
         regex=r"\b(?:unterstreich|verdeutlich|zeig|betont|hebt)\w*\b[^.]{0,30}\b(?:bedeutung|wichtigkeit|relevanz|notwendigkeit|potenzial|potential)\b|\b(?:die|deren|dessen) (?:bedeutung|wichtigkeit|relevanz|notwendigkeit)\b[^.]{0,60}\b(?:unterstreicht|unterstreichen|verdeutlicht|verdeutlichen|belegt|hervorhebt)\b",
         note="Bedeutungsbehauptung ohne Inhalt; konkrete Konsequenz nennen oder streichen."),
    dict(id="S05", label="Ausblick-Floskel", weight=2,
         regex=r"\b(?:zukünftige|künftige|weitere)\s+(?:forschung|forschungsarbeiten|untersuchungen|arbeiten)\s+(?:sollte|sollten|könnte|könnten|müssen|muss)\b|\bbleibt (?:spannend|abzuwarten)\b",
         note="Welche konkrete offene Frage, welches Experiment? Sonst inhaltsleer."),
    dict(id="S06", label="Absatzend-Resümee ('Somit wird deutlich')", weight=2,
         regex=r"\b(?:somit|damit|hiermit|dadurch|so)\s+(?:wird|ist)\s+(?:deutlich|klar|ersichtlich|offensichtlich)\b|\bwird deutlich,\s+dass\b",
         note="Wiederholt der Satz nur den Absatz? Dann streichen."),

    # --- F: Floskeln / Metakommentare --------------------------------------
    dict(id="F01", label="'Es ist wichtig zu beachten'", weight=3,
         regex=r"\bes ist (?:besonders |dabei |hierbei |jedoch |allerdings )?(?:wichtig|entscheidend|wesentlich|essenziell|essentiell|unerlässlich|zentral|bemerkenswert|erwähnenswert|interessant)(?:,)?\s+(?:zu\s+(?:beachten|betonen|erwähnen|bedenken|berücksichtigen|verstehen|wissen|erkennen)|dass)\b",
         note="Metakommentar ersetzt Begründung. Aussage direkt formulieren; ggf. WARUM wichtig nennen."),
    dict(id="F02", label="'Es ist hervorzuheben/anzumerken'", weight=2,
         regex=r"\b(?:es ist|ist)\s+(?:\w+\s+)?(?:hervorzuheben|anzumerken|festzuhalten|zu betonen|zu erwähnen|zu beachten|zu berücksichtigen|herauszustellen),?\s+dass\b|\bin diesem zusammenhang ist\b[^.]{0,20}\b(?:anzumerken|hervorzuheben|zu erwähnen)",
         note="Gewichtung explizit begründen oder Aussage direkt formulieren."),
    dict(id="F03", label="'Von besonderer Bedeutung ist'", weight=2,
         regex=r"\bvon (?:besonderer|zentraler|entscheidender|großer|herausragender|wesentlicher|maßgeblicher) (?:bedeutung|relevanz|wichtigkeit|tragweite)\b",
         note="Wofür bedeutsam? Bezug nennen, sonst Wertung ohne Information."),
    dict(id="F04", label="'Es sei darauf hingewiesen'", weight=1,
         regex=r"\bes sei (?:darauf |an dieser stelle |hier )?(?:hingewiesen|angemerkt|bemerkt|erwähnt|betont)\b",
         note="In Mathematik/Physik etablierte Konvention (Bemerkung). Nur bei Häufung kürzen."),
    dict(id="F05", label="'Es lässt sich feststellen/erkennen'", weight=2,
         regex=r"\bes (?:lässt sich|kann|zeigt sich|ist zu erkennen|ist festzustellen)\b[^.]{0,20}\b(?:feststellen|erkennen|beobachten|sagen|konstatieren)?\s*,?\s*dass\b",
         note="Wer stellt fest, worauf stützt es sich? Oft reicht der dass-Satz als Hauptsatz."),
    dict(id="F06", label="'Ein wesentlicher Aspekt ist'", weight=2,
         regex=r"\bein(?:e|en)?\s+(?:wesentlich|entscheidend|zentral|wichtig|weiter|bedeutend|kritisch)\w*\s+(?:aspekt|faktor|punkt|gesichtspunkt|baustein|bestandteil)\b",
         note="'Aspekt'/'Faktor' als Platzhalter. Den Gegenstand selbst benennen."),
    dict(id="F07", label="'Nicht zuletzt'", weight=2,
         regex=r"\bnicht zuletzt\b|\blast but not least\b",
         note="Rhetorische Steigerung; nur bei echter Gewichtung belassen."),
    dict(id="F08", label="Evidenzbehauptung ohne Beleg", weight=2,
         regex=r"\b(?:bekanntlich|selbstverständlich|offensichtlich|offenkundig|zweifellos|zweifelsohne|unbestritten|es ist (?:allgemein )?bekannt|es ist kein geheimnis|natürlich)\b",
         note="Ist die Aussage wirklich trivial/Allgemeinwissen im Fach? Sonst Beleg nötig (Klasse B)."),

    # --- N: Überhöhte Sprache ----------------------------------------------
    dict(id="N01", label="Funktionsverbgefüge", weight=1,
         regex=r"\b(?:zur anwendung (?:kommen|kommt|kam|gelangen|gelangt|bringen)|in betracht (?:ziehen|gezogen|zieht)|eine? (?:untersuchung|analyse|prüfung|bewertung|berechnung|messung|einteilung|unterscheidung|abschätzung|optimierung|anpassung) (?:durchführen|durchgeführt|vornehmen|vorgenommen|unterziehen|unterzogen)|einer? (?:analyse|prüfung|untersuchung|bewertung) (?:unterzogen|unterziehen)|zum einsatz (?:kommen|kommt|kam|gebracht)|in erscheinung treten|unter beweis stellen|berücksichtigung finden|verwendung finden|anwendung finden|einfluss (?:haben|hat|nehmen|nimmt) auf|eine? (?:erklärung|begründung|bestätigung|entsprechung) finden|zur verfügung stellen|in abhängigkeit stehen|abhängigkeit aufweisen|eine? (?:verbesserung|erhöhung|verringerung|reduktion|reduzierung|steigerung|zunahme|abnahme) (?:erfahren|erfährt|bewirken|bewirkt|zeigen|zeigt|aufweisen|aufweist))\b",
         note="Gibt es ein einfaches Verb (anwenden, untersuchen, beeinflussen)? Fachlich etablierte Gefüge ('eine Messung durchführen') sind zulässig."),
    dict(id="N03", label="Blähverb ('erfolgt/findet statt')", weight=1,
         regex=r"\b(?:erfolgt|erfolgen|erfolgte|erfolgten|findet statt|finden statt|fand statt|vollzieht sich|vollziehen sich)\b",
         note="Versteckt Agens/Handlung. 'Die Berechnung erfolgt mit …' -> 'X wird mit … berechnet'."),
    dict(id="N08", label="Blähnomen + Blähverb ('Durchführung … erfolgt')", weight=2,
         regex=r"\b(?:durchführung|vornahme|ermittlung|bestimmung|berechnung|realisierung|umsetzung|auswertung|betrachtung)\b[^.]{0,80}?\b(?:erfolgt|erfolgen|erfolgte|findet|finden|fand|kommt|kommen|wird vorgenommen|werden vorgenommen)\b|\b(?:erfolgt|erfolgen|erfolgte)\s+(?:\w+\s+){0,2}(?:durchführung|vornahme|ermittlung|bestimmung|berechnung|realisierung|umsetzung|auswertung|betrachtung)\b",
         note="Handlung steckt im Nomen. Verb aus dem Nomen bilden: 'Die Ermittlung … erfolgt' -> '… wird ermittelt'."),
    dict(id="N04", label="Kopula-Vermeidung ('stellt … dar', 'fungiert als')", weight=1,
         regex=r"\b(?:stellt|stellen|stellte|stellten)\b[^.]{1,60}\bdar\b|\bfungier(?:t|en|te|ten) als\b|\bdien(?:t|en|te|ten) als\b|\bbildet die grundlage\b",
         note="'ist' genügt oft. 'stellt dar' ist legitim bei Darstellungen (Abb. 2 stellt … dar)."),
    dict(id="N05", label="Gehobenes Modewort", weight=2,
         regex=r"\b(?:beleuchten|eintauchen|entfalten|entfaltet|nahtlos\w*|vielschichtig\w*|facettenreich\w*|bahnbrechend\w*|revolutionär\w*|wegweisend\w*|unverzichtbar\w*|maßgeschneidert\w*|ganzheitlich\w*|paradigmenwechsel|wechselspiel|zusammenspiel|spannungsfeld|landschaft|schlüsselrolle|meilenstein\w*|eckpfeiler\w*|grundpfeiler\w*|herzstück)\b",
         note="Metaphorisch/werbend. Durch präzisen Fachbegriff oder konkrete Beschreibung ersetzen."),
    dict(id="N06", label="Intensivierer/Wertadjektiv", weight=1,
         regex=r"\b(?:entscheidend\w*|maßgeblich\w*|essenziell\w*|essentiell\w*|fundamental\w*|bemerkenswert\w*|immens\w*|enorm\w*|erheblich\w*|beträchtlich\w*|außerordentlich\w*|zentral\w*|robust\w*|umfassend\w*|innovativ\w*|effizient\w*|vielversprechend\w*)\b",
         note="Ist die Wertung belegt/quantifiziert? 'erheblich' -> Zahl; 'robust' -> wogegen?"),
    dict(id="N07", label="Anglizismus/Lehnübersetzung", weight=2,
         regex=r"\b(?:macht (?:keinen |wenig |viel )?sinn|machen (?:keinen |wenig )?sinn|in (?:19|20)\d\d\b|adressier\w*|in anderen worten|mit anderen worten|einen unterschied machen|es ist erwähnenswert|am ende des tages|nichtsdestotrotz|realisier(?:t|en)\s*,?\s*dass|signifikant\w*)",
         note="'Sinn ergeben', 'im Jahr 2020', 'behandeln/angehen'. 'signifikant' nur statistisch verwenden."),

    # --- R: Satzschablonen ------------------------------------------------------
    dict(id="R01", label="'nicht nur …, sondern auch'", weight=1,
         regex=r"\bnicht nur\b[^.]{1,120}\bsondern (?:auch|zudem|ebenfalls)\b|\bsowohl\b[^.]{1,80}\bals auch\b",
         note="Einmal legitim; Häufung (>1 pro Seite) wirkt schablonenhaft. Ist der Kontrast überhaupt gemeint?"),
    dict(id="R04", label="Kommentar-Anhang (', was … zeigt')", weight=1,
         regex=r",\s+(?:was|wodurch|womit|wobei)\b[^.]{0,80}\b(?:zeigt|verdeutlicht|unterstreicht|ermöglicht|führt|ergibt|bedeutet|widerspiegelt|widerspiegeln)\b",
         note="Hängt eine Bewertung an eine Aussage an? Eigenen Satz bilden oder streichen."),
    dict(id="R05", label="Negativer Parallelismus ('nicht X, sondern Y')", weight=1,
         regex=r"\b(?:es geht|handelt es sich)\s+(?:dabei\s+|hier\s+)?nicht\s+(?:nur\s+)?(?:um|darum)\b|\bnicht (?:bloß|einfach|lediglich|nur) (?:ein|eine|einen)\b[^.]{1,60}\bsondern\b",
         note="Wurde X überhaupt behauptet? Sonst Strohmann-Kontrast; direkt Y sagen."),
    dict(id="R07", label="Rhetorische Frage", weight=2,
         regex=r"\?\s*$",
         note="In Fachtexten selten angemessen (außer echte Forschungsfrage). Als Aussage formulieren."),

    # --- V: Vagheit / Hedging -----------------------------------------------------
    dict(id="V01", label="Hedging-Häufung", weight=2,
         regex=r"\b(?:könnte|kann|dürfte|möglicherweise|eventuell|unter umständen|gegebenenfalls|wahrscheinlich|vermutlich|potenziell|potentiell|tendenziell|gewissermaßen)\b[^.]{0,40}\b(?:möglicherweise|eventuell|unter umständen|gegebenenfalls|potenziell|potentiell|tendenziell|vermutlich|wahrscheinlich)\b",
         note="Ein Unsicherheitsmarker pro Aussage genügt. Grad der Unsicherheit am Befund festmachen."),
    dict(id="V02", label="Vage Zuschreibung ohne Quelle", weight=3,
         regex=r"\b(?:studien|untersuchungen|forschungen|experten|expertinnen|fachleute|wissenschaftler\w*|forscher\w*|die literatur|in der literatur|zahlreiche arbeiten|viele autoren)\b[^.]{0,40}\b(?:zeigen|zeigten|belegen|belegten|haben gezeigt|sind sich einig|gehen davon aus|weisen darauf hin|betonen|legen nahe|wird (?:häufig|oft|vielfach))\b",
         note="Steht ein Literaturverweis im selben Satz? Wenn nicht: Klasse B (Beleg fehlt) markieren, KEINE Quelle erfinden."),
    dict(id="V03", label="Vager Quantor", weight=1,
         regex=r"\b(?:eine vielzahl (?:von|an)|zahlreiche|diverse|verschiedenste|vielfältige|unterschiedlichste|eine reihe von|eine fülle von|vielerlei|mannigfaltige)\b",
         note="Lässt sich die Menge nennen oder eingrenzen? Bei Aufzählung die Elemente nennen."),
    dict(id="V04", label="Überverallgemeinerung", weight=1,
         regex=r"\b(?:stets|immer|grundsätzlich|ausnahmslos|in allen fällen|jederzeit|niemals|nie|in jedem fall|universell)\b",
         note="Gilt die Aussage wirklich ohne Gültigkeitsbereich? Sonst Bedingung ergänzen (Klasse F prüfen)."),
    dict(id="V05", label="Füllwort/Abtönungspartikel", weight=1,
         regex=r"\b(?:eigentlich|gewissermaßen|im grunde(?: genommen)?|letztlich|letzten endes|quasi|sozusagen|halt|eben|ja|wohl|einigermaßen|irgendwie|ziemlich|durchaus|regelrecht|schlichtweg|geradezu)\b",
         note="Trägt das Wort Bedeutung? Abtönungspartikeln gehören in die gesprochene Sprache."),
]

# Konnektoren für die Frequenzstatistik (Satzanfang)
CONNECTORS = [
    "darüber hinaus", "des weiteren", "außerdem", "zudem", "ferner", "weiterhin",
    "zusätzlich", "überdies", "jedoch", "allerdings", "dennoch", "trotzdem",
    "somit", "damit", "folglich", "daher", "deshalb", "demnach", "dabei", "hierbei",
    "insbesondere", "zunächst", "anschließend", "schließlich", "abschließend",
    "zusammenfassend", "insgesamt", "dementsprechend", "infolgedessen",
    "vor diesem hintergrund", "in diesem zusammenhang", "im gegensatz dazu",
    "andererseits", "einerseits", "gleichzeitig", "ebenso",
]

# Abkürzungen, die keinen Satz beenden
ABBREVIATIONS = [
    "z. B.", "z.B.", "d. h.", "d.h.", "u. a.", "u.a.", "bzw.", "vgl.", "ca.", "etc.",
    "Gl.", "Gln.", "Abb.", "Tab.", "Kap.", "Abschn.", "Nr.", "S.", "Bd.", "Aufl.",
    "Hrsg.", "et al.", "i. A.", "i. d. R.", "i.d.R.", "s. o.", "s. u.", "o. Ä.", "u. Ä.",
    "Fig.", "Eq.", "Ref.", "ggf.", "evtl.", "sog.", "usw.", "max.", "min.", "Dr.",
    "Prof.", "bspw.", "inkl.", "exkl.", "zzgl.", "resp.", "Def.", "Bsp.", "Anm.",
    "engl.", "lat.", "griech.", "dt.", "frz.", "bzgl.", "gem.", "lt.", "Jh.", "ff.", "f.",
    "Fa.", "Vol.", "No.", "pp.", "ed.", "eds.", "Eqs.", "Figs.", "approx.",
]
