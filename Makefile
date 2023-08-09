.PHONY: cv

export FLASK_APP=run.py
export FLASK_ENV=development
export FLASK_DEBUG=1

run:
	@flask run

test:
	@pytest -p no:warnings

# Example of how you can call: make cv section=personal
cv:
	@flask cv --$(section)
