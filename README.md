# dotsplitter

Sentence splitter by dot

- [x] Não separar por abreviações padrões
- [x] Separação por outras pontuações
- [ ] Não separar por abreviações de nome

# Dependências

- Python 3.7
- Spacy

# Uso

```
usage: split.py [-h] [--abbrev-path ABBREV_PATH] [-i INPUT] [-o OUTPUT] lang

positional arguments:
  lang                  Language of the text. See spaCy language modules.

optional arguments:
  -h, --help            show this help message and exit
  --abbrev-path ABBREV_PATH
                        File with abbreviation list
  -i INPUT, --input INPUT
                        Path of the text file for input
  -o OUTPUT, --output OUTPUT
                        Path of the file for output
```

# Exemplo

```sh
    $  python split.py pt -i file.txt -o file_out.txt --abbrev-path data/abreviaturas.csv
```