import svgwrite
from dataclasses import dataclass

import svgwrite.text

@dataclass
class Config:
    width_total : int = 30
    height_total : int = 50
    letter_font_size : int = 7
    letter_y : int = 10
    line_thickness : float = 0.5
    bridge_thickness : int = 3
    marker_diameter : float = 2.85
    bridge_y : int = 20
    string_letters_y : int = 22
    string_letters_font_size : int = 2
    height_ratio : float = 0.5
    width_ratio : float = 0.7
    number_of_strings : int = 6
    number_of_frets : int = 6

@dataclass
class Strings:
    strings: str
    fingering: str
    chordName: str
    enharmonicChordName: str
    tones: str

class Generate_Chord_SVG:

    def __init__(self, file_name: str, strings: Strings, config:Config = None ):
        self.file_name = file_name
        self.strings = strings
        self.config = config
        if not config:
            self.config = Config()
        self.svg = svgwrite.Drawing(self.file_name, profile='tiny', size=(self.config.width_total, self.config.height_total))
        self.draw_svg()
        self.svg.save()

    def split_strings(self, strings: str) -> list[str]:
        if ' ' in strings:
            return strings.split(' ')
        else:
            return [s for s in strings]

    def calculate_dimensions(self) -> None:
        self.middle_x = self.config.width_total / 2
        self.width = self.config.width_total * self.config.width_ratio
        self.height = self.config.height_total * self.config.height_ratio
        self.width_margin = self.middle_x - 0.5 * self.width
        self.string_distance = (self.width - self.config.line_thickness) / (self.config.number_of_strings - 1)
        self.fret_distance = (self.height - self.config.line_thickness) / (self.config.number_of_frets - 1)
        self.strings_x_array = [self.width_margin + 0.5 * self.config.line_thickness + self.string_distance * i for i in range(self.config.number_of_strings)]
        self.frets_y_array=[ self.config.bridge_y + 0.5 * self.config.line_thickness + self.fret_distance * i for i in range(self.config.number_of_frets)]

    def draw_title(self) -> None:
        title = svgwrite.text.Text(
            text=self.strings.chordName,
            x=[self.config.width_total / 2],  # Set x to the center of the page
            y=[self.config.letter_y],
            text_anchor="middle",
            font_size=self.config.letter_font_size # Center the text horizontally
        )
        self.svg.add(title)

    def draw_bridge(self) -> None:
        x_start =  self.width_margin
        x_end =  self.width_margin + self.width
        y = self.config.bridge_y - 0.5 * self.config.bridge_thickness
        bridge_line = svgwrite.shapes.Line(start=(x_start, y), end=(x_end, y), stroke="black", stroke_width=self.config.bridge_thickness)
        self.svg.add(bridge_line)

    def draw_strings(self) -> None:
        y_start = self.config.bridge_y - self.config.bridge_thickness
        y_end = self.config.bridge_y + self.height
        for string_x in self.strings_x_array:
            string_line = svgwrite.shapes.Line(start=(string_x, y_start), end=(string_x, y_end), stroke="black", stroke_width=self.config.line_thickness)
            self.svg.add(string_line)

    def draw_frets(self) -> None:
        x_start = self.width_margin
        x_end = self.width_margin + self.width
        for fret_y in self.frets_y_array:
            fret_line = svgwrite.shapes.Line(start=(x_start, fret_y), end=(x_end, fret_y), stroke="black", stroke_width=self.config.line_thickness)
            self.svg.add(fret_line)
    
    def draw_markers(self) -> None:
        # '0 2 2 0 0 0' -> {5:2, 4:2}
        string_fret_dict = {int(index): int(string) for index, string in enumerate(self.split_strings(self.strings.strings)) if string not in ["0","X"]}
        for string_number in string_fret_dict.keys():
            x = self.strings_x_array[string_number]
            y = self.frets_y_array[string_fret_dict[string_number]] - 0.5 * self.fret_distance
            marker = svgwrite.shapes.Circle(center=(x,y),r=self.config.marker_diameter / 2, fill='black')
            self.svg.add(marker)
    
    def draw_string_letters(self) -> None:
        # '0 2 2 0 0 0' -> [0, 3, 4, 5]
        open_string_list = [int(index) for index, string in enumerate(self.split_strings(self.strings.strings)) if string == "0"]
        closed_string_list = [int(index) for index, string in enumerate(self.split_strings(self.strings.strings)) if string == 'x']
        for open_string in open_string_list:
            x = self.strings_x_array[open_string] - self.config.line_thickness
            y = self.config.bridge_y - self.config.bridge_thickness - 0.5
            string_letter = svgwrite.text.Text(text= 'o', x=[x], y=[y], font_size=self.config.string_letters_font_size)
            self.svg.add(string_letter)
        for closed_string in closed_string_list:
            x = self.strings_x_array[closed_string] - self.config.line_thickness
            y = self.config.bridge_y - self.config.bridge_thickness - 1
            string_letter = svgwrite.text.Text(text= 'x', x=[x], y=[y], font_size=self.config.string_letters_font_size)
            self.svg.add(string_letter)

    def draw_finger_numbers(self):
        # '0 2 2 0 0 0' -> {5:2, 4:2}
        string_fret_dict = {int(index): int(string) for index, string in enumerate(self.split_strings(self.strings.strings)) if string not in  ['0','X']}
        string_finger_dict = {int(index):int(finger) for index, finger in enumerate(self.split_strings(self.strings.fingering)) if finger != 'X'}
        for string_number in string_fret_dict.keys():
            x = self.strings_x_array[string_number] - self.config.line_thickness
            y = self.config.bridge_y + self.config.height_total * self.config.height_ratio + 2
            finger = svgwrite.text.Text(text=string_finger_dict[string_number], x=[x], y=[y], font_size=self.config.string_letters_font_size)
            self.svg.add(finger)

    def draw_svg(self):
        self.calculate_dimensions()
        self.draw_title()
        self.draw_bridge()
        self.draw_strings()
        self.draw_frets()
        self.draw_markers()
        self.draw_string_letters()
        self.draw_finger_numbers()


if __name__ == "__main__":
    config = Config()
    strings = Strings(strings='0 2 2 1 0 0', fingering='X 2 3 1 X X',chordName='E', enharmonicChordName="",tones="")
    svg = Generate_Chord_SVG(file_name='test.svg', strings=strings, config=config)  
    