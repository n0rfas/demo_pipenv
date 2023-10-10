# Demo pipenv



## Создание виртуального окружения

```shell
pipenv --python 3.10
```

По умолчанию виртуальное окружение размещается в месте наподобие: `/Users/anton/.local/share/virtualenvs/demo_pipenv-FiqZ1MBE`.

## Добавление пакета

```shell
pipenv install fastapi
```

## Добавление пакета в окружение разработчика

```shell
pipenv install pytest --dev
```

## Активация виртуального окружения

```shell
pipenv shell
```

При активации окружения все переменные из файла `.env` пробрасываются в него.

## Выход из окружения

```shell
exit
```

## Запуск скриптов внутри окружения (без активации)

```shell
pipenv run printspam
```
