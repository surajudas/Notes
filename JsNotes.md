# Javascript Notes
to learn: 
- [ ] dom manip
- [ ] async
- [ ] api stuff
- [ ] React

- Things to learn before a framework
  - Javascript Fundamental
  - Module
  - Classe
  - Arrow function
  - Promises / Asynchronus request
  - Destructurin
  - Concept of components & stat
  - Spread operator
  - High order array functions

## Intro
- Javascript is a dynamic lang that runs on both browsers(Spidermonkey and v8) and also outside the browser in the node runtime environment
- Standardised by ECMA and standard is called ECMAscript

## Bestpractices
- If your writing js in the html file itself then write it in the bottom most part of the body tag, that way the html content is loaded first and the script proccessed after that plus we actually need some elements to work(manip) with first.
- Use Camel notation to name identifiers eg. firstName
- Whenever in doubt use [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

## Basics
- all **statements** need to be terminated by `;` in js
- Except statements ending with blocks:
```js
function foo() {
// ...
}
if (y >0) {
// ···
}
```
- Code without semicolons is legal but not preferred
- comment is made by using `//`

## Operators 
### Comparison operators
- a == b : Loose equality (doesn't check types) 
- a != b : loose inequality
- a === b : strict equality (checks for same type)
- a !== b : strict inequality
- a < b / a > b / a >= b / a <= b : greater than and less than
> Note: There's no strict greater than/ less than operator

### Logical Operators
- expr1 && expr2 : And operator
- expr1 || expr2 : Or operator
- !expr : Not operator	

### Variables
- Define a variable using the `let` keyword
```js
let x;
console.log(x);

let y = 2;
y = 'hi'
console.log(y);
``` 
- This will print undefined and hi in the console
- Variables can be undefined in js and be defined later in the code
- Identifier names can't start with a number and -

### Constants
- Constants as their names suggest are variables that have a fixed value and can't be reassigned
```js
const pi = 3.1459;
console.log(pi);
```

## Data types
- Primitives | Reference types

### Primitives
- string, number, bool(true/false), undefined, null
```js
let name = 'Suraj'; //string
let age = 69; //number
let feelingGood = true; //bool
let purposeInLife; //undefined
let energyMeter = null; //null
```

- the type of an object can be checked by using `typeof object` eg. `typeof name => string`

#### String Properties and Methods
- string.length => returns the length of the string
- string.slice(start, end)
- string.replace(toReplace, newString) => The replace() method replaces a specified value with another value in a string
```js
let text = "Please visit Mcdonalds";
let newText = text.replace("Mcdonalds", "Dominos");
```
- string.toUpperCase() and string.toLowerCase()
- string.trim() => trims off leading and ending whitespaces
- The isNaN() function determines whether a value is NaN or not. The argument is converted to number first so be careful of that
```js
let ex1 = '123';
let ex2 = 'def not a number';

function checkIfNum(x) {if(isNaN(x)) {
    console.log('Hey this is not a number');
} else {
    console.log('this is number');
}}

checkIfNum(ex1);
checkIfNum(ex2);
```

#### Template Strings
```js
let name = 'Gandumon';
let age = 1649;
console.log(`${name} is turning ${age} this year`);
``` 

### Reference types
- objects, arrays, functions

### Objects
- A JavaScript object is a collection of named values that have properties and methods to them
- They are declared inside `{}`
- Everything in js is an object except primitives

```js
let person = {firstName:'Suraj', lastName:'Das', age:69};
``` 

- The properties of an object can be accessed in 2 ways :- dot notation or squre bracket notation
- Use the dot notation in most cases as its more concise and compact and the square notation can be used when we don't know what property we are going to access in advanced (like when user selects a property)
- Note json is based on js objects and can be converted to and fro but keep in mind keys and strings must be in double quotes only (no single quotes allowed)
- To convert from object to json pass in the array of objects inside `JSON.stringify()`

```js
let person = {firstName:'Suraj', socialPoints:-90000};
// dot notation
person.socialPoints -= 42000;
person.judgement = "Labor Camp"; // will create a new property of judgement

// square bracket
let summary = person["firstName"] + ' will be given ' + person["judgement"];
let selection = 'firstName'; // user selects a property
person[selection] = 'Kalia';

//Converting to json
personJSON = JSON.stringify(person)
console.log(personJSON)
// in json format
/* person = {
    "firstName":"Suraj",
    "socialPoints":-90000
}
*/
```

## Equality comparisons and sameness
### Strict equality using `===`
- Returns true if the operands are equal and of the same type.
- Strict equality is almost always the correct comparison operation to use.

### Loose equality using `==`
- Loose equality compares two values for equality after converting both values to a common type.
- undefined and null are loosely equal; that is, undefined == null is true, and null == undefined is true.

```js
if (1=='1') {
    console.log("1=='1'")
}

if (1==='1') {
    console.log("1==='1'")
}
/* Output
1=='1'
*/
```

### Arrays
- Arrays in js are dynamic in size and type of elements it can hold
- Its is made using `[]`
- An element can be accessed by its index, array[i]

```js
let favThings = ['blue', 'manga', 2];
favThings[0] = 'turqoise blue';
favThings[2] = [180, 360];
```
- Arrays are objects and hence have properties and methods to them
```js
console.log(favThings.length)
```

## Loops
### For loop
- Loops in js are a bit like in c/c++ I think
```js
for(initial value; condition till which the loop will iterate; increment) {
    statement;
}
```
```js
for(i = 0 ; i < 69; i++) {
  console.log(`loops are weird in js times ${i}`);
}
```

### While Loop
- While loop only takes in the condition till which to iterate
- remember to increment the initial value tho otherwise it will go on infinitly
```js
i = 0; 
while(i < 10) {
    console.log(i);
    i++
}
```

## Higher Order Array methods
- forEach, map, filter

### forEach 
- It is better to use this array method to iterate/traverse through an array than simply using a for/while loop
- The forEach method is called on the array and a callback function needs to be passed as the argument. This callback function handles/operates upon the incoming elements from the array.
- Multiple parameters can be passed to the callback fn but the first parameter must be the one that represents the incoming elements from the array
```js
const letters = ['r', 's', 't'];

letters.forEach( function(letter) {
    console.log(letter);
});
```

### Map
- Map returns the elements of an array
```js
let mappedLs = letters.map( function(letter) {
    return letter;
});
```

### Filter
- Filters and returns elements of an array according to a condition
```js
const letters = ['r', 's', 't', 3];

let filteredLs = letters.filter( function(letter) {
    return typeof(letter) == 'number';
});
console.log(filteredLs)
// output:- Array [ 3 ]
```

## Conditionals 
### If, else if, else
- If conditional can be nested in this order:- if (condition) {do}-> else if (condition) {do} -> else {do}
```js
let person = {firstName:'Suraj', socialPoints:-90000};
if (person.socialPoints < 0) {
    console.log("To the gulag you go 👿");
} else if (person.socialPoints >= 1000) {
    console.log("Keep up the good work citizen");
} else {
    console.log("Welcome to the mainland citizen")
}
```

### Ternary operator
- Shorthand if statement
- Used a lot to assign variables based on a condition
```js
let scoialScore = 200;
// ternary operator
let judge = (socialScore < 0) ? 'John Xina' : 'Randee Ortan'

console.log(judge)
// Randee Ortan
```
- let `variable` = `if condition` `?`(then) `value1` `:`(or) `value2`

### Switch
- Evaluates a variable or statement and has corresponding cases, if a case is true then its body is executed. A default case has to be there.
```js
let judge = (person.socialPoints < 0) ? 'John Xina' : 'Randee Ortan'

// Switches
switch(judge) {
    case 'John Xina':
        console.log('Why cant anybody see me?');
        break;
    default:
        console.log('Unga Bunga');
        break;
}
```

## Functions
- A piece of code that can be called multiple times from code. May or may not return a value
```js
function add5(num=9) {
    return num + 5;
}
// default value is 9 if no value is given
console.log(add5()); // 14
console.log(add5(12)); // 17
```

### Arrow functions
- Arrow functions are a handy way to write one liner functions.
```js
const addNums = (num1 ,num2) => num1 + num2
console.log(addNums(1, 3)) 
```

## OOP with js

## Function Constructors
- This is the outdated way to make classes (ES5)
- The identifier always start with a **capital letter**
- The variables that are needed to instantiate a class are passed as parameters to the function constructor
- The Classes' attributes can be defined by using the `this.<attribute>` keyword 
- The methods of the class can be defined both inside the function constructor or outside by using the objects'         `prototype` property
```js
// function constructor
function Person(firstName, lastName, dob, hobbies) {
    this.name = {'first':firstName, 
    'last':lastName
    };
    this.dob = new Date(dob); // year, month, date
    this.hobbies = hobbies;
}
Person.prototype.daysToLive = function () {
    return 80 - (2021 - this.dob.getFullYear());
}

let person1 = new Person('Kala', 'Kawua', '2001, 2, 4', ['singing', 'wrestling'])
console.log(`you have ${person1.daysToLive()} years to live`)
```

### Classes
- Classes were introduced in ES6 and work in the same way as many other languages
- a class is defined by the `class` keyword, the main syntax is something like:
```js
class nameOfTheClass {
    constructor(parameters, a, b, c,..) {
        this.attribute1 = a;
        this.attribute2 = [b, c];
        .
        .
    }
    someMethod(params) {
        do something;
    }
} 
example = nameOfTheClass(a, b, c,..)
example.someMethod(params)
```
- The constructor method of the class holds the attributes of the class
- Methods for the class can be defined in the class itself
- Example:
```js
// class
class Person{
    constructor (firstName, lastName, dob, hobbies){
        this.name = {'first':firstName, 
        'last':lastName
        };
        this.dob = new Date(dob); // year, month, date
        this.hobbies = hobbies;
    }
    daysToLive() {
        return 80 - (2021 - this.dob.getFullYear());
    }
    fullName() {
        return `${this.name.first} ${this.name.last}`
    }
}
```

>Note: The methods of the class are added to the prototype property of the class automatically

## The DOM
### The window
- A global variable, `window`, representing the window in which the script is running, is exposed to JavaScript code.
- In a tabbed browser, each tab is represented by its own Window object; the global window seen by JavaScript code running within a given tab always represents the tab in which the code is running.
- The window object provides methods and properties that should be globally available to js

### Selectors
- To select elements from the document we need to call the singls/multiple selector methdos on the `document` object
- Single selector methods:
  - `document.getElementById()`: gets html element by its id
  - `document.querySelector()`: gets any single html element that matches search query. Pretty similar to jquery.
- Multiple selector methods:
  - `document.getElementsByClassName()`: Returns a html collection object of all elements with the given class, the object has to be converted to an array before using array methods on tho.
  - `document.querySelectorAll()`: Returns a node list of all matching elements, you can use array methods on it without any conversion.
```js
const listItems = document.querySelectorAll('.item');
listItems.forEach((item) => console.log(item.textContent))
```
>Note: Use `querySelector` & `querySelectorAll` most of the time

### Doom Manip
- Various methods can be called on the selected document elements
- Examples:

```js
const list = document.querySelector('.items'); // selecting a ul list
list.remove(); // removes the whole list
list.firstElementChild.textContent = 'HEHEHEHHEHEHE'; // changes the text of the first element child of the list
list.children[1].textContent = 'Muhauhauhua'; // first gotta get a node list of all the children of the ul list then access any property of that child
list.lastElementChild.innerHTML = '<a href="https://www.example.com">clikity clak</a>'

const btn = document.querySelector('.btn');
btn.style.background = 'blue'; // changing the color of the btn to be blue
```
- You can use `document.createElement('<name of the tag>')` to create elements out of nowhere

### Events
- Events are fired to notify code of "interesting changes" that may affect code execution. These can arise from user interactions such as using a mouse or resizing a window, changes in the state of the underlying environment (e.g. low battery or media events from the operating system), and other causes. (from mdn docs)
- You add an event listener to the element you want to observe and give it to things: the type of event to look out for and a callback function
- The callback function's first parameter will be the event paratmeter often denoted by `e`. `e` is an object that has properties and methods pretaining to the element that is being observed
- there are many diff event types and can be found in the mdn docs
```js
const btn = document.querySelector('.btn');
btn.addEventListener('click', (e) => {
    e.preventDefault(); // prevents default form submit behaviour
    body = document.querySelector('body')
    body.classList.add('bg-dark')
})
```

# NPM basics
Npm is 'the' package manager that comes installed with nodejs, similar to gems in ruby and pip in python

## The package.json file
- It is a manifest file that holds info related to the project such as its name, author, version, etc. But the most imp thing it holds is the dependencies that the project uses.
- You can also create npm scripts in your package.json file
- It can be really easily created with `npm init` which will start a input dailouge and generate the json file at the end. 
- This dialouge can be skipped by adding the `-y` or `--yes` flag to the command, like `npm init -y`. Now all the default options will be selected and no time is wasted.
  - The default options of npm can be set by running `npm set <property-name>`, eg: `npm set package-author-name suraj` and `npm set package-license MIT`
  - To see what are the current defaults use `npm get <property-name>`
- The `'main'` object in the package file indicates which js file is the main js file in the project.

## Installing a module
- These days locally installed modules are automatically added to the package.json file.
- To install a specific version use `npm install <package>@version` eg. `npm install lodash@17.4.3`
- The installed module can then be used in your js files using 2 methods: 
  - Using the `require` method and assigning the imported module to a variable
    - Eg. `const _ = require('lodash')` here `_` is the name of the variables that points to the object imported, and can be anything u wan, in lodash's case the convention is to use `_`.
    - Then any method the module has can be called like normal eg. `_.each(numbersArray, (number) => console.log(number))`
  - The other way is to use the import statement at the top of your main js file
```js
import beeper from 'beeper';

await beeper();
// beep one time

await beeper(3);
// beep three times

await beeper('****-*-*');
// beep, beep, beep, beep, pause, beep, pause, beep
```

### Dev dependencies
- These modules are used mainly in the development process and normally not needed for production
- Basically stuff that helps out in the development by compiling something or automating some things, etc
- like for example gulp, gh-pages,...
- They are specified by the `-dev` flag
- The installed dev dependencies are added in the package file under `devDependencies` key
- You can choose not to install the dev dependencies when you are setting up someone else's project by doing `npm install --production`

## Uninstallign dependencies
- Alisases: `npm uninstall <package>`, `npm remove <package>`, `npm rm <package>`
- to remove local packages use `npm rm <package>`, to remove dev ones use `npm rm <package> -dev`, for global ones `npm rm <package> -g`

## Updating packages
- use `npm update <package>`

## Global modules
- They can be installed by using the `-g` flag eg. `npm install nodemon -g`
- Since its installed globally the installed module is not going to show up in the package.json file
- The install location of the global modules can be checked with `npm root -g`

## List modules
- Use `npm list --depth 0`

## Npm Scripts
- Alias kinda commands can be added to the project by adding them under the `scripts` key
- Some special scripts include `start`, `test` and some others
  - The start script is useful since even in diff projects the npm start command stays the same and even if you rename your main js file the start command is the same.
  - Platforms like heroku look for your start script to run your project
  - It can hold anything like `'start': 'node index.js'` or `'start': 'live-server'`
- Other scripts need to when used in the command line need to be used with `npm run` command.
  - Eg. under `'scripts'`: `'dev'`: `'live-server'`

### Misc stuff
- `setTimeout(<function>, <time>)` - executes given funciton after given time in miliseconds
- I seem to forget about making the variables actually variables by declaring them with let and const, this is likely a habit from using python so much.
- The `onfocus` property can be set to run a function when a specific element is in focus
```js
let input = document.querySelector('input');

input.onblur = inputBlur;
input.onfocus = inputFocus;

function inputBlur() {
  input.value = 'Focus has been lost';
}

function inputFocus() {
  input.value = 'Focus is here';
}
```


### Examples
1. Simple form
```js
const loginForm = document.querySelector('#my-form');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const msg = document.querySelector('.msg');
const users = document.querySelector('#users');

loginForm.addEventListener('submit', submitfn);

function submitfn(e) {
    e.preventDefault();
    if (nameInput.value === '' || emailInput.value === '') {
        msg.classList.add('error');
        msg.innerHTML = 'Enter your name and email!';

        setTimeout(() => msg.remove(), 3000);
    } else {
        const li = document.createElement('li');
        li.appendChild(document.createTextNode(`${nameInput.value} : ${emailInput.value}`));
        users.appendChild(li);
    }
}
```

2. ReGex can be used in js by simply creating a regex object and then using this objects' methods. A regex object can be created in 2 ways: 
    - `let re = \vanilla\d\`
    - `let re = new RegExp('^[0-9%^*()=+\/.-]*$');`

3. Whitespaces can be blocked in input boxes like so:
```js
// Stopping the use of space and tab keys
    var k = event ? event.which : window.event.keyCode;
    if (k == 32) return false;
```