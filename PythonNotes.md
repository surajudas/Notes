# Misc Python notes
- [Misc Python notes](#misc-python-notes)
  - [Tips](#tips)
    - [Naming Conventions](#naming-conventions)
  - [Standard library](#standard-library)
    - [Zip()](#zip)
    - [Packing and Unpacking variables](#packing-and-unpacking-variables)
  - [Venv](#venv)
  - [Pyinstaller](#pyinstaller)
  - [Threading](#threading)
    - [Main code](#main-code)
  - [Object oriented programming](#object-oriented-programming)
    - [Classes](#classes)
    - [Methods](#methods)
    - [Creating our custom classes](#creating-our-custom-classes)
    - [__init__](#init)
    - [self](#self)
    - [Inheritance](#inheritance)
    - [Changing a method of the parent class from the child](#changing-a-method-of-the-parent-class-from-the-child)
    - [Class Attributes](#class-attributes)
    - [Class Methods](#class-methods)
    - [Static Methods](#static-methods)
  - [Working with apis](#working-with-apis)
    - [Simplest example](#simplest-example)
    - [Headers](#headers)
    - [Payloads](#payloads)
      - [GET](#get)
      - [POST](#post)
    - [Authentication](#authentication)
    - [Bearer Authentication](#bearer-authentication)
    - [Status codes](#status-codes)
  - [SqilteDB](#sqiltedb)
    - [Best practices](#best-practices)
  - [Lambda, Map and filter](#lambda-map-and-filter)
    - [Lambda](#lambda)
    - [Map](#map)
    - [Filter](#filter)
  - [Genrators in python](#genrators-in-python)

## Tips
- Use [pyp](https://www.pypy.org/) when doing memory intensive tasks (web frameworks, graphics, etc) or need speed (optimisation)  
- Error: UnicodeEncodeError: 'charmap' codec can't encode character '\u2640' in position 23: character maps to <undefined> 
  - Fix: with open("mangas.txt",'w',encoding='utf-8') as f:
  - You just change the encoding of the text to utf-8
- Error: AttributeError: impartial import of random 
  - Fix: Donot name your py file random.py
- Error: sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread.
  - Fix: In your sqlite3.connect() add check_same_thread=False
  - Note: Make sure that only one write operation is done at a time

### Naming Conventions
So PEP 8 tells you that:

- modules (filenames) should have short, all-lowercase names, and they can contain underscores;
- packages (directories) should have short, all-lowercase names, preferably without underscores;
- classes should use the CapWords convention.

---
PEP 8 tells that names should be short; this following gives a good overview of what to take into account when creating variable names, which also apply to other names (for classes, packages, etc.):

- variable names are not full descriptors;
- put details in comments;
- too specific name might mean too specific code;
- keep short scopes for quick lookup;
- spend time thinking about readability.

## Standard library
### Zip()
- Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. 
- With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.
```
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y) # zip() Creates a iterator
>>> list(zipped) # Iterator converted to list
[(1, 4), (2, 5), (3, 6)]
``` 
### Packing and Unpacking variables
- You can assign multiple values to multiple variables by separating variables and values with commas `,`.
- values can be of diff types
`a, b, c = 1, 2, 3`
- If there is one variable on the left side, it is assigned as a tuple.
`a = 1, 2, 3`
- If the number of variables on the left and the number of values on the right do not match, a ValueError will occur, but you can assign the rest as a list by appending * to the variable name.
```py
# a, b = 100, 200, 300
# ValueError: too many values to unpack (expected 2)

# a, b, c = 100, 200
# ValueError: not enough values to unpack (expected 3, got 2)

a, *b = 100, 200, 300

# a -> 100, b -> (200, 300) 
```
- You can assign the same value to multiple variables by using = consecutively.
`a = b = 1` 

## Venv
- Use venv to isolate packages from the main py installation when doing projects
```
# Starting the venv 
c:\>python -m venv c:\path\to\myenv
<venv>/bin/Activate.ps1
for eg.
python -m venv venv
venv/bin/Activate.ps1
```
- Switching python interpreter to venv's python
 - To select a specific environment, use the Python: Select Interpreter command from the Command Palette (Ctrl+Shift+P).
![python interpreter](https://code.visualstudio.com/assets/docs/python/environments/select-interpreters-command.png)

## Pyinstaller
- When using pyinstaller in a venv be sure to change the python interpreter of the shell to the venv's one otherwise it won't be able to find the python installation 
- The command I use mostly- `pyinstaller <nameofthefile>.py --onefile --icon=<path to ico file>`, the icon path is not in quotes btw

## Threading 
> I'll be using the concurent futures library not the threading one

### Main code
```python
import concurrent.futures

with concurrent.futures.ThreadPoolExecutor() as e:
    # when you dont have any arguments
    f1 = e.submit(do_something)
    # when you want to get the return value of the funct
    f2 = e.submit(do_something, 1) 
    print(f2.result())
    # when you want to pass in a list of arguments
    for arg in args:
        e.submit(do_something,arg)
    # alternatively
    e.map(do_something, args)     
    # for return values
    # with submit method
    results = [e.submit(do_something,arg) for arg in args] 
    for f in concurrrent.futures.as_completed(results):
        print(f.result())
    # with map method
    e.map(do_something, args)
    for result in results:
        print(result)     
```

## Object oriented programming
The main objective of oop is to create reusable code that's easy to modify or in more elegant words:-
> Object-oriented is a software design in which we can simply group data its data types and methods under a single package.

### Classes
- Pretty much everything that we work with in python is an object of a class
- Python has built in classes like  , int, float,...
- What operations we can do is defined by that object's class say we do `'s'+2` this will give us an error since an addition operation has not been defined bw a  ing and int class

### Methods
- A method is knida like what actions you can perform with that class
- you could also say its functions that go into our classes 

### Creating our custom classes 
```python
class <class_name>:
    def method(self):
        do_something

x = class_name()
```
- Suppose we create a dog class
```python
class dog:
    def bark(self):
        print("Bow Bow")

x = dog()
x.bark()
print(type(x))
```
- When we print out the type of our variable x we get `<class '__main__.dog'>`
  - main being the default module that is used and dog is the class that x is assigned the instance of  
- Methods can obviously take in arguments and return something too 
```python
class calc:
    def add(self,x,y):
        return x + y
print(calc().add(2,3))       
``` 

### __init__
- The init method gets invisibly called everytime an object of that class is made
- To me it seems like that the innit method kinda defines the fundamental characteristics of that class 
  - So lets say we have a car class then we would have its company, color, horsepower, torque, etc as its fundamental properties
```python
class car:
    def __init__(self, model, hp, color):
        self.model = model
        self.hp = hp
        self.color = color
    def selling_price(self):
        # do some evaluation
        return (f'{10*self.hp*random.randint(1,10)}$')    
MyCar = car('mitsubushi',450,'blue')        
print("You'll get around",MyCar.selling_price(),"for your car")
```

### self 
- Self passes in a reference of the object created to its parent class
- We can use self to define the basic nature of the class as we did in above examples 
- We can access/modify these `self.<values>` from both outside the class and from inside the methods 
- We can also have `self.<values>` that are not taken as attributes, for eg. `self.alive` in the code bellow is not taken as an argument
```python
class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.alive = True
    def change_name(self, name):
        self.name = name
    def get_identity(self):
        print(self.name, self.age)    

x = dog("tim",12)
x.get_identity()
x.change_name("larry")
x.get_identity()
```

### Inheritance
- Inheritance allows you to use the blueprint of the parent class and then pass it on to child classes 
- You pass on the parent's blueprint to child classes by passing the parent class as an argument to the child classes
- When the same method exists in the parent and child classes the method of the child class overrides the parent's or in other words the more specific one always wins
```python
class pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hi I am {self.name} and {self.age} year(s) old")
    def speak(self):
        print("Uhhh")   
class cat(pet):
    def speak(self):
        print("Meow")        
class dog(pet):
    def speak(self);
        print("Bow Bow")
x = cat("Kali",6)
x.introduce()
y = dog("Baloo",3)
y.introduce()                
```

### Changing a method of the parent class from the child
- If we need to change/add to a method of the parent class from inside the child class we can use the super() method to do so 
- The super() is a reference to the parent class 
- But if we are changing some method of the parent class we do need to write out the arguments for that method and pass them inside the `super.<method>(arg1,arg2)`
```python
class pet:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
# You gotta include the args for the method that ur changing
class cat: 
    def __init__(self, name, age, color):  
        super().__init__(name, color) 
        self.color = color             
```

### Class Attributes
- Class attributes are used to define data that is not specific to an instance of that class, we could say that they are constants that apply to all objects of that class
- Class attributes are not defined inside any of the methods of the class but instead defined below the class definition
- They can be accessed by calling `<classname>.<attrname>` and without the need to create an object of that class
- If you change the class attribute from your code, it is changed for all objects of that class 
- They are only useful in pretty niche situations 
```python
class stock:
    items = 0
    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity 
        stock.items += quantity
milk = stock("milk",2)
print(stock.items)
sauce = stock("sauce",3)
print(stock.items)        
``` 

### Class Methods 
- Class methods are used to act on class attributes they are again not specific to an instance of that class and can be called by using `<classname>.<methodname>` 
- They are created using a special decorater `@classmethod` and passing in the `cls` argument
> NOTE: A class method can't access instance specific properties like `self.<somevale>`
```python 
# Rewriting the above code using class method
class stock:
    items = 0
    def __init__(self, name, quant):
        self.name = name 
        self.quant = quant
        stock.items += self.quant
    @classmethod
    def show_stock(cls):
        print(stock.items)    
milk = stock("milk",2)
stock.show_stock()
sauce = stock("sauce",3)
stock.show_stock()          
```

### Static Methods
- Static methods are more used for organisation than for usablility 
- The main idea being that they don't change anything as in they are *static* 
```python
class Calc:
    @staticmethod
    def add(x,y):
        return x + y
    @staticmethod    
    def multiply(x,y):
        return x*y
    @staticmethod    
    def divide(x,y):
        return x/y
print(Clac.add(2,3))
print(Calc.multiply(2,3))   
```              

## Working with apis
> I'll continue when I need more  

[docs]("https://docs.python-requests.org/en/v3.0.0/user/quickstart/")

### Simplest example 
- We import the requests module to interact with the api and use the get method to well get the response from the api
- Their response is stored in a variable generally called response 
- We get a status code and the thing that we requested for if the call is successful
- After that we can use the json method on the response to make a dictionary out of it and process it further
```python 
import requests

response = requests.get("https://randomfox.ca/floof") # Creates a response object 
print(response.status_code) # Prints out the api status code  
fox = response.json() # Creates a dictionary from the response object to work with
print(fox['image']) 
```

- We can use the json module to clean up the response beforeprinting it out 
```python
import json

def jprint(obj):
    # create a formatted  ing of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
```

### Headers
- If you’d like to add HTTP headers to a request, simply pass in a dict to the headers parameter.
```py
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)
```

### Payloads
#### GET
- You often want to send some sort of data in the URL’s query  ing. If you were con ucting the URL by hand, this data would be given as key/value pairs in the URL after a question mark, e.g. httpbin.org/get?key=val.
- Requests allows you to provide these arguments as a dictionary of  ings, using the params keyword argument. As an example, if you wanted to pass key1=value1 and key2=value2 to httpbin.org/get, you would use the following code:
```py
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)
# resultant url: https://httpbin.org/get?key2=value2&key1=value1
```
- You can also pass a list ofitems as a value:
```py
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)
# resultant url: https://httpbin.org/get?key1=value1&key2=value2&key2=value3
```
#### POST
- Typically, you want to send some form-encoded data — much like an HTML form. To do this, simply pass a dictionary to the data argument. Your dictionary of data will automatically be form-encoded when the request is made:
```py
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)
# the post request on json form
{
  ...
  "form": {
    "key2": "value2",
    "key1": "value1"
  },
  ...
}
```
- There are times that you may want to send data that is not form-encoded. If you pass in a  ing instead of a dict, that data will be posted directly. 
- The json parameter will automatically encode your dictionary to a  ing value
- Using the json parameter in the request will change the Content-Type in the header to application/json.
- I had to use this method to interact with the Mangadex api
```py
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, json=payload)
```
### Authentication 
- To use most apis you have to authenticate yourself I've seen these 3 forms:
  1. Creating an account with the service and getting yourself a tokken which is then sent alongside the payload
  2. Many web services that require authentication accept HTTP Basic Auth. This is the simplest kind, and Requests supports it  aight out of the box.
  Making requests with HTTP Basic Auth is very simple:
  ```py
  requests.get('https://api.github.com/user', auth=('user', 'pass'))
  <Response [200]>
  ```
  3. Some use the post http method to post the credentials to the api which returns a session and refresh tokken, mangadex uses this way of auth 
  ```py
  payload = {"username": " ing","password": " ingst"}
  response = requests.post("https://api.mangadex.org/auth/login", json=payload)
  ```

### Bearer Authentication
- Bearer authentication (also called token authentication) is an HTTP authentication scheme that involves security tokens called bearer tokens. The name “Bearer authentication” can be understood as “give access to the bearer of this token.” 
- The bearer token is a cryptic  ing, usually generated by the server in response to a login request. The client must send this token in the Authorization header when making requests to protected resources:
```json
Authorization: Bearer <token>
```
### Status codes
- 200: Everything went okay, and the result has been returned (if any).
- 301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or anendpoint name is changed.
- 400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
- 401: The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t sendthe right credentials to access an API.
- 403: The resource you’re trying to access is forbidden: you don’t have the right permissions to see it.
- 404: The resource you tried to access wasn’t found on the server.
- 405: Method not allowed http exception (your using the wrong http method eg get in place of post)
- 503: The server is not ready to handle the request.

## SqilteDB
SQilte is a lightweight disk-based database which doesn't require a seperate server to operate like most other dbs. It is mostly used for internal processes and prototyping.  
It is a built in library in python, thus no imports. 
1. To get started you need to first create an object to represent the db, a connector

```py
import sqlite3
con = sqlite3.connect('example.db')
```

2. You can also supply the special name :memory: to create a database in RAM. This is really useful for a lot of use cases
   1. The proper way to do in-memory databases is to create a context manager with the connector which automatcally commits the changes if succesful and rollbacks the changes if an exception occurs.

```py
#Create the connection outside of the function, and pass it into the function, or create a shared memory connection:

db = sqlite3.connect("file::memory:?cache=shared")

#However, the database will be erased when the last connection is deleted from memory; in your case that'll be each time the function ends.
#Rather than explicitly call db.commit(), just use the database connection as a context manager:

try:
    with db:
        cur = db.cursor()
        # massage `args` as needed
        cur.execute(*args)
        return True
except Exception as why:
    return False

#The transaction is automatically committed if there was no exception, rolled back otherwise. Note that it is safe to commit a query that only reads data.
```

3. Once you have a Connection, you can create a Cursor object and call its execute() method to perform SQL commands:

```py
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
```

4. The data you’ve saved is persistent (on hardisk) and is available in subsequent sessions:

```py
import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()
```

5. To retrieve data after executing a SELECT statement, you can uss 3 ways 
   1. treat the cursor as an iterator
   2. call the cursor’s fetchone() method to retrieve a single matching row 
   3. call fetchall() to get a list of the matching rows.

```py
# Iterator example
for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)

# Outuput
# ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)
# ('2006-03-28', 'BUY', 'IBM', 1000, 45.0)
# ('2006-04-06', 'SELL', 'IBM', 500, 53.0)
# ('2006-04-05', 'BUY', 'MSFT', 1000, 72.0)

# Fetch example
cur.execute('SELECT * FROM stocks ORDER BY price')
row = cur.fetchone()
rows = cur.fetchall()
print(row)

# Output
# ('2006-01-05', 'BUY', 'RHAT', 100.0, 35.14)
# [('2006-01-05', 'BUY', 'RHAT', 100, 35.14), ('2006-03-28', 'BUY', 'IBM', 1000, 45.0), ('2006-04-06', 'SELL', 'IBM', 500, 53.0), ('2006-04-05', 'BUY', 'MSFT', 1000, 72.0)]
```

### Best practices
- Often we will need to use values from Python variables and the first way to do that comes to our mind is fstrings to insert the variable into the sql query but that is a very bad idea since that opens up the app to sql **injection attacks**. 

```py
# Never do this -- insecure!
symbol = 'RHAT'
cur.execute(f"SELECT * FROM stocks WHERE symbol = '{some_variable}'")   
```

- Instead, use the DB-API’s parameter substitution. Put a placeholder wherever you want to use a value, and then provide a tuple of values as the second argument to the cursor’s execute() method. An SQL statement may use one of two kinds of placeholders: question marks (qmark style) or named placeholders (named style). For the qmark style, parameters must be a sequence. For the named style, it can be either a sequence or dict instance. The length of the sequence must match the number of placeholders, or a ProgrammingError is raised. If a dict is given, it must contain keys for all named parameters. Any extra items are ignored. Here’s an example of both styles:

```py
import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table lang (name, first_appeared)")

# This is the qmark style:
cur.execute("insert into lang values (?, ?)", ("C", 1972))

# The qmark style used with executemany():
lang_list = [
    ("Fortran", 1957),
    ("Python", 1991),
    ("Go", 2009),
]
cur.executemany("insert into lang values (?, ?)", lang_list)

# And this is the named style:
cur.execute("select * from lang where first_appeared=:year", {"year": 1972})
print(cur.fetchall())

con.close()
```
> Tip: 
> - Sqlite doesn't have a bool type by default so use this instead `mycol BOOLEAN NOT NULL CHECK (mycol IN (0, 1))` when you need a bool type coloumn. Here 0/1 rep False/True respectively.
```
cur.execute('''CREATE TABLE animes 
    (id INTEGER PRIMARY KEY, date text, name text NOT NULL UNIQUE, ep int, wstate BOOLEAN NOT NULL CHECK (wstate IN (0, 1)), online BOOLEAN NOT NULL CHECK (online IN (0, 1)));''')
```

> - A `UNIQUE` constraint ensures all values in a column or a group of columns are distinct from one another or unique.
>   - The following shows how to define a UNIQUE constraint for a column at the column level and a UNIQUE constraint for multiple columns resp:
```sql
CREATE TABLE table_name(
    ...,
    column_name UNIQUE,
    ...
);
```
```sql
CREATE TABLE table_name(
    ...,
    UNIQUE(column_name1,column_name2,...)
);
``` 

## Lambda, Map and filter

### Lambda
- Lambda functions add grace to your python programs by making it easy to write functions in one line and when the only do a single thing.
- You can only execute one expression inside a lambda function.
```py
# Normal function
def add(x,y):
    return x+y

# Lambda function
lambda x,y: x+y

# Can be assigned to a variable
addout = lambda x,y: x+y
addout(3,5) # Gives 8
```

### Map
- Map method allows us to send all elements of an iterable through a function without using loops
- map() is useful when you need to apply a transformation function to each item in an iterable and transform them into a new iterable.
Basic syntax: `map(function, iterable[, iterable1, iterable2,..., iterableN])`
- Now, map() returns a map object, which is an iterator that yields items on demand.   
That’s why you need to call list() to create the desired list object or next() to get individual values.
```py
nums = [1,2,3,4]
sqrs = map(lambda x: x**2, nums)
print(next(sqrs))
# Output: 1
# OR
sqrslist = list(sqrs)
print(sqrslist)
# Output: [4,9,26]
```
- If you supply multiple iterables to map(), then the transformation function must take as many arguments as iterables you pass in. Each iteration of map() will pass one value from each iterable as an argument to function. The iteration stops at the end of the shortest iterable.
```py
first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]
list(map(pow, first_it, second_it))
# [1, 32, 729], the map stopped at 3 since it was the shortest iteratable
```

### Filter
- The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
```py
# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))
```

## Genrators in python
todo ✔