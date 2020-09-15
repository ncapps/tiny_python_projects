.PHONY: test

WORDS = "../inputs/words.txt"

test:
	pytest -xv test.py unit.py

words:
	[[ ! -f $(WORDS) ]] && (cd ../inputs && unzip words.txt.zip)
