.PHONY: all check pdf book methods clean
export PYTHONDONTWRITEBYTECODE := 1
all: pdf

check:
	python3 scripts/check_all.py

pdf: check
	latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=build build/book.tex
	python3 scripts/verify_book.py --tex build/book.tex --log build/book.log
	latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=build build/methods.tex
	python3 scripts/verify_book.py --tex build/methods.tex --log build/methods.log
	python3 scripts/verify_links.py
	python3 scripts/clean.py

book: check
	latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=build build/book.tex
	python3 scripts/verify_book.py --tex build/book.tex --log build/book.log
	python3 scripts/clean.py

methods: check
	latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=build build/methods.tex
	python3 scripts/verify_book.py --tex build/methods.tex --log build/methods.log
	python3 scripts/clean.py

clean:
	python3 scripts/clean.py
