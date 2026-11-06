VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.DEFAULT_GOAL := help
.PHONY: help venv install build run run-exec clean

help:
	@echo "Доступные команды:"
	@echo "    make help       - Вывести доступные команды"
	@echo "    make venv       - Создать виртуальное окружение"
	@echo "    make install    - Установить зависимости"
	@echo "    make build      - Собрать проект в исполняемый файл"
	@echo "    make run        - Запустить проект из исходников"
	@echo "    make run-exec   - Запустить бинарный файл проекта"
	@echo "    make clean      - Очистить проект от мусора"

venv:
	@echo "Устанавливаю вируальное окружение..."
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	@echo "Вирьуальное окружение установлено!"

install: venv
	@echo "Устанавливая зависимости..."
	$(PIP) install -r requirements.txt
	@echo "Зависимости установлены!"

build: venv install
	@echo "Собираю проект..."
	$(PIP) install pyinstaller
	$(VENV)/bin/pyinstaller -Fw -n "School map" main.py
	mv ./dist/School\ map .
	rmdir dist
	chmod +x ./School\ map
	@echo "Проект собран успешно!"

run: venv install
	$(PYTHON) main.py

run-exec: build
	./School\ map

clean:
	@echo "Произвожу очистку проекта..."
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf build
	rm *.spec
	@echo "Очистка проета завершена успешно!"
