# Flask (Python) example

## [Python](https://www.python.org/)
From [Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))
> Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales. Van Rossum led the language community until stepping down as leader in July 2018.

> Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, it also has a comprehensive standard library.

> Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation.

## [Flask](http://flask.pocoo.org/)
> Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. And before you ask: It's BSD licensed!

A quick note on Flask v Django and on why we chose Flask. While Django provides a lot of really great features, it also locks you into the way it expects you to do things like database, migrations, seeding, views. We have a need to connect to various data backends, including Elasticsearch, and to provide a consistent API layer with JSON-API. Flask just gives us greater flexibility to do so.

## Koans
(Programming) Koans are a popular tutorial-esque style of learning new programming languages through examples and TDD. Created initially for the [Ruby](https://www.ruby-lang.org/en/) programming language, many ports have been created for other languages.

You can find [Python Koans](https://github.com/gregmalcolm/python_koans) on GitHub.