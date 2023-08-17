# Project Documentation

This documentation provides information on setting up, configuring, and using the OEE Calculator Django project.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#Prerequisites)
3. [Installation](#Installation)
4. [Configuration](#Configuration)
5. [Usage](#Usage)



## Introduction

The OEE Calculator is a Django application that calculates the Overall Equipment Effectiveness (OEE) of machines based on production data. It provides a REST API to retrieve OEE data, and it allows filtering by camera name, date range, and OEE threshold.

## Prerequisites

Before you begin, ensure you have the following requirements met:

-Python 3.x installed
-Django installed (`pip install django`)
-Django Rest Framework installed (`pip install djangorestframework`)

### Installation
Clone the repository:

- Example:
  ```http
  git clone `https://github.com/BurhanMohammad/ OEE-Calculator.git`
  cd OEECalculator


### Install project dependencies:
- Example:
```http
  pip install -r requirements.txt

```

### Configuration
- Configure the database settings in `OEECALICUATUR/settings.py`.
- Run database migrations:
```http
    python manage.py migrate

```  
    
## Usage
Run the development server:
```http
 python manage.py runserver
```
-Access the API at `http://localhost:8000/`.

### API Endpoints
-`/machines/`: List of all machines.
-`/production-logs/`: List of all production logs.
-`/oee-calculation/`: Calculate OEE data based on      filters.
## License
This project is licensed under the MIT License.

