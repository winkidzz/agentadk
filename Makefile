.PHONY: venv install run clean

venv:
	python3 -m venv .venv
	. .venv/bin/activate; pip install --upgrade pip

install:
	. .venv/bin/activate; pip install -r requirements.txt

run:
	. .venv/bin/activate; adk agents chat --agent agent.yaml

clean:
	rm -rf .venv