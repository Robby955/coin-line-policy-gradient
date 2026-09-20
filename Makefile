.PHONY: test figures paper

test:
	python3 -m unittest discover -v

figures:
	python3 summarize_correction_time.py

paper: figures
	latexmk -cd -pdf -interaction=nonstopmode -halt-on-error paper/coin-line-rates.tex
