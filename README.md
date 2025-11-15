# 🎨 Evolving Art — Interactive GUI Edition

An interactive desktop application for evolving generative artwork through guided selection.

This project builds a full graphical application around a genetic-art workflow. It uses the evolutionary engine from the original project (`src/core/`), but the rendering, visualization, and all GUI components have been rewritten and expanded.

> Fork of: [https://github.com/gianluccacolangelo/evolving-art](https://github.com/gianluccacolangelo/evolving-art)
>
> ✔ Evolution logic reused
> ❌ Rendering not reused
> ❌ CLI workflow replaced with a full GUI

---

## ✨ What This Version Adds

| Component                                              | Original Project |                This Fork                |
| ------------------------------------------------------ | :--------------: | :-------------------------------------: |
| Evolution engine (genome, mutation, composition logic) |         ✅        |              **Inherited**              |
| Command-line workflow                                  |         ✅        |                    ❌                    |
| Rendering system                                       |       Basic      | **Rewritten (vector + raster engines)** |
| GUI (PySide6 desktop app)                              |         ❌        |                 **New**                 |
| Population browser & metadata                          |         ❌        |                 **New**                 |
| Live mutation controls                                 |         ❌        |                 **New**                 |
| Interactive selection-based evolution                  |       Basic      |               **Enhanced**              |
| PNG/SVG export + generation grids                      |         Basic        |                 **Enhanced**     |

---

## 🖥 Screenshots

### Menu Screen

Game-style interface with population management

![Menu Screen](plots/main_menu.png)

### Populations Browser

Manage saved populations with rich metadata

![Populations Screen](plots/populations.png)

### Create Population

Initialize new evolution experiments with custom parameters

![Create Population Screen](plots/create_population.png)

### Evolution Screen

Multi-select grid with live previews, inspector panel, and mutation controls

![Evolution Screen](plots/evolve.png)

---

## 🚀 Quick Start

```bash
conda env create -f environment.yml
conda activate evolving-art

python main.py
```

---

## 🧬 How It Works

The app uses an evolutionary pipeline:

1. Generate an initial population of visual genomes
2. Render and display results
3. User selects preferred individuals
4. Engine mutates and breeds new candidates
5. Repeat and explore emergent creative forms

Everything is saved automatically, including metadata and full lineage.

---

## 🧱 Architecture Overview

```
src/
 ├─ core/                    # Evolution engine (from original repo)
 ├─ rendering/              # New rendering pipeline (vectorizer + rasterizer)
 ├─ app/                    # PySide6 GUI (screens, widgets, theme)
 ├─ population_manager/     # Persistence, metadata, autosave, history
main.py                     # Entry point
```

---

## 🖼 Rendering System

This fork includes an entirely reworked rendering stack featuring:

* Vector-based geometry extraction
* Shapely-driven boolean geometry evaluation
* SDF-free raster backend (replacing the original pipeline)
* Options for:

  * PNG export
  * SVG export
  * Generation sheet export
* Auto bounds with override support

---

## 📦 Saving & Export

* Individuals: **PNG / SVG**
* Whole generations: **grid export**

Populations are stored under:

```
populations/<name>/history/gen_###.json
```

---

## 🔗 Attribution

* Evolution engine base → **gianluccacolangelo / evolving-art**
* Rendering, GUI, interaction logic → **This fork**

---


