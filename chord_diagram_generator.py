import guitar_chords
from bs4 import BeautifulSoup
from bs4.element import  Tag
from typing import Union

def generate_chord_svg(
        chord_name: str, 
        return_xml: bool = False, 
        return_svg_path: bool = False, 
        return_tag: bool = False) -> Union[str,Tag,None]:
    """
    Generates an SVG image or SVG XML content of the specified guitar chord.

    Parameters:
        chord_name (str): The name of the chord.
        return_xml (bool, optional): Flag indicating whether to return SVG XML content. Defaults to False.
        return_svg_path (bool, optional): Flag indicating whether to return the path to the generated SVG image file. 
                                          Defaults to False.

    Returns:
        Union[str, Tag, None]: If return_xml is True, returns the SVG XML content. 
                               If return_svg_path is True, returns the path to the generated SVG image file.
                               If return_tag is True, returns the BeautifulSoup tag of the SVG content.
                               If none of return_xml, return_svg_path, return_tag is True, returns None.
    """
    # Instantiate GenerateGuitarChords class
    try:
        chord_gen = guitar_chords.GenerateGuitarChords()
        svg_path = chord_gen.get_guitar_chord_path(chord_name=chord_name)
    except Exception as e:
        print(e)
        return

    if not svg_path:
        return
    if return_xml:
        # Read SVG content and return SVG XML
        with open(svg_path, 'r') as f:
            svg_xml = f.read()
        return svg_xml
    elif return_svg_path:
        # Return the path to the generated SVG image
        return svg_path
    elif return_tag:
        with open(svg_path, 'r') as f:
            svg_xml = f.read()
        soup = BeautifulSoup(svg_xml, 'xml')
        return soup.svg
    else:
        return

if __name__ == "__main__":
    chord_svg = generate_chord_svg(chord_name='Em', return_xml=True)