# RegEx Notes

## Tips from u/nickcernis
- Use https://regexr.com/. You can paste an expression at the top, mouse over each highlighted section, and it will explain what that part does. It's a great way to decipher hieroglyphics into something you can start to understand.
- Complete https://regexone.com/. It's a great interactive introduction to regular expressions that should fill any gaps in your knowledge. You have to fill in the regex that satisfies the named matches.
- Complete https://regexcrossword.com/. It's a “reverse regex” crossword web game where you have to type the string that satisfies the expressions in all of the row and column headers. (See https://regexcrossword.com/howtoplay.)
- Look at common regex patterns and try to understand them. Paste some from https://projects.lukehaas.me/regexhub/ into regexr.com and hover over each group in the regex to help figure out anything you're not familiar with. Start with the shortest examples that you don't yet understand.

### An Introduction
- ReGex is a tool to extract information from text (code, log files, documents,..)
- Everything is a character and we write expressions to match a specific pattern of characters (aka a string)
- Characters include both ascii and unicode
- regex returns every string that has common character given by my query, for eg in: abcdefg, abcde, abc | abc matches all three
- When writing regex its best to be as concise in your expression as possible so that no false positives come up. They call it a `tight` expression.

### The 123s 
- 