.PHONY: venv install run clean

venv:
	python3 -m venv .venv

install: venv
	. .venv/bin/activate; pip install --upgrade pip
	. .venv/bin/activate; pip install -r requirements.txt

run:
	. .venv/bin/activate; adk run my_agent

clean:
	rm -rf .venv