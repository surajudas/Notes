# Justpy notes 
Mostly code snippets
- [Justpy notes](#justpy-notes)
  - [Components Cheatsheet](#components-cheatsheet)
  - [Tips and tricks](#tips-and-tricks)
  - [Basic Page with p tag](#basic-page-with-p-tag)
  - [Advanced use of elements and styling](#advanced-use-of-elements-and-styling)
  - [Event Handling](#event-handling)
    - [Basic Event](#basic-event)
    - [Additional Event Properties](#additional-event-properties)
    - [Multiple events](#multiple-events)
    - [Sharing Events](#sharing-events)
    - [Routes](#routes)
    - [Parsing html and making corresponding justpy commands](#parsing-html-and-making-corresponding-justpy-commands)
    - [Auto-reload on code change](#auto-reload-on-code-change)
    - [Asyncio in justpy](#asyncio-in-justpy)
    - [Apis in justpy](#apis-in-justpy)
    - [Static Files](#static-files)

## Components Cheatsheet
Component | Attributes 
----------|------------
General | a=`<page>/<parent component>`: adds the element to the page/parent element, style=`inline-style`, classes=Class of the element (used with tailwindcss) 
Events | click, mouseenter, mouseleave
jp.WebPage | head_html: gives access to the head tag, to add link tags, css: main stylesheet
jp.P | text: the text that will be shown  
jp.Div | text
jp.Button | text, message, num_clicked

## Tips and tricks 
- Its easy to add custom fonts and link css frameworks:
  - First disable tailwindcss in justpy.env 
    - Add this line: `TAILWIND = False`
  - In the head tag we link the style sheets or any fonts we want or we can use the @import function in css to do the same
```python
wp.head_html = '<link href="https://unpkg.com/nes.css@2.3.0/css/nes.min.css" rel="stylesheet" />'
wp.css = '@import url(https://fonts.googleapis.com/css?family=Press+Start+2P);'
```
- When just want to use a div to center an element just make the div in the element difinition instead of making a variable like `jp.Img(src="somepath",a=jp.Div(classes="flex justify-center",a=wp))`

## Basic Page with p tag
- Components in justpy are classes and their objects/instances, elements for eg. justpy.P is the component and its object the element
- The WebPage handles a get request from the user
- Functions that retutrn the webpage are called 'request handlers' and there has to be one to render the page using the justpy()
```python
import justpy as jp
# Create a request handler
def handler():
    # Inside the handler 
    # Instantiate the webpage
    wp = jp.WebPage()

    # Create a paragraph element and add it to the webpage
    p = jp.P(text="\'Sup", a=wp)
    
    # return the webpage
    return wp
jp.justpy(handler)    
```

## Advanced use of elements and styling 
- We use the delete_flag=False argument when we don't want to create a new page for each new request
- the style argument is used as an inline style
- we can also use the classes argument to set the class of the element and use tailwindcss to create nice lookin components 
> Note: class is a reserved word so classes is used instead to pass in class
> Info: When you define a page that is going to be rendered in more than one browser tab or page, you need to set its `delete_flag` to `False`.
```python
import justpy as jp

page = jp.WebPage(delete_flag=False)
for i in range(1, 11):
    p = jp.P(
        text=f"{i})Hello World!",
        a=page,
        style=f"color: rgb(18, 68, 102); font-size: {10*i}px",
    )  

def hello():
    return page

jp.justpy(hello)
```

## Event Handling
### Basic Event
- Here the on method links the event "click" to the event handler my_click
- self in the my_click event handler is a refrence to the object that the event happens on
- msg is dictionary of information about the event taking place
- These 2 arguments must always be passed when creating an event handler
- Here the text attribute of Button d is changed from 'Not clicked yet' to 'I was clicked' by using self.text
```python
import justpy as jp

def my_click(self, msg):
    self.text = "I was clicked"
    print(msg["event_type"])
    print(msg)


def event_demo():
    wp = jp.WebPage()
    d = jp.Button(
        text="Not clicked yet", a=wp, classes="text-xl m-2 p-2 bg-blue-500 text-white"
    )
    d.on("click", my_click)
    return wp


jp.justpy(event_demo)

# Output
"""click
{'event_type': 'click', 'id': 1, 'class_name': 'Button', 'html_tag': 'button', 'vue_type': 'html_component', 'event_target': '1', 'value': '', 
'page_id': 0, 'websocket_id': 0, 'event_current_target': '1', 'session_id': '75fb07c9e27f45aebad938d6f1805091', 'msg_type': 'event', 
'page': WebPage(page_id: 0, number of components: 1, reload interval: None), 'websocket': <starlette.websockets.WebSocket object at 0x000002856D44FF70>, 
'target': Button(id: 1, html_tag: button, vue_type: html_component, name: No name, number of components: 0)}"""
```
### Additional Event Properties
JustPy does not pass all the JavaScript event properties by default since in most cases they are not needed. If you need additional properties from the JavasScript event, use the additional_properties attribute. In the example below, more fields are added to msg.
```python
import justpy as jp

def my_click(self, msg):
    print(msg)
    self.text = 'I was clicked'

def event_demo():
    wp = jp.WebPage()
    wp.debug = True
    d = jp.Div(text='Not clicked yet', a=wp, classes='w-48 text-xl m-2 p-1 bg-blue-500 text-white')
    d.on('click', my_click)
    d.additional_properties =['screenX', 'pageY','altKey','which','movementX','button', 'buttons']
    return wp

jp.justpy(event_demo)
```
### Multiple events
The same element can handle multiple events
```python
import justpy as jp

def my_click(self, msg):
    self.text = 'I was clicked'
    self.set_class('bg-blue-500')

def my_mouseenter(self, msg):
    self.text = 'Mouse entered'
    self.set_class('bg-red-500')

def my_mouseleave(self, msg):
    self.text = 'Mouse left'
    self.set_class('bg-teal-500')

def event_demo():
    wp = jp.WebPage()
    d = jp.Div(text='Not clicked yet', a=wp, classes='w-64 text-2xl m-2 p-2 bg-blue-500 text-white',
             click=my_click, mouseenter=my_mouseenter, mouseleave=my_mouseleave)
    return wp

jp.justpy(event_demo)
```
- In the example above, there are three event handlers, one each for the `click`,`mouseenter` and `mouseleave` events. All three are bound to the same element, `d`
- Instead of using the on method, you can bind an event handler using a keyword argument that corresponds to the name of the event.
- The above example also introduces the `set_class` method. This method "knows" which Tailwind classes logically cannot apply together (for example, text color can't be both red and blue at the same time) and removes the appropriate classes while adding the class provided as parameter. In the case above, the background can only be one color so the `set_class` method removes the class bg-blue-500 and adds the class bg-red-500.

### Sharing Events
- In the eg below a single event is shared among many buttons
- 
```python
import justpy as jp

def button_click(self, msg):
    self.num_clicked += 1
    self.message.text = f'{self.text} clicked. Number of clicks: {self.num_clicked}'
    for button in msg.page.button_list:
        button.set_class('bg-blue-500')
        button.set_class('bg-blue-700', 'hover')    
    self.set_class('bg-red-500')
    self.set_class('bg-red-700', 'hover')

def event_demo():
    number_of_buttons = 33
    wp = jp.WebPage()
    button_div = jp.Div(classes='flex m-4 flex-wrap', a=wp)
    button_classes = 'w-32 mr-2 mb-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full'
    message = jp.Div(text='No button clicked yet', classes='text-2xl border m-4 p-2', a=wp)
    button_list = []
    for i in range(1, number_of_buttons + 1):
        b = jp.Button(text=f'Button {i}', a=button_div, classes=button_classes, click=button_click)
        b.message = message
        b.num_clicked = 0
        button_list.append(b)
    wp.button_list = button_list
    print(button_div)
    return wp 

jp.justpy(event_demo)
"""Output: Div(id: None, html_tag: div, vue_type: html_component, name: No name, number of components: 33)"""
```
We can assign any element of the page as an attribute to access it in an event handler?
I just can't go through the rest of the docs at this moment so I'll do it gradually when I need that functionality and learn about it, right now I'll go and try to make something, organisation later

### Routes 
- Routes are set like in most other frameworks like flask using a decorator
>Note:Routed paths must start with '/'
```python
@jp.SetRoute('/hello')
def hello_function():
    wp = jp.WebPage()
    wp.add(jp.P(text='Hello there!', classes='text-5xl m-2'))
    return wp

@jp.SetRoute('/bye')
def bye_function():
    wp = jp.WebPage()
    wp.add(jp.P(text='Goodbye!', classes='text-5xl m-2'))
    return wp
jp.justpy()
```

### Parsing html and making corresponding justpy commands
We use parse_html to easily convert this to JustPy commands.   
This component is based on this [example](https://tailwindcss.com/components/alerts/#top-accent-border) from the Tailwind documentation.  
Run the following program. As it does not start a web server, there is no need to load a web page. We will be interested only in the printout.
```python
import justpy as jp

# Example based on https://tailwindcss.com/components/alerts/#top-accent-border
html_string = """
<div class="bg-teal-100 border-t-4 border-teal-500 rounded-b text-teal-900 px-4 py-3 shadow-md" role="alert">
  <div class="flex">
    <div class="py-1">
    <svg class="fill-current h-6 w-6 text-teal-500 mr-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
    <path d="M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 17.07zm12.73-1.41A8 8 0 1 0 4.34 4.34a8 8 0 0 0 11.32 11.32zM9 11V9h2v6H9v-4zm0-6h2v2H9V5z"/></svg>
    </div>
    <div>
      <p class="font-bold">Our privacy policy has changed</p>
      <p class="text-sm">Make sure you know how these changes affect you.</p>
    </div>
  </div>
</div>
"""

d = jp.parse_html(html_string)
for c in d.commands:
    print(c)
```

The printout is the following:
```py
root = jp.Div(name='root')
c1 = jp.Div(classes='bg-teal-100 border-t-4 border-teal-500 rounded-b text-teal-900 px-4 py-3 shadow-md', role='alert', a=root)
c2 = jp.Div(classes='flex', a=c1)
c3 = jp.Div(classes='py-1', a=c2)
c4 = jp.Svg(classes='fill-current h-6 w-6 text-teal-500 mr-4', xmlns='http://www.w3.org/2000/svg', viewBox='0 0 20 20', a=c3)
c5 = jp.Path(d='M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 17.07zm12.73-1.41A8 8 0 1 0 4.34 4.34a8 8 0 0 0 11.32 11.32zM9 11V9h2v6H9v-4zm0-6h2v2H9V5z', a=c4)
c6 = jp.Div(a=c2)
c7 = jp.P(classes='font-bold', a=c6, text='Our privacy policy has changed')
c8 = jp.P(classes='text-sm', a=c6, text='Make sure you know how these changes affect you.')
```

These are the JustPy commands required to duplicate the elements defined in the HTML. We are now are ready to define our 
component. We will call it MyAlert.
```py
import justpy as jp

class MyAlert(jp.Div):

    def __init__(self, **kwargs):
        self.title_text = 'This is the title'
        self.body_text = 'This is the body'
        super().__init__(**kwargs) # Important! see below
        root = self
        c1 = jp.Div(classes='bg-teal-100 border-t-4 border-teal-500 rounded-b text-teal-900 px-4 py-3 shadow-md',
                    role='alert', a=root)
        c2 = jp.Div(classes='flex', a=c1)
        c3 = jp.Div(classes='py-1', a=c2)
        c4 = jp.Svg(classes='fill-current h-6 w-6 text-teal-500 mr-4', xmlns='http://www.w3.org/2000/svg',
                    viewBox='0 0 20 20', a=c3)
        c5 = jp.Path(
            d='M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 17.07zm12.73-1.41A8 8 0 1 0 4.34 4.34a8 8 0 0 0 11.32 11.32zM9 11V9h2v6H9v-4zm0-6h2v2H9V5z',
            a=c4)
        c6 = jp.Div(a=c2)
        c7 = jp.P(classes='font-bold text-lg', a=c6, text=self.title_text)
        c8 = jp.P(classes='text-sm', a=c6, text=self.body_text)

def alert_test():
    wp = jp.WebPage()
    d = MyAlert(a=wp, classes='m-2 w-1/4', title_text='hello', body_text='How is everybody?')
    d.title_text = 'Shalom'
    return wp

jp.justpy(alert_test)
```

Alternativly you can use the html blob as is and set it as the inner_html argument of the component which is **less of a pain** to do 
```py
#Footer component 
class Footer(jp.Footer):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.inner_html = """
        <footer class="mt-52 md:mt-20 footer">
            <div class="flex flex-col items-center">
                <p class="mt-3 text-sm text-grey-500 font-bold">©2020 Suraj Das</p>
            </div>
        </footer>"""
```        

### Auto-reload on code change
This can be done pretty easily by just adding 2 lines of code where you normally start the server
```py
app = jp.app
jp.justpy(index, start_server=False)
```
Then when starting the server use this command instead:
```
uvicorn --reload <Python file's name>:app
```
> Remember to cd into that directory first

### Asyncio in justpy
JustPy uses starlette.io, "a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services". To shield users from the complexities of async programming in Python, JustPy allows both functions that handle requests and functions that handle events to be either async or not. The framework checks if a function is a coroutine and runs it accordingly.  

When a request or event handler require I/O operations over the internet (or to access a local database or even file), it is recommended that they be of type async and that all I/O and database operations be non-blocking (this means they are run as a coroutine or in another thread). Otherwise, the application will not scale. 
```py
async def get_image(self, msg):
    r = await jp.get(f'https://dog.ceo/api/breed/{msg.page.breed}/images/random')
    self.src = r['message']
```
> Note: A async function has to await something ie. file operation, I/O event, etc  

### Apis in justpy
To help with the simple case of using an API with the HTTP GET method, JustPy provides a helper function   conveniently called get. The function asynchronously retrieves information which (by default in JSON format) and converts it to a Python dictionary.
```py
r = await jp.get(f'https://dog.ceo/api/breed/{breed}/images/random')
img_url = r['message']
```

### Static Files
- Static resources are those that are not generated dynamically by the application. An image is an example of a static resource.
- By default, all static resources for JustPy can be found under the /static route

```py
import justpy as jp

def static_test():
    wp = jp.WebPage()
    jp.Img(src='/static/papillon.jpg', a=wp, classes='m-2 p-2')
    return wp

jp.justpy(static_test)
```

- You should see the picture on the web page.
- If you enter the URL http://127.0.0.1:8000/static/papillon.jpg you will get the picture also.
- If want to keep your static resources in a separate directory, the simplest thing to do is to create a subdirectory in the directory your program is in. If you call the directory "my_pictures" for example, and put the image there, you would need to set the src attribute of the image to "/static/my_pictures/papillon.jpg".  
The line in the code would look like this:`jp.Img(src='/static/my_pictures/papillon.jpg', a=wp, classes='m-2 p-2')`

