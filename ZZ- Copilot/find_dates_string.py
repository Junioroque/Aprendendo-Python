"""Faça uma função que retorne datas dentro de um texto.
   A função deve receber uma string e me retornar uma lista com todas
   as datas encontradas. Caso não encontre nenhuma data, me retorne
   uma lista vazia."""
   
import re   
def find_dates_string(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    dates = re.findall(pattern, text)
    return dates

"""Faça uma função que retorne datas dentro de um texto.
   A função deve receber uma string e me retornar uma lista com todas
   as datas encontradas. As datas podem estar no formato dd/mm/aaaa 
   ou dd-mm-aaaa ou dd/mm/aa ou dd-mm-aa.
   Caso não encontre nenhuma data, me retorne uma lista vazia."""
   
def find_dates_string(text):
    pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    dates = re.findall(pattern, text)
    return dates

"""Faça uma função que retorne datas dentro de um texto.
   A função deve receber uma string e me retornar uma lista com todas
   as datas encontradas. As datas podem estar no formato dd/mm/aaaa 
   ou dd-mm-aaaa ou dd/mm/aa ou dd-mm-aa.
   Caso não encontre nenhuma data, me retorne uma lista vazia, me retorne uma lista 
   vazia e caso encontredatas repetidas, me retorne apenas uma vez."""
   
def find_dates_string(text):
    pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    dates = re.findall(pattern, text)
    unique_dates = list(set(dates))
    return unique_dates

"""Faça uma função que receba uma lista de datas em padrão diferente e retorne
   todas as datas não repetidas no padrão dd/mm/aaaa.
   As datas podem estar no formato dd/mm/aaaa ou dd-mm-aaaa ou dd/mm/aa ou dd-mm-aa."""

def convert_dates(dates):
    converted_dates = []
    for date in dates:
        if '-' in date:
            date = date.replace('-', '/')
        converted_dates.append(date)
    unique_dates = list(set(converted_dates))
    return unique_dates
