# Slide deck — `slides.md`

The slide deck for the YZV 322E tool presentation, written in [Marp](https://marp.app/) markdown.

10 slides, 16:9, exported to PDF for submission.

## Render to PDF

You have three options. **`npx` is the fastest** since `node` is already on this machine.

### Option 1 — `npx` (recommended, no install)

```bash
cd slides/
npx --yes @marp-team/marp-cli@latest slides.md --pdf --allow-local-files
```

Output: `slides.pdf` in the same directory. First run downloads Marp CLI (~30 s).

### Option 2 — Install Marp CLI globally

```bash
npm install -g @marp-team/marp-cli
marp slides/slides.md --pdf --allow-local-files
```

### Option 3 — VS Code Marp extension

Install the *Marp for VS Code* extension, open `slides.md`, then *Marp: Export slide deck* → PDF.

## Tweak the deck

- Edit `slides.md` directly. Each slide is separated by `---` on its own line.
- The YAML front matter at the top controls theme, colors, header/footer, and per-section CSS overrides.
- Per-slide directives like `<!-- _class: cover -->` apply only to the slide that follows.

## Final submission file

After rendering, the file you upload to the platform is `slides/slides.pdf`. The assignment requires PDF or PPTX — Marp produces PDF directly.
