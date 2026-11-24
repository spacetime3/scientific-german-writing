# scientific-german-writing

**A Claude skill that edits German scientific texts like a careful technical copy editor: it removes filler and AI-style boilerplate, tightens sentences, and never touches your equations, numbers, units or citations.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Language: German](https://img.shields.io/badge/texts-Deutsch-black)
![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-orange)

> 🇩🇪 Deutsche Beschreibung: [weiter unten](#deutsch)

---

## Why this exists

Theses and papers in German increasingly contain phrases like *„Es ist wichtig zu beachten, dass …“*, *„spielt eine zentrale Rolle“* or *„Zusammenfassend lässt sich sagen …“*. These phrases sound scientific but say nothing. Generic “humanizers” swap synonyms and smooth everything over. In technical texts that is dangerous, because a smoother sentence can silently change a physical statement.

This skill works differently:

| | Generic rewrite | **scientific-german-writing** |
|---|---|---|
| Filler and boilerplate | replaced by other filler | **deleted**, or replaced by the concrete function (“begrenzt”, “bestimmt”) |
| Good sentences | rewritten anyway | **left untouched** and listed under “bewusst belassen” |
| Wrong physics in the draft | silently “fixed” or polished | **flagged** `⟨F: …⟩` for the author to decide |
| Missing references | sometimes invented | **flagged** `⟨B: Quelle fehlt⟩`, never invented |
| Equations, numbers, units, citations | at risk | **verified unchanged** by an integrity checker |
| “Was this written by AI?” | guesses | **no authorship verdict**: it judges language only |

## Before / after

**Before**
> Es ist wichtig zu beachten, dass die Wahl der Wellenlänge, die Pulsdauer und die Pulsenergie entscheidende Faktoren für den Behandlungserfolg sind. […] Da die Photonenenergie mit zunehmender Wellenlänge steigt, eignen sich infrarote Laser besonders gut für die Ablation harter Gewebe.

**After**
> Der Behandlungserfolg hängt wesentlich von Wellenlänge, Pulsdauer und Pulsenergie ab. […] Da die Photonenenergie mit zunehmender Wellenlänge steigt, eignen sich infrarote Laser besonders gut für die Ablation harter Gewebe. ⟨F: Nach E = hc/λ sinkt die Photonenenergie mit der Wellenlänge. Die Begründung trägt nicht. Bitte prüfen.⟩

The filler is gone. The physics error is **not** quietly rewritten: the author decides.

**Before** (engineering)
> Im Rahmen der vorliegenden Arbeit erfolgt die Durchführung der thermischen Auslegung des Wechselrichtermoduls auf Grundlage eines Cauer-Netzwerks.

**After**
> Das Wechselrichtermodul wird auf Grundlage eines Cauer-Netzwerks thermisch ausgelegt.

More examples: [`examples/before_after_examples.md`](skills/scientific-german-writing/examples/before_after_examples.md)

## What it does

Five modes, chosen automatically from your request:

- **Analyse:** findings table by problem class (language, grammar, logic, questionable content, missing evidence)
- **Überarbeitung (revision):** revised text, change log, list of what was deliberately kept, integrity check
- **Satz für Satz:** six steps per sentence (original → weakness → explanation → proposal → content comparison → justification)
- **Absatz:** logic, information order, argumentation, transitions, terminology
- **Stilkontrolle:** rating on nine criteria (precision, naturalness, terminology, grammar, sentence structure, density, redundancy, coherence, consistency)

It is tuned for **physics, electrical and mechanical engineering, medical technology, optics/laser physics, materials science, mathematics and computer science**. It knows each field's conventions, for example that the passive is standard in methods sections, *„Es sei …“* in math, and *„wir“* in theory and computer science.

### What's inside

- **55-entry pattern library** of AI-typical and artificial phrasing (introductions, transitions, conclusions, meta-comments, nominal style, sentence templates, hedging, argument templates). Each entry has alternatives, a full example and **when the phrase is fine**.
- **Phrase library for 17 text functions:** definitions, derivations, models and approximations, limitations, references to equations and figures …
- **`scan_text.py`:** pre-scan for pattern candidates, sentence-length variation, repeated openers, connector density, nominalisations, triplets and redundancy.
- **`check_integrity.py`:** compares original and revision for formulas (LaTeX), citations (`[12]`, `(Author, 2020)`), equation/figure/table references, quantities with units, material designations (`Ti-6Al-4V`, `Er:YAG`), symbols and acronyms.
- **Sources:** German university writing centres, Ehlich, Graefen & Moll, Hyland, DIN 1338, and research on LLM vocabulary (Kobak et al. 2025, Reinhart et al. 2025 PNAS, Juzek & Ward 2025) and on detector reliability (Weber-Wulff et al. 2023, Liang et al. 2023). Established recommendations are kept separate from the skill's own rules. See [`source_references.md`](skills/scientific-german-writing/references/source_references.md).

## Tested

- **46 automated regression tests** ([`run_tests.py`](skills/scientific-german-writing/tests/run_tests.py)), including 11 deliberate corruptions (changed number, unit, citation year, equation index, sign in an `align` block, alloy name …). All 11 are detected, with no false alarms.
- **Blind test with independent instances.** With the skill: **35/35** checks passed. Without it: 9/13. Without the skill, the physics error was rewritten without asking, new content was added, and an already good text was reworded. Details: [`blind_test_results.md`](skills/scientific-german-writing/tests/blind_test_results.md)

## Install

**Claude Code (plugin):**
```
/plugin marketplace add spacetime3/scientific-german-writing
/plugin install scientific-german-writing@scientific-german-writing
```

**Claude Code (manual):** copy `skills/scientific-german-writing/` to `~/.claude/skills/`.

**Claude.ai / Claude Desktop:** download `scientific-german-writing.skill` from the [latest release](https://github.com/spacetime3/scientific-german-writing/releases/latest) and upload it under *Settings → Capabilities → Skills*.

The helper scripts need Python ≥ 3.8 and no extra packages. Without Python, the skill follows the same rules manually.

## Usage

Paste a section of your thesis and say what you want, for example:

- „Überarbeite bitte dieses Theoriekapitel, Formeln nicht anfassen.“
- „Analysiere Satz für Satz, was hier schwach ist.“
- „Mein Betreuer sagt, der Absatz ist zu nominal. Was kann ich tun?“
- „Bewerte den Stil nach Kriterien.“

Run the scripts directly:
```
python skills/scientific-german-writing/scripts/scan_text.py kapitel.md
python skills/scientific-german-writing/scripts/check_integrity.py alt.md neu.md
python skills/scientific-german-writing/tests/run_tests.py
```

## What it deliberately does not do

- It does not decide whether a text was written by a human or an AI. Studies show detectors are unreliable and biased against non-native writers.
- It does not help disguise AI use or evade detectors. The goal is better language, not hiding where a text came from.
- It does not invent references, numbers or new technical claims.

## Contributing

Pattern suggestions, field-specific conventions (chemistry? biology?) and real-world false positives are very welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

If this skill saved your thesis chapter, a ⭐ helps others find it.

---

<a id="deutsch"></a>
## 🇩🇪 Deutsch

**scientific-german-writing** ist eine Claude-Skill für die sprachliche Überarbeitung deutscher wissenschaftlicher Texte, also Bachelor-, Master- und Doktorarbeiten, Fachartikel und Forschungsberichte. Der Schwerpunkt liegt auf Natur- und Ingenieurwissenschaften.

Die Skill arbeitet wie ein sorgfältiges Fachlektorat:
- Floskeln, mechanische Übergänge, Nominalketten und Absatz-Resümees werden **im Kontext** geprüft. Es gibt keine starre Verbotsliste: „Darüber hinaus“ bleibt stehen, wenn tatsächlich etwas hinzukommt.
- Gute Sätze bleiben unverändert. Ein guter Text wird als gut zurückgegeben.
- Fachlich fragwürdige Aussagen werden mit `⟨F: …⟩` markiert, fehlende Belege mit `⟨B: …⟩`. Nichts wird eigenmächtig „korrigiert“, und es werden keine Quellen erfunden.
- Gleichungen, Variablen, Einheiten, Zahlen, Literatur- und Abbildungsverweise werden nach jeder Überarbeitung automatisch auf Unverändertheit geprüft.
- Es gibt kein Urteil darüber, ob ein Text „von einer KI“ stammt, sondern nur nachvollziehbare sprachliche Befunde.

**Installation:** siehe [Install](#install) oben. **Kurzanleitung auf Deutsch:** [`skills/scientific-german-writing/README.md`](skills/scientific-german-writing/README.md).

## License

[MIT](LICENSE)
