import pdfplumber
import re
import requests
from io import BytesIO
# What happens if I make a request?


def get_dict(date):
    url = f"http://www.informeseguridad.cns.gob.mx/files/homicidios_{date}_v2.pdf"
    response = requests.get(url)
    pdf_content = response.content

    with pdfplumber.open(BytesIO(pdf_content)) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()

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

dates = ["10062023", "11062023", "12062023", "13062023"]

for date in dates:
    get_dict(date)