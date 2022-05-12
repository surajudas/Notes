# React notes

## Meta
- A library to build user interfaces
- has a rich package ecosystem hence is commonly thought of as a proper framework
- stuff like react-routing has to be installed seperatly
- Core philosohpy is reusable components and working together with markup and logic in the same place by using jsx (javascript syntax extension)

# Tips
- When passing integers or functions as props u have to wrap them inside `{}`
- Hmm use a global state when u need to pass this state to other components and component level states when only that component needs access to that state

## Installation
- Use the create-react-app package to well create your react apps as it simplifies many things out of the box
- 2 methods of installation: `npx create-react-app <app-name>` or `npm install -g create-react-app` and then `create-react-app <app-name>` in your desired directory
- Use the ES7 React/Redux/Graphql.. snippets extension to make ur life easier

## App component and JSX
- After doing create-react-app a directory structure and boilerplate files are created
  - The puclic folder contains the index.html and related files, these can be edited anyway you want
  - The src folder has the App.js and index.js files which are compiled to create the view basically (maybe)
  - Running `npm build` will create static files ready for deployment
- When returning jsx u can only return a single parent element
```js
function App() {
  return (
    <div className="App">
      <h1>Hello World</h1>
    </div>
  );
}
export default Header
``` 
this will work perfectly

```js
function App() {
  return (
    <div className="App">
      <h1>Hello World</h1>
    </div>
    <h1>Hi</h1>
  );
}
``` 
this will not

- `<>`, `</>` empty tags can be used as fragments ie. no parent tag if you dont want any
```js
function App() {
  return (
    <>
      <h1>Hello World</h1>
    </>
  );
}
``` 

# Components
## Creating a component
- Components for the ui of the app are created under `src/components/`
- The naming convention for them is to capitalise the first letter eg. `components/Headers.js`
- Type `rfce` to make a component with an arrow function and export boilerplate
- The import statement `import React from 'react'` in components is no longer needed in the current version of react
- The JSX Element is exported at the end of the component like `export default Header`
- The compnent is imported in the app via an import statement
```js
import Header from './components/Header'
```

## Passing Props
- Props are values that can be passed to the component for rendering onto the view via keyword arg style syntax

In App.js
```js
function App() {
  return (
    <div className="container">
      <Header title={'Hello world'}/>
    </div>
  );
}
```

- Inside the component, you can access the prop in 2 ways:
  - Taking the prop in the argument of the function and then using the `prop.attribute` inside the JSX segment
  - Destructuring the prop right there in the function argument and using them directly 

In Headers.js

### Destructuring way
```js
const Header = ({ title }) => {
  return (
    <header className='header'>
      <h1>{title}</h1>
    </header>
  )
}
```

### Prop way
```js
const Header = (props) => {
  return (
    <header className='header'>
      <h1>{props.title}</h1>
    </header>
  )
}

```

## Styling
- 3 ways: 
  - Css file
  - Style components package
  - direct css in js

### Direct css in js
- uses style tag in Jsx
- useful for dynamic styling
- Pass style attributes inside `{{attributename: 'somevalue'}}` 

In Header.js
```js
const Header = ({ title, bgColor }) => {
  return (
    <header className='header'>
      <h1 style={{color:'white', backgroundColor:bgColor}} >{title}</h1>
    </header>
  )
}
```

### Events Basics
- Events can be added to the component by passing in a function to the onClick(or other html events like onSubmit,etc) attribute of the JSX component
```js
const Header = () => {
    const onClick = ( e ) => {
    console.log('click')
  }

    return (
      <header className='btn'>
        <Button onClick={onClick} text = 'Hi'/>
      </header>
    )
}
```

## States
### Lists
- When we use something like map, filter or forEach to output some JSX its called a list.
- When using lists, the parent element in the JSX should have an unique identifier eg. id field in json
```js
// array of task objects
const tasks = [
      {
        "id": 1,
        "text": "Doctors Appointment",
        "day": "Feb 5th at 2:30pm",
        "reminder": true
      },
      {
        "id": 2,
        "text": "Meeting at School",
        "day": "Feb 6th at 1:30pm",
        "reminder": true
      }
    ]

const Tasks = () => {
    return (
        <>
          {tasks.map( (task) => (
              <h3 key={task.id}>{task.text}</h3>
          ))}  
        </>
    )
}
```

### Creating states
- The list in the above example is not a part of the state i.e it remains static relative to the rest of the app
- To make it a part of the state we need to use a `react hook` called `useState` by importing it:

```js
import { useState } from "react";
```

- The object you want to include in the state has to be then included in the JSX element, like so:

```js
//suppose we have component Tasks
const Tasks = () => {
  //then to create the state object
  const [<name of state object>, set<name of state object>] = useState(
    //<the state object>
  )
  return (
    <>
    <h1>hi</h1>
    </>
  )
}
```

- the setObject can be used to change the object on the run but by change we mean
- the state is recreated each time any change is made and the new state is sent up

### Global state
- Basically to manage all the state objects, they are kept in the main App and passed down to the various components as needed
- Events related to the state objects are to also be created in the global App which get passed down and the actions then that these events do are passed up to the state
- One example would be like: 
  - create an event to delete a task from the tasks object
    - this deleteTask event/function is created in the App and passed on to progressive component heirarchy
    - `deleteTask in App -> prop in Tasks component -> prop in Task component, prop passed to onClick of the concerned element`

