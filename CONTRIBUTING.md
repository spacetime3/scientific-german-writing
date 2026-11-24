# Contributing / Mitwirken

Contributions in English or German are welcome. Beiträge auf Deutsch oder Englisch sind willkommen.

## Good first contributions
- **New pattern** for `references/ai_language_patterns.md`: include the phrase, a real-looking example sentence (no copyrighted text), why it is weak, at least two alternatives, and **when the phrase is legitimate**. The last point is mandatory, because the skill never works as a blacklist.
- **False positive** from `scan_text.py` on a real text: open an issue with the sentence and the pattern ID.
- **Field conventions** for disciplines not yet covered (chemistry, biology, geosciences …) in `references/technical_writing.md`.
- **Integrity gaps:** an element that `check_integrity.py` should protect but doesn't. Please add a negative test to `tests/run_tests.py`.

## Rules
1. Run `python skills/scientific-german-writing/tests/run_tests.py` before opening a PR. All tests must pass.
2. Keep established recommendations (with source) separate from new heuristics (mark them as own rules `[R]`).
3. Never add invented sources. Every source needs title, author/institution, year and a link.
4. The skill must not gain features for disguising AI authorship or evading detectors.
