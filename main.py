import guitar_chords

def generate_chord_svg(chord_name: str, return_xml: bool = False, return_svg_path: bool = False) -> str:
    """
    Generates an SVG image or SVG XML content of the specified guitar chord.

    Parameters:
        chord_name (str): The name of the chord.
        return_xml (bool, optional): Flag indicating whether to return SVG XML content. Defaults to False.
        return_svg_path (bool, optional): Flag indicating whether to return the path to the generated SVG image file. 
                                          Defaults to False.

    Returns:
        str: If return_xml is True, returns the SVG XML content. 
             If return_svg_path is True, returns the path to the generated SVG image file.
             If neither return_xml nor return_svg_path is True, returns None.
    """
    # Instantiate GenerateGuitarChords class
    chord_gen = guitar_chords.GenerateGuitarChords()

    # Get SVG image path for the chord
    svg_path = chord_gen.get_guitar_chord_path(chord_name=chord_name)

    if return_xml:
        # Read SVG content and return SVG XML
        with open(svg_path, 'r') as f:
            svg_xml = f.read()
        return svg_xml
    elif return_svg_path:
        # Return the path to the generated SVG image
        return svg_path
    else:
        return

if __name__ == "__main__":
    chord_svg = generate_chord_svg(chord_name='Em', return_xml=True)