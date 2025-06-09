# GEN DAQ API - Python Driver
> Setup, control and acquire data from the Genesis Highspeed systems via python.

[![Build Status](https://dev.azure.com/GenesisHighSpeed/GHS%20ESW/_apis/build/status/hbkworld.ghs-gendaqapi-python?branchName=main)](https://dev.azure.com/GenesisHighSpeed/GHS%20ESW/_build/latest?definitionId=117&branchName=main)

The GEN DAQ API can be used to control the HBM GEN Series tethered mainframes.

## Requirements

Python 3.10+

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [GEN DAQ API - Python Driver](https://pypi.org/project/ghs-gendaqapi-py/) package.

```bash
pip install ghs-gendaqapi-py
```

## Usage

Refer [examples](./examples) for detailed use cases. 
Refer [documentation](https://github.com/hbkworld/ghs-gendaqapi-python/blob/main/docs/html/index.html) for detailed API documentation

```python
from ghsapi import ghsapi

# create Gen Daq API's object
gen = ghsapi.GHS()

# connect to mainframe
gen.ghs_connect(IP_ADDRESS, PORT_NO)

# disconnect from mainframe
gen.ghs_disconnect()
```

## Development environment setup

Below are the steps to follow to setup devlopement enviroment for system integration and testing.

### Requirements

- `Python 3.10+`
- `Anaconda/Miniconda`

### Clone repo

```bash
git clone https://github.com/hbkworld/ghs-gendaqapi-python.git
```

### Virtual Environment 

**Option 1 :  Create Environment Using Conda**

Run the following command to create environment from the specification file

```bash
conda create --name <venv_name> --file spec-file.txt
conda activate <venv_name>
```

**Option 2 :  Create Environment Using Python**

Navigate to the root of the repository to create virtual environment

```bash
py -m venv <venv_name>
<venv_name>\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Run example files

Edit files in [examples](./examples) to enter mainframe IP and Port number

```bash
python examples\FILENAME
```

## Testing

Edit files in [functionaltest](./functionaltest) to enter mainframe IP and Port number

### Unit test

```bash
python unittest\FILENAME
```

### Functional test

```bash
python functionaltest\FILENAME
```
