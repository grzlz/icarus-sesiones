import pdfplumber
import re

with pdfplumber.open("C:/Users/grzlz/Desktop/homicidios_14062023_v2.pdf") as pdf:
    # Initialize an empty list to hold all lines

    # Loop through each page in the PDF
    first_page = pdf.pages[0]
    text = first_page.extract_text()
    print(len(text))

    # Initialize an empty dictionary
    dictionary = {}

    # Process each line (excluding the header line and the last line)
pattern = r'([a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+)\s+(\d+)'

matches = re.findall(pattern, text)
result = {match[0].strip(): int(match[1]) for match in matches}

# print(result)

    # Print the resulting dictionary



states = [
    'Aguascalientes',
    'Baja California',
    'Baja California Sur',
    'Campeche',
    'Coahuila',
    'Colima',
    'Chiapas',
    'Chihuahua',
    'Ciudad de México',
    'Durango',
    'Guanajuato',
    'Guerrero',
    'Hidalgo',
    'Jalisco',
    'México',
    'Michoacán',
    'Morelos',
    'Nayarit',
    'Nuevo León',
    'Oaxaca',
    'Puebla',
    'Querétaro',
    'Quintana Roo',
    'San Luis Potosí',
    'Sinaloa',
    'Sonora',
    'Tabasco',
    'Tamaulipas',
    'Tlaxcala',
    'Veracruz',
    'Yucatán',
    'Zacatecas'
]

new_dict = {key: result[key] for key in states if key in result}

print(new_dict)