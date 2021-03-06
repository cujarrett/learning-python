## What is it?
It's a small set of hacks to learn the basics of [Python](https://www.python.org/). Python is powerful, fast,
plays well with others, runs everywhere, is friendly & easy to learn, is Open. I'm using Python 3.7.5 for this project (current LTS).

## Take Aways
- Python comes on a lot of OS's by default but it's more common to find Python 2 instead of Python 3.
- Python `Virtual Environments` allow you to specify a specific version of Python for that use. Requires first installing `virtualenv` via `pip install virtualenv`.

  Example creation of Python `Virtual Environments`
  ```sh
  # virtualenv <folder to create> <path to desired python version install>
  virtualenv py3 -p /usr/local/bin/python3
  ```

  Example activation of Python `Virtual Environments`
  ```sh
  # <folder created above via >/bin/activate
  py3/bin/activate
  ```

  Example deactivation of Python `Virtual Environments`
  ```sh
  deactivate
  ```

- Python's package manager `pip` manages dependencies. It leverages a `requirments.txt` file detailing project dependencies.

  Example package install
  ```sh
  pip freeze > requirements.txt
  ```

  Example pip `requirments.txt` file
  ```sh
  cat requirements.txt
  ```

  ```python
  certifi==2019.9.11
  chardet==3.0.4
  idna==2.8
  requests==2.22.0
  urllib3==1.25.7
  ```

- `pip install` vs. `import`? `pip install` brings the dependency local for runtime where as `import` uses a looked up asset via putting it somewhere python can expect it to be.

- In Python everything has a id. The id property is immutable.
- In Python everything has a value.

- Immutable vs. Mutable Types

  | Class      | Description                          | Immutable          |
  |------------|--------------------------------------|--------------------|
  | bool       | Boolean value                        | :white_check_mark: |
  | int        | integer                              | :white_check_mark: |
  | float      | floating-point number                | :white_check_mark: |
  | list       | mutable sequence of objects          |                    |
  | tuple      | immutable sequence of objects        | :white_check_mark: |
  | str        | character string                     | :white_check_mark: |
  | set        | unordered set of distinct objects    |                    |
  | fronzenset | immutable form of set class          | :white_check_mark: |
  | dict       | associative mapping (aka dictionary) |                    |

  ```python
  b = []
  b(id) # 4527447816
  b.append(3)
  print(b) # [3]
  ```

  ```python
  a = 4
  id(a) # 4321639424
  a = a + 1
  id(a) # 4321639456
  ```

- Use `None` for null check in Python. Use a `foo is None` check for performance vs. slower and more process heavy ` foo == None` as `foo is None` checks the id and it exits with less process needed.

- [Strings](./strings.py)
- [String Manipulation](./string-manipulation.py)
- [Conditionals](./conditionals.py)
- [Loops](./loops.py)
- [Relational Operators](./relational-operator.py)
- [Lists](./lists.py)
- [List Slice](./list-slice.py)
- [List Comprehensions](./list-comprehensions.py)
- [Dictionaries](./dictionaries.py)
- [Tuples](./tuples.py)
- [Sets](./sets.py)
- [Logging](./logging.py)
- [Command Line Input](./cli-input.py)
- [Functions](./functions.py)
- [Modules](./modules.py)
- [Reading From A File](./reading-from-a-file.py)
- [Writing To A File](./writing-to-a-file.py)
- [Error Handling](./error-handling.py)
- [Scopes](./scopes.py)
- [Classes](./classes.py)

- `pip` useful commands
  - `pip install <package-name>` to install a package
  - `pip list` to list all packages installed to the current virtual environment
  - `pip search <package-name>` can be used to search packages available
  - `pip list --outdated` show out of date dependencies
  - `pip uninstall <package-name> ` to uninstall package

## Things I like
- Simple
- Forces good styling as there is no braces used
- Key word arguments
  ```python
  def madlibs(name, noun = "shoes", adjective = "red"):
    return "{0} has {1} {2}".format(name, adjective, noun)
  madlib = madlibs("Will", adjective="black", noun="boots")
  print(madlib) # Will has black boots
  ```

## Things I'm not a huge fan of
- Python's package ecosystem doesn't seem to all use [Semantic Versioning](https://semver.org/) (example: `idna` as `2.8`)
- Text file for dependency details feels lackluster
- Underscore as multi word variable convention (`sum_of_two_numbers = 1 + 3`) :expressionless:
- `global`, `nonlocal`, and local varibales are confusing solution that feels clumsier than just having scopes be blocked at first glance. I'm sure there's cool things you could do with it in principal, but I also feel like you'd be a jerk if you actually used them.
