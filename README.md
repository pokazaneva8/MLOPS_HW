# HW_3_Pokazaneva

# ml_lab
В качестве s3 хранилища используется собственное minio:
* https://gitlab-tester-test.ru:8888 (UI)
* https://gitlab-tester-test.ru:8887 (console)

Пароли в файле .env.example

1. Каталог в момент начала выполнения pipeline-а
```
data/
        external/
                ...
        interim/
                i_love_ml.csv <- Исходный файл
        processed/
                ...
```

2. Скопировать данные из .env.example в файл .env
```sh
cp .env.example .env
```
3. Сделать исполняемым файлы в директории scripts
```
chmod +x ./scripts/*
```

4. Установка зависимостей через poetry
```
poetry install
```

5. Выполнить скрипт pipeline-а:
```
sh ./scripts/pipeline.sh
```
6. По ваш каталог должен иметь следующий вид:
```
data/
        external/
                i_love_ml.csv <- Файл загруженный через S3 хранилище
        interim/
                i_love_ml.csv <- Исходный файл
        processed/
                i_love_ml.csv <- Обработанный файл из S3 хранилища
```