# Conditional styling
- You can change the style of the ui on the fly by using ternary operators to set diff css classes for the elements
- This is made even more easier if you use something like tailwind or bulma

```js
<div className={`task ${task.reminder ? 'reminder' : ''}`}></div>
```

## Input forms
- The form in JSX is basically the same as in html, label followed by the input tag
- eg. of a simple input form

```js
const AddTask = () => {
    return (
        <form className='add-form'>
            <div className='form-control'>
                <label>Task</label>
                <input type='text' placeholder='Add Task' />
            </div>
            <div className='form-control'>
                <label>Day & time</label>
                <input type='date' placeholder='Add Day & Time' />
            </div>
            <div className='form-control form-control-check'>
                <label>Set Reminder</label>
                <input type='checkbox'/>
            </div>
            <input className='btn btn-block' type='submit' value='Submit'/>
        </form>
    )
}
```

- Each input tag has its own state
```js
const [task, setTask] = useState('')

const [date, setDate] = useState('')

const [reminder, setReminder] = useState(false)
```

- You then need to do 2 things:
  1. Set the value of the field to be that field's corresponding state's value eg. 

```js
const [task, setTask] = useState('')

<input type='text' placeholder='Add Task' value={task} />
```

  2. Set the value of the state of that field to be what the user types in that feild, which can be found by using the onChange event and then accessing the event's target value

```js
<input type='text' placeholder='Add Task' value={task} 
onChange={(e) => setTask(e.target.value)} />
```

- So its basically like: `value of field = value of field state = getting value from that field by accessing its event`


### Submitting the form
- first create a function in your global app (eg. onAdd) that adds the inputted form to your state by making the form into an compatible object
- this function is passed to the component that holds your form
- in the form first we make a function to mold the input into an object to pass to the onAdd functino and do some misc stuff like clearing the form
- then that new function is passed on to the onSubmit event
```js
// in App.js
const addTask = (task) => {
  let id = Math.floor(Math.random() * 100)
  setTasks([...tasks, {id, ...task}])
}

// in AddTask component
const onSubmit = (e) => {
        e.preventDefault()

        if (!text) {
            alert('Please enter a text')
        }

        onAdd({text, day, reminder})

        settext('')
        setday('')
        setReminder(false)
    }

// and
<form className='add-form' onSubmit={onSubmit}>
```

## Changing ui using states
### Toggling elements
- have a state variable that holds a boolean value indicating the visibility of the ui component
```js
const [toggleTasks, setToggleTasks] = useState(
    false
  )
```
- then its as simple as having an if loop to control the displaying of the component
```js
{toggleTasks && <AddTask onAdd={addTask}/>}
```
- finally you gotta pass the `setState` method to the component where button which should toggle this ui component resides **but** not directly, its easier to make an arrow function that contains the `setState` function
```js
// in App.js
<Header onAdd={() => setToggleTasks(!toggleTasks)} toggleTasks={toggleTasks}/>

// in Header.js
<Button text='Toggles component' onClick={onAdd} />
```
### Changing style
- Dynamic styling can again be used with state variables 
- you pass the state (which determines your style) to the component you want to control the style of
- one example
```js
// in a Header component
// toggleTasks is the state variable
<Button text={`${toggleTasks ? 'Close' : 'Add'}`} bgColor={`${toggleTasks ? 'tomato' : 'steelblue'}`} />
```

## Adding Static files to components
- Create a `assets` folder inside your src directory
- put your files in the assets folder
- import the files inside your js file
```js
import emoji from './assets/crying-svgrepo-com.svg'
```
- use them ~
```js
<img src={emoji} alt='spinning-crying-emoji' className='animate-spin inline w-5'/>
```

## Components with children
- In addition to the props that you can add to your components, React also creates certain props for your components automatically.
- One such prop is called children. When you render a component, the children prop will automatically be passed whatever content comes between the opening and closing tags for that component. This is helpful when you want to create a component that wraps some generic content.
- You can think of this concept in a frame and picture context, the frame is the main component and the picture its children prop.
  - this will be implemented as such
```js
// in frame.js
import React from 'react'

const Frame = ({ children }) => {
  return (
    <div>
      <h1>This is the page title</h1>
      { children }
    </div>
  )
}

export default Frame
```

```js
// in picture.js
import React from 'react'
import Frame from '../components/frame'

const GalleryPage = () => {
  return (
    <Frame>
      <img src='' />
    </Frame>
  )
}

export default GalleryPage
```

## Building for deployment
- `npm run build` creates a build version of your app in the `build/` directory
- To deploy it to web servers just push the build folder

### Deploying to github pages
1. Create an empty repo on github
2. install gh-pages as a dev dependency
`npm install gh-pages --save-dev`
3. In your package.json file add the following entry on the top level (not part of any other node)
`"homepage": "https://{username}.github.io/{repo-name}"`
4. In the existing scripts property, add a predeploy property and a deploy property, each having the values shown below:
```js
"scripts": {
  //...
  "predeploy": "npm run build",
  "deploy": "gh-pages -d build"
}
```
5. Initialise the git repo ala `git init` 
6. Add your remote `git remote add origin <https://link to repo>`
7. Build your app (`npm run deploy`), the extra stuff like creating a gh-pages branch, commiting the changes to gh-pages,.. are automatically done by the package
8. You can then commit your source code normally to the master branch `add -> commmit -> push origin master`

> Note: Don't create a repo in your react app before depoloying with the gh-pages package otherwise it creates permission errors.