setup:
	@if ! pyenv versions --bare | grep -qx "gravlax"; then \
		pyenv virtualenv 3.12.11 gravlax; \
	else \
		echo "Virtualenv 'gravlax' already exists."; \
	fi
	pyenv local gravlax

build:
	python3 setup.py bdist_wheel

install: setup build
	pip install ./dist/*.whl

info: install
	@pip list | grep "gravlax"
	@pip freeze | grep "gravlax"

clean:
	pip uninstall -y gravlax-calculator
	rm -rf ./build/ ./dist/ *.egg-info