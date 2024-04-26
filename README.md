# Guitar Chord Generator

The Guitar Chord Generator is a Python package designed to generate SVG images of guitar chords based on chord names. It also provides an API to fetch chord data from the Uberchord API.

## Installation

You can install the Guitar Chord Generator package using pip:

```bash
pip install git+https://github.com/michavardy/ChordDiagramGenerator.git
```

## Configuration

No additional configuration is required to use the Guitar Chord Generator package. However, make sure you have the necessary dependencies installed.

## Usage

To generate an SVG image of a guitar chord, you can use the GenerateGuitarChords class:

```python
from chord_diagram_generator import generate_chord_svg
generate_chord_svg(chord_name="Em")
generate_chord_svg(chord_name="Em", return_xml=True)
generate_chord_svg(chord_name="Em", return_svg_path=True)
```
