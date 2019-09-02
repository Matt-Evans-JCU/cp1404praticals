COLOUR_NAMES = {'AliceBlue': '#f0f8ff', 'green1': '#00ff00', 'green2': '#00ee00', 'green3': '#00cd00',
                'green4': '#008b00', 'GreenYellow': '#adff2f', 'orange1': '#ffa500', 'orange2': '#ee9a00', 'orange3':
                '#cd8500', 'orange4': '#8b5a00'}

colour = input("Pick a Colour: ")

while colour != '':
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour")
    colour = input("Pick a Colour: ")
