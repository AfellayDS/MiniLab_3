# Лабораторная работа №3 (I вариант)
Студент: Филиппов Денис Константинович (группа 5030102/10401).
## Локальный запуск приложения
1. Склонируйте репозиторий
2. Создайте и активируйте виртуальное окружение для проекта
3. Установите зависимости с помощью команды 
	```bash
	pip install -r requirements.txt
	```
4. Запустите приложение с помощью команды
	```bash
	streamlit run main.py
	```
## Описание и логика работы
Приложение предоставляет программный интерфейс для работы с информационно-статистическим сервером Московской биржи. В рамках интерфейса доступны следующие типы информации: статические данные о рынках (режимы торгов и их группы, финансовые инструменты и их описание), данные для построения графиков ("свечей"), котировки, дивиденды, различные метаданные. Документация реализованных запросов в [Postman](https://elements.getpostman.com/redirect?entityId=31837212-c0e4d8ef-f3f2-4594-9f48-0d012e77395f&entityType=collection).

Для ввода и вывода информации доступен веб-интерфейс. Пользователю необходимо вести тикер компании (SBER, GAZP, PHOR, YNDX) и временной интервал, в пределах которого необходимо вывести исторические данные. После этого приложение создаст дашборд, который содержит информацию об исторических котировках и выплаченных дивидендах компании.