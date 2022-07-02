# Тестирование Selenium+Behave(BDD)+Allure
## Команда запуска скрипта
behave -f allure_behave.formatter:AllureFormatter -o reports/ features
## Команда вывода отчета в браузер
allure serve reports/
# Тестирование Selenium(Page Object)+Pytest+Allure
## Команда запуска скрипта
pytest --alluredir results
## Команда вывода отчета в браузер
allure serve results