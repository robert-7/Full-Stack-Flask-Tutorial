# Flask Application

This is where you'll find the Flask codebase.

## Folder and File Structure

* [static](static) - Holds any static files that need to be sent over by the server
* [templates](templates) - Holds the template HTML page files
* [__init__.py](__init__.py]) - The entrypoint into our app module. It's the first
  thing that's loaded in the module.
* [course_list.py](course_list.py) - A list of dictionaries containing course data, used to seed the database.
* [forms.py](forms.py) - Where the WTForms classes are defined for handling user input and validation.
* [models.py](models.py) - Where the models are defined. This is the link between
  MongoDB documents in a collection and Python objects of a class.
* [routes.py](routes.py) - Where the path routes are defined.
