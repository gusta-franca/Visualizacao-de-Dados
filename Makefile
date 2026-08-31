src ?= data/raw
dst ?= data/raw
out ?= data/processed
start ?= 1979
end ?= 2026


.PHONY: all columns unzip run

all: unzip columns run

columns:
	@mkdir -p $(out)
	@python3 -m scripts.run_columns --src $(src) --out $(out) --start $(start) --end $(end)

run:
	@python3 main.py

unzip:
	@mkdir -p $(dst)
	@python3 -m scripts.run_unzip --src $(src) --dst $(dst)

