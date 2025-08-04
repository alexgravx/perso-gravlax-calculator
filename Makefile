setup:
	@if ! pyenv versions --bare | grep -qx "gravlax"; then \
		pyenv virtualenv 3.12.11 gravlax; \
	else \
		echo "Virtualenv 'gravlax' already exists."; \
	fi
	pyenv local gravlax
	python3 -m pip install --upgrade build

build:
	python3 -m build

install: setup build
	pip install ./dist/*.whl

info:
	@pip list | grep "gravlax"
	@pip freeze | grep "gravlax"

push: install
	python3 -m pip install --upgrade twine
	python3 -m twine upload dist/*

clean:
	pip uninstall -y gravlax-calculator
	rm -rf ./build/ ./dist/ *.egg-info
	pip freeze | xargs pip uninstall -y