import json

with open('src/requirements.json') as f:
    d = json.load(f)

with open('__generated_requirements.tex', 'w') as f:
    f.write(r'\section{System features}' + '\n')
    for id_ in d:
        if d[id_]['category'] == '3':
            f.write(f'\\subsection{{{d[id_]["requirement"]}}}' + '\n')
            f.write('\\subsubsection{Description and Priority}' + '\n')
            f.write(f'{d[id_]["description"]}\n')
            f.write('\\subsubsection{Stimulus/Responce Sequences}' + '\n')
            f.write(f'{d[id_]["stimulus_responce"]}\n')
            f.write('\\subsubsection{Functional Requirements}' + '\n')
            f.write(f'{d[id_]["functional_requirements"]}\n')
    f.write(r'\section{External Interface Requirements}' + '\n')
    f.write('There is no specific requirements in this section\n')

    f.write(r'\section{Other Nonfunctional Requirements}' + '\n')
    f.write(r'\subsection{Perfomance Requirements}' + '\n')
    for id_ in d:
        if d[id_]['category'] == '5a':
            f.write(f'\\subsubsection{{{d[id_]["requirement"]}}}' + '\n')
            f.write(f'{d[id_]["description"]}' + '\n')
    f.write(r'\subsection{Safety Requirements}' + '\n')
    for id_ in d:
        if d[id_]['category'] == '5b':
            f.write(f'\\subsubsection{{{d[id_]["requirement"]}}}' + '\n')
            f.write(f'{d[id_]["description"]}' + '\n')
    f.write(r'\subsection{Security Requirements}' + '\n')
    for id_ in d:
        if d[id_]['category'] == '5c':
            f.write(f'\\subsubsection{{{d[id_]["requirement"]}}}' + '\n')
            f.write(f'{d[id_]["description"]}' + '\n')
    f.write(r'\subsection{Software Quality Requirements}' + '\n')
    f.write('There is no specific requirements in this section.' + '\n')
    f.write(r'\section{Other Requirements}' + '\n')
    for id_ in d:
        if d[id_]['category'] == '6':
            f.write(f'\\subsection{{{d[id_]["requirement"]}}}' + '\n')
            f.write(f'{d[id_]["description"]}' + '\n')
