# ICH-Synth Benchmark Generation Pipeline

This repository contains the procedural generation pipeline for the **ICH-Synth Benchmark**, a multi-view dataset designed for evaluating 4D reconstruction of Intangible Cultural Heritage (ICH) performances.

## Benchmark Overview

The **ICH-Synth Benchmark** consists of 150 sequences across three categories:

- **Paper Cutting (剪纸):** 60 sequences focusing on planar and thin-surface deformation.
- **Calligraphy (书法):** 50 sequences capturing complex 3D motion of brush strokes and ink deposition.
- **Shadow Puppetry (皮影戏):** 40 sequences involving articulated motion of jointed traditional puppets.

### Dataset Generation

We provide a procedural generation pipeline to allow for full reproducibility and the creation of custom benchmark variants.

#### Requirements
- Python 3.x
- Pillow (PIL)
- NumPy

#### Usage
To generate the full benchmark (150 sequences), run:
```bash
python3 src/synthetic/generate_benchmark.py
```

The output will be stored in `data/ICH-Synth/`, organized by category and sequence ID. Each frame contains 8 synchronized multi-view images and ground-truth camera matrices.
