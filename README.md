## hyper-science: make media in scientific papers explorable

This project is meant to be a prototype, developed by Alex Dagri ([@postaxmi](https://github.com/postaxmi)) and Alberto Chiusole ([@bebosudo](https://github.com/bebosudo)) for the course *Open Data Management and the Cloud* at [DSSC](https://dssc.units.it).

The goal of this project is to provide a practical example of how to setup a platform to **connect scientific papers to the multimedia** they are related to; e.g., papers about astrophysics can be linked to images of their observations, while papers of sound engineering can point to resources of their experiments.


### Tools used

We decided to use the Django web framework, and a specific extension on top of it, called Django REST Framework, to create the API for this project. Django has a really powerful ORM (Object Relational Mapping) tool, that allows the developer to write objects in a database as code, and let the tool map those to tables and relations.

[Django Rest Framework (DRF)](https://www.django-rest-framework.org/) is a flexible tool that relies on Django to create APIs, providing an easy serialization procedure.

We also used several other plugins to enhance the user experience when managing data: [django-filters](https://django-filter.readthedocs.io/) to quickly select objects from the database using easy filters and [django-crispy-forms](https://django-crispy-forms.readthedocs.io/) to more easily model these filters, [django-sql-explorer](https://github.com/groveco/django-sql-explorer) to provide an SQL interface for more complex queries, [DRF-xml](https://github.com/jpadilla/django-rest-framework-xml) to provide XML parsers for machine-usability.


### Environment setup

The best way to setup the environment is to use `pipenv`, with the provided Pipfile (Python version 3.6 must be available in the system):

```console
$ git clone https://github.com/postaxmi/hyper-science.git
$ cd hyper-science
$ pipenv install
```
To populate the database with some test data, use:
```console
$ pipenv shell
$ ./hyper-science/manage.py migrate
$ ./hyper-science/example-db-populator.py
```

To run the development server, use:
```console
$ pipenv shell
$ ./hyper-science/manage.py runserver
```


### Test queries

Once the environment is setup, you can test some queries, e.g.:

* http://127.0.0.1:8000/api/v1/category_concepts/
* http://127.0.0.1:8000/api/v1/category_concepts/?attribute__description__icontains=WEIght
