# Task 6 report - A4 black-and-white weekly set review

## Deliverables

- Editable source: `content/batch-2/print/weekly-set-review-source.md`
- Reproducible generator: `content/batch-2/print/generate_weekly_set_review.py`
- Printable PDF: `content/batch-2/print/mya-weekly-set-review.pdf`

## Content and layout

The two-page A4 handout covers only set concepts, membership/non-membership, and representation. Page 1 contains a learning card, one core conclusion, one `∈/⊆` misconception reminder, and four self-authored questions with lined working space. Page 2 withholds three-level hints and answers until the learner turns the page. Hierarchy is conveyed with type size, weight, rules, borders, and dotted writing lines for black-and-white printing; no set operation is introduced.

## Generation and verification

- Generated with ReportLab using an embedded CJK Unicode font. The generator now searches a fixed macOS/Linux candidate list (Arial Unicode, Noto Sans CJK, WenQuanYi, Droid fallback, and AR PL UKai), verifies Chinese plus `∈`、`∉`、`⊆`、`≤` and `≥`, prints the selected path, and fails with installation guidance if none is usable. This verification selected `/System/Library/Fonts/Supplemental/Arial Unicode.ttf`.
- Replaced all generated en/em dashes with ASCII hyphens, including `10-15` and `元素-集合`.
- Rendered both final pages at 2× with PyMuPDF to `/tmp/mya-weekly-render/page-1.png` and `/tmp/mya-weekly-render/page-2.png`, then visually inspected them. The first draft had the working-area label crowding compact prompts; the generator was adjusted and the final render has no clipping, overlap, or broken glyphs.
- Structural checks with pypdf/pdfplumber confirmed: exactly 2 pages; each is `595.28 × 841.89 pt` (A4); no encryption; title `Mya 周中集合复盘单`; author `Secondary School Content Team`; embedded font present; expected Chinese and mathematical text extracts without replacement glyphs.
- `pdfinfo` and `pdftoppm` are not installed in this environment, so their required checks/rendering were not executable. The structural and visual fallback above was used instead.
