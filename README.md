### Hexlet tests and linter status:
[![Actions Status](https://github.com/DARIAkuch/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DARIAkuch/python-project-50/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=DARIAkuch_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=DARIAkuch_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=DARIAkuch_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=DARIAkuch_python-project-50)
***

# Difference generator (gendiff) 
***

## Required: 
[Python 3.12.0 +] - (https://www.python.org/downloads/)

[UV 0.5.11 +] - (https://astral.sh)
***

## INSTALLATION:
``` 
git clone git@github.com:DARIAkuch/python-project-50.git
```
````
cd python-project-50
````
`````
uv build
``````
````````
uv tool install dist/*.whl
````````
***

### Suppoerted file formats: 

#### - JSON (.json)
#### - YAML (.yaml, .yml)
***

## How to use: 

1. Place your files to the tests/test_data folder. 
2. Run the following command, replacing file1 and file2 with your actual file names:
````
uv run gendiff tests/test_data/(file1) tests/test_data/(file2)
````
3. Defualt output format is **stylish**, to change to output format use **-f** flag and specify the desired format, json or plain, after the flag.
***

### Examples:

- **stylish** (default)
````
uv run gendiff tests/test_data/(file1) tests/test_data/(file2)
````
``````
uv run gendiff -f stylish tests/test_data/(file1) tests/test_data/(file2)
``````
Demonstration:
[![asciicast](https://asciinema.org/a/5czy5PO4ya8KkEYXGvnNClUjm.svg)](https://asciinema.org/a/5czy5PO4ya8KkEYXGvnNClUjm)
***
- **plain** 
````
uv run gendiff -f plain tests/test_data/(file1) tests/test_data/(file2)
````
Demonstration:
[![asciicast](https://asciinema.org/a/Vr8Ll6YqOXERfDsgsw95AQD59.svg)](https://asciinema.org/a/Vr8Ll6YqOXERfDsgsw95AQD59)
***
- **json**
````
uv run gendiff -f json tests/test_data/(file1) tests/test_data/(file2)
````
Demonstration:
[![asciicast](https://asciinema.org/a/HxfJcvkuzeiQKXEn4C91IHlR1.svg)](https://asciinema.org/a/HxfJcvkuzeiQKXEn4C91IHlR1)
***