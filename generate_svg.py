import svgwrite



class Generate_Chord_SVG:
    
    default_config = {
    # all dimensions are in px
    "total_width" : 50,
    "total_length" : 50,
    "font_size" : 9,
    #"space_between_strings" : 10,
    "line_thickness" : 1,
    "side_margins" : 4,
    "top_margins" : 10,
    "height_ratio" : 0.75,
    "num_of_frets" : 5,
    }

    def __init__(self, file_name: str, strings: str, fingering: str, chord_name: str, config : dict = None):
        # 'file_name' = 'chords/Em.svg', 'strings'= '0 2 2 0 0 0', 'fingering'= 'X 2 3 X X X', 'chord_name'= 'Em'
        self.config = config
        if not self.config:
            self.config = self.default_config
        self.file_name = file_name
        self.strings = strings
        self.fingering = fingering
        self.chord_name = chord_name
        self.svg = svgwrite.Drawing(self.file_name, profile='tiny', size=(self.config['total_width'], self.config['total_length']))
        self.draw_svg()
        self.svg.save()

    def calculate_space_between_strings(self) -> None:
        self.config["space_between_strings"] = (self.config["total_width"] - 2*self.config["side_margins"] - self.config["line_thickness"]) / 5
        
    def draw_bridge(self) -> None:
        width = self.config["total_width"] - self.config["side_margins"]
        thickness = self.config["line_thickness"] * 4
        height = self.config["top_margins"]
        bridge = svgwrite.shapes.Rect(insert=(5, 40 - height/2), size=(width, height), stroke=svgwrite.rgb(0, 0, 0, '%'), stroke_width=thickness, fill="none")
        self.svg.add(
            self.svg.line(
                start=(self.config["side_margins"], self.config["top_margins"]), 
                end=(width, self.config["top_margins"]), 
                stroke=svgwrite.rgb(0, 0, 0, '%'), 
                stroke_width=self.config["line_thickness"] * 2
                )
            )
    
    def draw_strings(self) -> None:
        string_x_array = [self.config["side_margins"] + 0.5 * self.config["line_thickness"] + self.config["space_between_strings"] * i for i in range(6)]
        length = self.config["height_ratio"] *  self.config["total_length"]
        for x in string_x_array:
            self.svg.add(
                self.svg.line(
                    start=(x, self.config["top_margins"]), 
                    end=(x, length), 
                    stroke=svgwrite.rgb(0, 0, 0, '%'), 
                    stroke_width=self.config["line_thickness"]
                    )
            )

    def calculate_space_between_frets(self) -> None:
        height = self.config["total_length"] * self.config["height_ratio"]
        self.config['space_between_frets'] = (height - 0.5 * self.config["line_thickness"] ) / self.config["num_of_frets"]

    def draw_frets(self) -> None:
        fret_y_array = [self.config["top_margins"] ]
        fret_y_arra = [self.config["top_margins"] + 0.5 * self.config["line_thickness"] + self.config["space_between_frets"] * i for i in range(self.config["num_of_frets"])]

    def draw_svg(self):
        self.calculate_space_between_strings()
        self.calculate_space_between_frets()
        self.draw_bridge()
        self.draw_strings()
        self.frets()


if __name__ == "__main__":
    svg = Generate_Chord_SVG(file_name='Em.svg',strings='0 2 2 0 0 0',fingering='X 2 3 X X X', chord_name='Em')  
    