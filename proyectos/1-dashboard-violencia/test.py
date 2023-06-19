import pdfplumber
import re
import requests
from io import BytesIO
import pandas as pd
from datetime import datetime, timedelta
# What happens if I make a request?

# def get_date(date):
#     day = date[:2]
#     month = date[2:4]
#     year = date[4:]

#     formatted_date = f"{day}-{month}-{year}"
#     return formatted_date

# def get_dict(date):
#     url = f"http://www.informeseguridad.cns.gob.mx/files/homicidios_{date}_v2.pdf"
#     response = requests.get(url)
#     pdf_content = response.content

#     with pdfplumber.open(BytesIO(pdf_content)) as pdf:
#         first_page = pdf.pages[0]
#         text = first_page.extract_text()

#     pattern = r'([a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+)\s+(\d+)'
#     matches = re.findall(pattern, text)
#     result = {match[0].strip(): int(match[1]) for match in matches}
#     states = [
#         'Aguascalientes',
#         'Baja California',
#         'Baja California Sur',
#         'Campeche',
#         'Coahuila',
#         'Colima',
#         'Chiapas',
#         'Chihuahua',
#         'Ciudad de México',
#         'Durango',
#         'Guanajuato',
#         'Guerrero',
#         'Hidalgo',
#         'Jalisco',
#         'México',
#         'Michoacán',
#         'Morelos',
#         'Nayarit',
#         'Nuevo León',
#         'Oaxaca',
#         'Puebla',
#         'Querétaro',
#         'Quintana Roo',
#         'San Luis Potosí',
#         'Sinaloa',
#         'Sonora',
#         'Tabasco',
#         'Tamaulipas',
#         'Tlaxcala',
#         'Veracruz',
#         'Yucatán',
#         'Zacatecas'
#     ]

#     new_dict = {key: result[key] for key in states if key in result}
#     df = pd.DataFrame.from_dict(new_dict, orient='index', columns=['Value'])
#     df.index.name = 'State'
#     df["Date"] = get_date(date)
#     return df


# def get_appended_dataframes(dates):
#     my_df = pd.concat([get_dict(date) for date in dates])
#     print(my_df)


# dates = ["10062023", "11062023", "12062023", "13062023"]
# get_appended_dataframes(dates)



def generate_days():
    date_format = "%d%m%Y"
    days = []
    current_date = datetime.strptime("03042019", date_format).date()
    today = datetime.now().date()

    while current_date <= today:
        days.append(current_date.strftime(date_format))
        current_date += timedelta(days=1)

    return days

days = generate_days()
print(len(days))
#TODO iterate over all the 1520 days and save the data to a csv file
#TODO find the best way to save it to a csv file
#TODO find best way to upload this to a database or to write it to a csv file