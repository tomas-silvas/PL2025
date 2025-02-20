#Lista ordenada alfabeticamente dos compositores musicais;  array ordenado
#Distribuição das obras por período: quantas obras catalogadas em cada período;    dicionário ordenado (periodo -> num_obras)
#Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período.    (periodo -> lista_ordenada_titulos)
import re

def parse_csv(file_path):

    entries = []
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Remove todas as ocorrências dos caracteres " e \n dentro das aspas duplas
        content = re.sub(r'".*?"', lambda x: x.group(0).replace('\n', ' '), content, flags=re.DOTALL)
        lines = content.split('\n')
        for line in lines[1:]:  # Ignora o cabeçalho
            parts = line.split(';')
            if len(parts) >= 7:  # Verifica se há pelo menos 7 partes após a divisão
                nome = parts[0]
                periodo = parts[3]
                compositor = parts[4]
                entries.append((nome, periodo, compositor))
            else:
                print("erro na leitura:", line)
    return entries

def create_catalogs(entries):
    compositores_list = []
    periodos_dict = {}
    periodos_titles_dict = {}
    for entry in entries:
        nome, periodo, compositor = entry
        if compositor not in compositores_list:
            compositores_list.append(compositor)
        if periodo in periodos_dict:
            periodos_dict[periodo] += 1
            periodos_titles_dict[periodo].append(nome)
        else:
            periodos_dict[periodo] = 1
            periodos_titles_dict[periodo] = [nome]
    compositores_list.sort()
    periodos_dict = dict(sorted(periodos_dict.items()))
    periodos_titles_dict = dict(sorted(periodos_titles_dict.items()))
    return compositores_list, periodos_dict, periodos_titles_dict

file_path = 'obras.csv'
entries = parse_csv(file_path)
compositores_list, periodos_dict, periodos_titles_dict = create_catalogs(entries)