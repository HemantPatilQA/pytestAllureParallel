Command To Execute
- pytest -n 4 --alluredir=allure-results
- pytest --reruns 2 -n 4 --alluredir=allure-results

Command to check the Allure Report after execution
- allure serve allure-results

<b>Command to Set Up Virtual Environment with PyThon 3.11</b>
- python3.11 -m venv venv
<br>Note : Make sure Python 3.11 is installed and it's path is added in the System Environment Variables
- To activate the virtual environment : venv\Scripts\deactivate
- To deactivate the virtual environment : deactivate
- 