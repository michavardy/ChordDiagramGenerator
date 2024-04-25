# Guitar Chord Generator

The Guitar Chord Generator is a Python package designed to generate SVG images of guitar chords based on chord names. It also provides an API to fetch chord data from the Uberchord API.

## Installation

You can install the Guitar Chord Generator package using pip:

```bash
pip install git+https://github.com/michavardy/GuitarChordGenerator.git
```

## Configuration

No additional configuration is required to use the Guitar Chord Generator package. However, make sure you have the necessary dependencies installed.

## Usage

To generate an SVG image of a guitar chord, you can use the GenerateGuitarChords class:

```python
from ChordDiagramGenerator import generate_chord_svg

chord_svg = generate_chord_svg(chord_name='Em', return_xml=True)
chord_svg = generate_chord_svg(chord_name='Em', return_svg_path=True)
```


## Poetry

```conf
[tool.poetry]
name = "ChordDiagramGenerator"
version = "0.1.0"
description = "A package for generating chord diagrams"
authors = ["Micha Vardy michavardy@gmail.com"]

[tool.poetry.dependencies]
python = "^3.9"
svgwrite = "^1.4.1"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.scripts]
generate_chord_svg = "main:generate_chord_svg"

[tool.setuptools_scm]
```
