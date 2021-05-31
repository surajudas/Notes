# Tailwind quick reference notes
Tailwind is a low level css framework that allows for modular design.  
Everything on the page is styled using small components provided by the framework instead of providing premade stuff which allows for a lot of flexibility. 

### Tailwind tips
- Use `text-center` to center some text in that tag/container
- The responsive breakpoints `sm:,md:,lg:` act at that screen size and above so any property without this selector will act at all screensizes below specified selector if any

## Fonts & Colors

## Postioning 
Utilities for controlling how an element is positioned in the DOM.
Default class reference
Class|Properties
-----|----------
static | position: static;
fixed | position: fixed;
absolute | position: absolute;
relative | position: relative;
sticky | position: sticky;

- Most tailwind websites use the sticky property to [sticky](https://tailwindcss.com/docs/position#sticky) the nav and footer to one position 