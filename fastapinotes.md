# FastAPI
> FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

- [FastAPI](#fastapi)
  - [Installation](#installation)
  - [Basic Structure](#basic-structure)
    - [Routing](#routing)
    - [Route handler](#route-handler)
    - [Concurrency](#concurrency)
  - [Docs](#docs)
  - [Path Parameters](#path-parameters)
    - [Path parameters with types](#path-parameters-with-types)
    - [Path Parameters and Numeric Validations](#path-parameters-and-numeric-validations)
  - [Order matters](#order-matters)
  - [Query Parameters](#query-parameters)
    - [Optional Params](#optional-params)
    - [Additional query validations](#additional-query-validations)
  - [Request Body](#request-body)
    - [Using Pydantic Models](#using-pydantic-models)
  - [Handling Errors](#handling-errors)
  - [Posting files to the api](#posting-files-to-the-api)
    - [To remember while handling files](#to-remember-while-handling-files)
  - [Getting files from api](#getting-files-from-api)
  - [Background tasks](#background-tasks)
  
## Installation
`pip install fastapi` & `pip install uvicorn` (for a web server)

## Basic Structure
- imports `from fastapi import FastAPI`
- Instantiate the app instance `app = FastAPI()`

### Routing 
- Routes in fastapi are done by using decorators with that routes corresponding http method eg. `@app.get('/'), @app.post('/')`
- One of:
    - POST
    - GET
    - PUT
    - DELETE

### Route handler
- The async route handler is defined just below it
```py
async def root():
    return {"message": "Hello World"}
```
- On opening the route on a browser you will get the json response: `{"message": "Hello World"}`

### Concurrency
- If you are using third party libraries that tell you to call them with await, like:
`results = await some_library()`
- if you are using a third party library that communicates with something (a database, an API, the file system, etc) and doesn't have support for using await then declare your path operation functions as normally, with just def
- If your application (somehow) doesn't have to communicate with anything else and wait for it to respond, use async def.

## Docs
- Docs for the api are auto generated in fastapi
- 2 types of docs are created:- Swagger, ReDoc
- A "schema" is a definition or description of something. Not the code that implements it, but just an abstract description.

## Path Parameters
- Path parameters are passed by using f-string like syntax on the decorator and then supllying it to the function
```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```
- Using an option directly from Starlette you can declare a path parameter containing a path using a URL like: `/files/{file_path:path}`
- In this case, the name of the parameter is file_path, and the last part, :path, tells it that the parameter should match any path.
```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
```

### Path parameters with types
- You can declare the type of a path parameter in the function, using standard Python type annotations:
```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```
- This also provides automatic type validation
- But if you go to the browser at http://127.0.0.1:8000/items/foo, you will see a nice HTTP error of:
```
{
    "detail": [
        {
            "loc": [
                "path",
                "item_id"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}
```
- notice that it also gives the exact loc (location) where the validation didn't pass
> Note: The value provided is automatically converted from string to python int

### Path Parameters and Numeric Validations
- The same way you can declare more validations and metadata for query parameters with Query, you can declare the same type of validations and metadata for path parameters with Path.
```py
from typing import Optional
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```
## Order matters
- When creating path operations, you can find situations where you have a fixed path.
- Like /users/me, let's say that it's to get data about the current user.
- And then you can also have a path /users/{user_id} to get data about a specific user by some user ID.
- Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}:
```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
```
- **Otherwise**, the path for /users/{user_id} would match also for /users/me, "thinking" that it's receiving a parameter user_id with a value of "me".

## Query Parameters
- Query parameters are the variables passed in to the api like `someapi.com/foo/?skip=0&limit=10`
- When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.
```py
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```
- We can make the query params have a default value by just defining that default value in the function definition like we did in the above example
- You can also declare bool types, and they will be converted like 1,yes,True,flase,0 will correspond to True and Flase

### Optional Params
- To declare a query param as optional we have to import optional from typing and then specify like `q: Optional[str] = None`
```py
from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
```

- If a default value is not provided for a query param then its assumed as required and the request will give error if it is not provided  
eg.
```{
    "detail": [
        {
            "loc": [
                "query",
                "needy"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
}
```
### Additional query validations
- first import Query from fastapi
- ues parameters to Query (min_length,max_length,gt: greater than,ge: greater than or equal,lt: less than,le: less than or equa)
- default values are added as an argument in the begining of Query
- To make the query param required while using Query use `...` as the first argument
```py
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```
- If u get a error when you define a non-defult param before a default param then pass *, as the first parameter of the function.
```py
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get"), q: str
):
```

## Request Body
- When you need to send some data to the api you send it via a request body
- The api also always sends out a response body 
- The request body is sent via a post,put,delete request 
- To declare a request body, you use Pydantic models 

### Using Pydantic Models 
- First, you need to import BaseModel from pydantic
- Then you declare your data model as a class that inherits from BaseModel.
- Use standard Python types for all the attributes
- The same as when declaring query parameters, when a model attribute has a default value, it is not required. Otherwise, it is required. Use None to make it just optional.
- To add it to your path operation, declare it the same way you declared path and query parameters:
```py
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
```
- Inside of the function, you can access all the attributes of the model object directly:
```py
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
```
- Fastapi will auto detect if the function parameter is a path param/query/request body

## Handling Errors
- To use http errors import HTTPException from fastapi
- We use this way of handling errors instead of return because of security concerns
```py
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
```

## Posting files to the api
- To post or get a file with fastapi u need to import `file` and `UploadFile` from `fastapi`: `from fastapi import FastAPI, File, UploadFile`
- The file is sent using a request body
- Any type of file can be sent using the `UploadFile` argument 
- Just define the function like:   
`async def create_upload_file(file: UploadFile = File(...)`  

**UploadFile**  

UploadFile has the following attributes:  

- filename: A str with the original file name that was uploaded (e.g. myimage.jpg).
- content_type: A str with the content type (MIME type / media type) (e.g. image/jpeg).
- file: A SpooledTemporaryFile (a file-like object). This is the actual Python file that you can pass directly to other functions or libraries that expect a "file-like" object.

UploadFile has the following async methods:  

- write(data): Writes data (str or bytes) to the file.
- read(size): Reads size (int) bytes/characters of the file.
- seek(offset): Goes to the byte position offset (int) in the file.
    - E.g., await myfile.seek(0) would go to the start of the file.
    - This is especially useful if you run await myfile.read() once and then need to read the contents again.
- close(): Closes the file.

- As all these methods are async methods, you need to "await" them. For example, inside of an async path operation function you can get the contents with:  

`contents = await myfile.read()`

- If you are inside of a normal def path operation function, you can access the UploadFile.file directly, for example:  

`contents = myfile.file.read()`

Full example:  
```py
from fastapi import FastAPI, File, UploadFile

@app.post("/uploadfile/")
async def create_upload_file(*, file: UploadFile = File(...), parent: str, description: Optional[str] = None):
    contents = await file.read()
    PostFile(contents,file.filename,description,parent)
    file.close()
    return {"status": "uploaded ok"}
```    

### To remember while handling files 
- Always close the file after youre done with all the proccessing
- If you want to get all the content of the uploaded file call the read method on the file, like:  
`contents = await file.read()`

## Getting files from api 
- To return a file as a response in ur api import FileResponse  
`from fastapi.responses import FileResponse`
- Then pass in the path of the file to be returned to the FileResonse method

```py
from fastapi import FastAPI
from fastapi.responses import FileResponse

some_file_path = "large-video-file.mp4"
app = FastAPI()

@app.get("/")
async def main():
    return FileResponse(some_file_path)
```

## Background tasks
- Often we want to do some proccessing in the route handler but it would then block (like delay) the response of the route
- To run that task in the background we can just import `BackgroundTasks` from fastapi and it will automatically set up different threads for both the task and the response, magic isn't it ✨
```py
from fastapi import FastAPI, BackgroundTasks
from time import sleep

app = FastAPI()

def send_email(message):
    sleep(5)
    print('Sending email: ', message)

@app.get('/')
async def index(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, "Hello there.")
    return {'result' : 'success'}
```