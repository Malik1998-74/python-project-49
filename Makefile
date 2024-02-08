brain-games:
	poetry run brain-games
# запуск логики приветствия

brain-even:
	poetry run brain-even
# запуск логики нечетность

brain-calc:
	poetry run brain-calc
# запуск логики математические выражения

brain-gcd:
	poetry run brain-gcd
# запуск логики НОД

brain-progression:
	poetry run brain-progression
# запуск логика арифмитическая прогрессия 

brain-prime:
	poetry run brain-prime
# запуск логики простое число
	
build:
	poetry build
# сборка пакета

install:
	poetry install
# инициализировать виртуальное окружение

lint:
	poetry run flake8 brain_games
# проверка flake8 на ошибки

publish:
	poetry publish --dry-run
# отладка публикации

packege-install:
	python3 -m pip install --user dist/*.whl
# установка пакета в систему

packege-reinstall:
	pip install --user --force-reinstall dist/*.whl
# переустановка пакета