import json
import colours as c


def load_json(file_name):
    # Open a json file called file_name
    with open(file_name) as file:
        # Load the json file into a dictionary
        return json.load(file)


def convert(value):
    if 1000 <= value < 1000000:
        # Kilo
        value = str(value / 1000) + " K"

    elif 1000000 <= value < 1000000000:
        # Mega
        value = str(value / 1000000) + " M"

    elif value >= 1000000000:
        # Giga
        value = str(value / 1000000000) + " G"

    return value


def input_colours(bands):
    colours = []
    while len(colours) < 5:
        # Calculate a suffix for the number i.e. 2nd or 3rd
        suffixes = ["", "st", "nd", "rd", "th", "th"]
        suffix = suffixes[len(colours) + 1]

        # Ask the user to input the colour of the resistor band
        colour = input(f"{c.cyan}What is the colour of the "
                       f"{c.blue}{len(colours) + 1}{suffix}{c.end} "
                       f"{c.cyan}band? {c.end}").lower()

        if colour in bands:
            # Only add the colour if it is valid
            colours.append(colour)

        else:
            # Otherwise, print an error message
            print(f"{c.red}Error: This colour does not exist.{c.end}")

    return colours


def calc_resistor(colours, bands):
    # Set default values
    bands_value = ""
    multiplier = 1
    tolerance = 0

    for i, colour in enumerate(colours):
        # Get the band value from
        if i < 3:
            bands_value += str(bands[colour]["band"])

        # Get the multiplier
        elif i == 3:
            multiplier = bands[colour]["multiplier"]

        # Get the tolerance
        elif i == 4:
            tolerance = bands[colour]["tolerance"]

    # Calculate the resistor value
    resistor_value = int(bands_value) * multiplier
    return resistor_value, tolerance


def main(file_name):
    # Print the welcome message
    print(f"{c.magenta}Resistor Calculator v0.1.0{c.end}")

    # Load the band information from the json file
    bands = load_json(file_name)

    # Get the colours of the resistor's bands from the user
    colours = input_colours(bands)

    # Calculate the value and tolerance of the resistor
    resistor_value, tolerance = calc_resistor(colours, bands)

    # Convert the value to a readable format
    converted_value = convert(resistor_value)

    # Collect and create the final value
    final_value = f"{converted_value}Ω +/-{tolerance}%"

    # Print the original colours entered and final value
    print(f"\n{c.blue}You have entered: {c.cyan}{', '.join(colours)}{c.end}"
          f"\n{c.blue}Your resistor is: {c.cyan}{final_value}{c.end}")


if __name__ == "__main__":
    main("bands.json")
