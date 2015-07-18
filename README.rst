============================
Final CMS Code for FastTrack
============================

Welcome dear reader!

This is the final code for the 'FastTrack to Building Your own Custom CMS Using Django'. If you
follow the instructions of the booklet, your own project should look similar.

We have added a script, `generate_data.py` that generates random data for use in your CMS. To make
it easier to use this script we are also including the `media` folder that contains images for use
within articles in the CMS.

If you are still reading the booklet, and just want to access to the code snippets used in that,
this is not the right place; what you are looking for can be found
`here <https://github.com/9dot9Media/fasttrack_to_cms_code_snippets>`_ instead.

This project has few direct requirements, and those are listed in the
`requirements.txt <./requirements.txt>`_ file. You can install the packages listed in this file using
the `pip` command as follows:

.. code:: shell

    pip install -r requirements.txt

After that use the `makemigrations` command to create the database migrations, and then the
`migrate` command to apply them. Normally the migrations created as part of the `makemigrations`
command are supposed to be part of the code and included within the repository.

.. code:: shell

    python3 manage.py makemigrations
    python3 manage.py migrate

Now create a superuser if you want to access the admin panel:

.. code:: shell

    python3 manage.py createsuperuser

Finally you can start the development server using the following command and access the application
at http://localhost:8000/:

.. code:: shell

    python3 manage.py runserver

Using the generate_data Script
------------------------------

The `generate_data.py <./generate_data.py>`_ script included with this code just had one additional requirement, and that
is `fake-factory`. The `fake-factory` Python package is incredibly useful when generating random
test data that feels similar in overall appearance and structure to the content it is emulating.

Installing this package is as easy as running:

.. code:: shell

    pip install fake-factory

After that you can simply run the script as a normal Python 3 script as:

.. code:: shell

    python3 generate_data.py

Since this script adds data to your database, it needs to have been initialised first by running the
`migrate` command. Also note that if you make too many changes to the code of this database, the
script might stop working as it is tied to the database structure as developed in the booklet.

If you want to know how this script works, don't worry it is documented.