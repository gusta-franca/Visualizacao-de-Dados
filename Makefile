PYTHON := ./.venv/bin/python
PIP := ./.venv/bin/pip

src ?= data/raw
dst ?= data/raw
out ?= data/processed
start ?= 1979
end ?= 2026

.PHONY: all columns unzip setup install freeze run

all: unzip columns run

setup:
	@python3 -m venv .venv
	@$(PIP) install --upgrade pip
	@$(PIP) install -r requirements.txt

install:
	@$(PIP) install -r requirements.txt

freeze:
	@$(PIP) freeze > requirements.txt

columns:
	@mkdir -p $(out)
	@$(PYTHON) -m scripts.run_columns --src $(src) --out $(out) --start $(start) --end $(end)

unzip:
	@mkdir -p $(dst)
	@$(PYTHON) -m scripts.run_unzip --src $(src) --dst $(dst)

run: install
	@$(PYTHON) main.py