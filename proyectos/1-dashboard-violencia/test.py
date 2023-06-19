import pdfplumber
import re
import requests
from io import BytesIO
# What happens if I make a request?

url = "http://www.informeseguridad.cns.gob.mx/files/homicidios_13062023_v2.pdf"

response = requests.get(url)

print(response.status_code)
pdf_content = response.content

with pdfplumber.open(BytesIO(pdf_content)) as pdf:
    # Perform operations on the PDF document
    # Access pages, extract text, extract tables, etc.
    for page in pdf.pages:
    # Loop through each page in the PDF
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        print(len(text))


    # Process each line (excluding the header line and the last line)
pattern = r'([a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+)\s+(\d+)'

matches = re.findall(pattern, text)
result = {match[0].strip(): int(match[1]) for match in matches}

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