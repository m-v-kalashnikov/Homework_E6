# Homework_E6
Get fibonacci number in docker
В репозитории готовый проект по заданию, Dockerfile и docker-compose.yml.

Запуск элементарный:
- клонируем репозиторий
- в папке репозитория:
    - docker-compose build
    - docker-compose up

После выполнения приведенной выше команды, вы можете получить доступ к приложению на http://localhost:5200

Ниже изложил задание на момент начала выполнения:
Задача

Сервис должен по GET запросу с параметром k возвращать k-ое число Фибоначчи. Необходимо реализовать кеширование, то есть, если число уже было запрошено, результат должен браться из кеша, а не пересчитываться.

Кеширование необходимо реализовать с помощью memcached (или redis), фреймворк для веб-сервиса используйте на ваше усмотрение, однако для такого небольшого проекта брать Django скорее перебор.

Приложение должно запускаться в Docker. Код приложения должен быть выложен на github, вместе с файлами Dockerfile и docker-compose.yml. В репозитории в README.md вам нужно поместить инструкцию по запуску приложения.

Дополнительно можно задеплоить это приложение в облачный сервис, например, Яндекс.Облако или mail.ru cloud solutions.

Задание считается выполненным, если:

    Прислана ссылка на репозиторий в github;
    Репозиторий содержит код приложения на Python, у которого есть эндпоинт, который GET запросу c параметром k считает k-ое число Фибоначчи;
    Рассчет k-ого числа Фибоначчи происходит только в случае, если ранее это число не запрашивалось, иначе значение берется из Redis или memcached;
    Приложение на Python и Redis могут быть запущены в контейнерах, и репозиторий содержит словесные (README.md) и машинные (Dockerfile, docker-compose.yaml) инструкции по запуску задания;
    Бонус: прислана ссылка этого приложения, развернутого в каком-либо облачном сервисе.
