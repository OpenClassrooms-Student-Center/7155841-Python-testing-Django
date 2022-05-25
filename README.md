[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

# Django-Test-Project
This project has been created for you to practice different types of testing. The source code contains a Django project for a mini e-commerce site. You can use it to develop a set of scenarios needed to test all of the source code. Note that the suggested solutions are available in different branches of the directory structure.

## Prerequisites
- Install Python 3: [Python 3 download](https://www.python.org/downloads/)
- Install git: [Git download](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)


## Installation
1. Download the Project to Your Local Directory:
```shell
git clone https://github.com/OpenClassrooms-Student-Center/4425126-testing-python.git 
cd 4425126-testing-python
```

2. Set up a Virtual Environment:
  - Create the virtual environment: `python -m venv venv`
  - Activate the virtual environment:
    - Windows: `venv\Scripts\activate.bat`
    - Unix/MacOS: `source venv/bin/activate`
3. Install project dependencies
```shell
pip install -r requirements.txt
```

## Run
- Run the server using the following command: `python manage.py runserver`

## Solutions
1. Suggested solution for unit testing using Pytest:
```shell
git checkout pytest-test
pytest
```

2. Suggested solution for unit testing using fixtures:
```shell
git checkout fixture-test
pytest
```

3. Suggested solution for unit testing using classes:
```shell
git checkout class-test
pytest
```

4. Suggested solution for integration testing:
```shell
git checkout integration-test
pytest
```

5. Suggested solution for functional testing (don't forget to download the webdriver):
```shell
git checkout functional-test
python manage.py test
```

6. Suggested solution for performance testing:
```shell
git checkout performance-test
locust
```

