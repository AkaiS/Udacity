Lesson0 = [
["HTML", "HTML stands for HyperText Markup Language. It is the foundation of all web pages and allows for all web design and implimentation of images, videos, links, etc."],
["Hyperlinks/Links","Hyperlinks (commonly referred to as links) connects the web. Links are paths to other pages or specific parts of a page.", '<a href="www.website.com">What is visible</a>'], 
["Tags", "Tags help change generic text in HTML documents.Tags can be used to create links, bold or italicize words, seperate certain instances of text so they can receive a style and much more. Tags outline elements. Some tags require to be closed while void tags, which are used for images and break, do not.Tags can also have attributes which change the way the tag functions."],
["Elements", "Elements are what HTML documents are made of. They are seperated by tags."],
["Inline vs Block", "Elements in HTML can be either inline or block. If they are block thereis an invisible box around the element."]
]

Lesson1 = [
["HTML vs CSS", "HTML is the basic structure and the content of a web page. CSS is the style in which the HTML is presented."],
["CSS", "CSS, also known as Cascading Style Sheets, controls font, size, border, position, margins, orientation and much more."],
["Document Object Model", "Document Object Model or DOM is a cross platform convention for language. Things are ordered in a tree like structure to represent how elements interact with each other. This method of organization bears strong resemblance to a family tree with branches having the ability to inherit traits."],
["Boxes", "Every element in an HTML file is represented by boxes. Text, boxes. Images, boxes. Circles, boxes. HTML makes the boxes. CSS is used to mix, match and even overlap these boxes in creating a web page."]
]

Lesson2 = [
["Adding Style", "Style is added to an HTML page through a CSS page. Use a period before classes (.note, .sectiontitle) a hashtag/pound sign before ids (#pageheader) and nothing prior to tags (p, div). Weave them together such as h.sectionheader to change the style on a specific part of a class."],
["CSS - Inheritance", "Inheritance is the process with which nested elements recieve style because they are part of an overarching element. For example you can make all the text in an html file appear as a certain font and then change the size of the font for each individual tag, class or id. Inheritance allows for less code and repetition."],
["Margin, Border, Padding, Content", "Every element has multiple layers which make up the total element. There is the content which could be a video, text, image, etc. Then there is the padding which expands the box and inherits color of the box/content background color. The border surrounds the padding and also inherits the background color. However the color and design can be changed causing a definitive border. The margin is the space an element requires before running into another element. This helps seperate elements."],
["Box-Sizing: Border-Box", "Browser specific prefixs may be necessary for this newer technique. Using border-box lets you set the size of the whole box in either percentage or pixels. This includes the border, padding and content."],
["Flexbox", "Flexbox is a tool used to position boxes. Flexbox allows for boxes to be position next to each other rather than just in a list format. Apply display:flex and change the size percentage of the box to allow for boxes to position next to each other.", "display: flex"],
["Images", "Store an image in a place that the HTML document can access it (folder for images in the website folder). In case the image has trouble loading add an alt attribute.", '<img src="folder/name" alt="random">'],
["Devtools", "DevTools can be used to tweak a page to get an idea of what you may want to permanently change on a page. After any tweaks you can simply refresh the page to have the page return to its original form."],
["Repetition", "One of the biggest parts of coding is avoiding repetitive code. That is why CSS, classes and other such things exist. CSS allows you to style large chunks of code all at once. Likewise, classes allow you to style multiple sections of code that are of that class. There are a lot of things you can do to reduce the amount written and to streamline your code."]
]

Lesson3 = [
["Programs", "Programs are anything that tell a computer what to do; how complicated or simple it is does not matter. Web pages, games and operating systems are all examples of programs."],
["High Level Languages", "High level languages exist as a non ambigious language platform. Spoken languages such as English are far too ambigious to tell a computer what to do. As stated prior, computers will only do what they are told so code can not be ambigious. This is in both the way the syntax is, and how it is used. Expressions such as 2 + 2 + will end up causing an error as it is not a proper expression."],
["Expressions", 'Code is made up of expressions which are the "grammatical" foundation of the language, similiar to sentences. Can be as simple as 2 + 2 or much more complicated like ((123 * 526) + 231) - 326 and beyond. Structure will not always be numeric.'],
["Limits of Computers", "Computers are inherently limited by the speed that data can be moved. Data can be moved at a speed close to light and because of this hard limit computers have been getting smaller. The smaller the computer the less distance the data must travel allowing for quicker computations."]
]

Lesson4 = [
["Variables", "Variables are one of the main concepts in programming. With an assignment operator you can give a variable (letters or words) a value. That value is then stored and can be used or modified. Variables are used to clarify code and store data."],
["Assignment Operator", "Unlike in typical arithmetic, the equal sign (=) is used as an assignment operator in python and other programming languages. It is used to give a variable a value.", "variable = expression"],
["Strings", "Strings are characters surrounded by single or double quotations. They can be stored in variables. Anything within the quotations will not be read as an expression."],
["Concatenation", 'Concatenation is the method of joining strings. "This is " + "an example." Will concatenate into "This is an example." Take care to realize when you are concatenating or adding as the symbol is the same and the process is determined by whether numbers or strings are used.', "string + string == stringstring"],
["Indexing", "Indexing is the method with which to give strings a numeric reference. You can index a string or a variable that is storing a string. The first character in a string is at the 0 position. Using [n:x] you can specify a section of a string that you would like to retrieve. [n:] Takes everything starting at n. [:n] Takes everything for n. [:] Takes the whole string. [n:x] Starts at n and takes up to, but not including, x. Indexing can also start from the back of the string with negative numbers starting at -1.", '"index"[0] == i'],
["Find", "Find compares a given set of characters to a string. If it finds the set of charcters in the string it will give you the position of the first character. If it does not find anything it will return -1. At x is what find will look for in the string and n is the position at which it will start looking. You can find with a string or a variable.", "string.find(x,n)"]
]

Lesson5 = [
["Functions", "Functions or procedures are code that receives an input, works with it and then returns an output. You call a function with an input. Functions can be called multiple times meaning you can code something then use it repeatedly, helping eliminate repetition and simply code.", "def functionname(parameters)"],
["Making vs Using a Function", "Functions must be defined. In this definition the function is coded to perform a task. However just creating a function does not actually fulfill the task. You must use the function, normally with an input, so that the function executes and performs the task."],
["Importance of Return", 'Without return a function may do nothing at all. It can execute addition in a sum function but then by never returning the value, it "forgets" the changed value and for the program it is like the function was never called. Functions can do things such as print but to save a value it must be returned.']
]

Lesson6 = [
["Making Decisions", """Python has a number of operands used to return a boolean datatype of True or False. There are many different types of comparison such as:
	> greater than,
    >= greater than or equal to,
    < less than,
    <= less than or equal to,
    == equal to,
    != is not equal to.
There are also logical structures such as and, or and not that can be used in comparisons."""],
["If-else", "If or if-else statements execute code if a condition is met. In an if else code will also be executed if the if statement is False."],
["While loops", "Unlike if statement which will only execute 0 or 1 times, while loops execute as long as the condition is True. This means that if the condition does not change to False, the loop will continue forever. While loops can also be stopped by a break input."],
["Debugging", "Making mistakes in code is something that happens to everyone. One of the most important skills to have is to be a good debugger. This means figuring out what is wrong with code and solving. This often happens by breaking up and seeing what each part of the code does. However, sometimes when correcting code your code will become less correct that the original. It is important to keep variations of code even after figuring out a variant that works."]
]

Lesson7 = [
["Lists", "Lists are one of the most powerful storage containers in Python. They are a mutable structure that can hold things like variables, numbers, strings and even other lists. Individual aspects of a list can be changed while not becoming a new, copied list."],
["Index", "Indexing in lists grabs the position of an element in a list. You can using slicing with these indexes to grab certain items in a list."],
["Mutation vs Copied", "While lists can be mutated they can also be copied and will be with certain functions. When concatenating two lists a new list is created to hold the elements. Changing specific values at certain indexes or using a function such as .append mutates the list into holding new or more elements."],
["Finding Length", "To find the length of an element such as a string or list the 'len' function is used. It will return the number of items in a list or characters in a string."],
["In", "The function 'in' is used in a boolean fashion. If x can be found in y, True will be returned. Otherwise it will return False. This can be used to find a certain word in a long string or a certain element in a list."],
["Devensive Programming", "Defensive programming is the practice of desigining code so that it can deal with circumstances that were unintended and allows for the program to continue running instead of crashing."],
["Problem Solving", "Problem solving is a vital process to coding. When trying to figure out how to code or deal with a problem, you need to break it down into several steps. Figure out the input and the output. Write some pseudocode to get an idea of how to structure the code. Then you pick the foundation of the code and begin. After every part extensive testing should be done to ensure the code functions as intended."]
]

Lesson8 = [
["Abstraction", "Abstraction is the way of dealing with complex code. It is a technique to only deal with the relevant portions of computer code. This is most relevant when you import modules. You may not know the exact code and way that the modules function, but as long as you know what the module returns and can do, you can use it."],
["Documentation", "Modules and code often have documentation. This documentation lists all the functions in a module you can use as well as what they all do. With documentation you can get an abstract idea of how a module works and then use it without reading the actual code."],
["Classes", "Classes are the bread and butter of object oriented programming. To create an object of a certain class gives it access to specific parameters and functions. Object oriented programming revolves around having objects to manipulate and classes give a way to impress the same parameters on multiple objects."],
["__init__", "To initialize an instance of a class you use __init__. Initializing sets the instance variables for that instance of a class and sets aside a space in memory for the new object."],
["Instance", "An instance is a single occurance of a class. Instance variables are variables only occuring in an instance and instance methods are only in instances as well."],
["Self", "While technically could be called something else, it is the term used to refer to the instance of the class being called, while inside of the class definition."],
["Class Variables", "Class Variables are variables that will remain the same accross all instances of that class. For example if class for something like car, may always have 4 wheels."],
["Inheritance", "Classes can be inherited. This means they get the variables and methods of another class. If you inherit from a class you can utilize their methods or you can override them by simply rewriting the method in the new class."],
["Object Oriented Programming", "Object Oriented Programming or OOP, is a programming paradigm that revolves around manipulating objects and data. Objects can have their own data and procedures and classes can provide a 'definition' that can be impressed upon multiple objects allowing them to share data and procedures. OOP is often quite easy to understand as it can easily correlate with real world objects. Thinking about something like a board game can be easy to lay the foundation for as you can create objects for a card, a die, the gameboard or whatever else the game may need. For bigger projects OOP can be quite advantagous because of the flexability of objects and classes. To give an example I might have a hundred different circles and want to be able to draw all of them with turtle. Instead of writing a function to draw a circle for each circle thats data I might have, I could write a single function and associate it with the circle class, allowing any circle object to print itself with turtle. Regardless of how many circle objects there may be, I could always change the definition of the circle class to change the behavior of all of the circle objects. I could also change individual circle objects and they could still be usable in whatever code they may appear in."],
["Object", "An object can be anything from a variable to a function to an instance of a class as it is a location in memory that has an id and a value."],
["Method", "A method is a function that is nested in an object. It typically changes the parameters of that object. Methods can be used in conjunction with classes to give ever instance a class certain methods. Those methods are not absolute however as a new class that is inheriting from another class can 'override' existing methods. This means that when called the new class can create a method with a name that was previously defined and change how that method functions."],
["Modules", "Modules are a collection of functions that share a purpose. A commonly used module in Python is the datetime module. This module has functions to get current date and time, compare two different times, work with individual parts of the date and time (like hours or days) and several others. Modules in general are the greatest example of abstraction because the way they work isn't explained but what each module will return and how to use it is."],
["Library", "Python already comes with a library and it is called the python standard library which is a collection of modules that covers all of your basic needs. However for more complicated tasks people often need to create their own tools and modules. That collection of tools or modules ends up being a library."],
["Connections to Abstraction", "The create a movie trailer website is an excellent example of abstraction. I know what I would receive when I created the movie class data but I didn't know how the python backend worked. Luckily, it wasn't necessary (yet) for me to understand how the page ended up rendering as long as I understood what it would render. For me coding in any language utilizes abstraction because of a lack of understanding of how the code compiles to interact with a computer."]
]

Lesson9 = [
["Network", "A network is a the connection of entities via indirect connections. This means that rather than communicating directly with a person like one would do with a walkie talkie, information gets bounced from place to place until it arrives at the ended target."],
["Latency", "Latency is the time it takes information to bounce from the source, to the destination and then back to the source. On the internet this time is typically measured with milliseconds."],
["Bandwidth", "While latency describes how fast you get information back, bandwidth describes how much information can be sent at a time. You can have a slow response time and a high bandwidth though they normally come fairly hand in hand."],
["Protocols", "Protocols are the way that a client communicates with a server. Protocols help insure that information is sent correctly and consistently while sending information in a format that is easier for a server to process."],
["Absolute vs Relative Paths", "An absolute path is the full URL and path to get to a web page such as www.udacity.com. Relative paths similar to what we use to point to a stylesheet or script. The full path doesn't need to be written, just the relative one from the index of a program of webpage."],
["Form", "The form tag is used to represent a section of HTML that allows for user input. With the action parameter you can describe which part of the backend you would like to access while the method parameter can send a GET or POST request."],
["Input and Label", "In HTML the way to get interactive user information is with the void tag input. Input tags can have different types like submit, checkbox, password, text and radio. Inputs can be named and described using the label tag. When radio buttons have the same name a value can be applied to the input to differentiate inputs."]
]

Lesson10 = [
["Dictionaries", "Dictionaries are unordered sets of values that are labeled with a key. Keys allow very quick access and unlike lists there is not need to iterate over a large body of data to get information. The keys in a dictionary are immutable while the value is any mutable value such as lists, strings, variables or even other dictionaries."],
["GET vs POST", "A GET request is primarily used to fetch information from a server. There is a maximum URL length, they are good to cache and shouldn't be used to change the server. POST on the otherhand has no maximum length and can't be cached, but the main difference is that it is perfect to update the server. Basically, GET to look at a page and POST to have someone add to it."],
["Validation", "When ever you receive information you should validate it to check that it matches the data you are trying to receieve.  The example presented was when getting a date you would want to check that what was inputted was actually a date. This would mean checking that the year is a valid number and possible year while month and days would have to be in certain ranges. Validation helps prevent getting strange, nonfitting information which could cause big problems when you are getting information from hundreds or more people."],
["Escaping", "Another extremely important thing to do to any user input is to escape it. Proper escaping filters any input your website receives and removes or substitutes anything that may interfere with the working of your code. An example of this are the fairly common autoescape functions which take thing like <b> and transform it into &ltb&gt which helps prevent inserting working code into any text input your site may have."],
["Templates", "One of the keys to good programming is the avoidance of repetition and templates are a tool to do just that. Templates allow you to avoid repetition by being a form with which you can plug in data. The form can be used as many times as a user would like and it allows you to do things like only write the html for a header and footer once and then just have every individual page extend that base page. On top of this, templates help improve clarity. You want to avoid have html in a python page and templates help seperate the two."],
["Jinja2", "Jinja2 is a template library that comes with Google App Engine. Template libraries allow for code such as python in HTML templates."],
["Template Inheritance", "Template inheritance is what allows templates to extend other existing templates such as a header and footer template."]
]

Lesson11 = [
["Databases", "Databases are programs, a machine or even a group of machines that work by storing and retrieving data."],
["Tables", "Data in databases are stored in tables. Every entry takes up a row of the table and the columns make of the attributes of those entries."],
["Named Tuples", "Named tuples are commonly used in databases. The difference between a named tuple and an ordinary tuple is that you can call named values from the tuple using dot notation and can reference all tuples of a certain name. These both make them very useful in databases."],
["SQL", "SQL or Structured Query Language, is a system of querying that has been around since the 1970's. Though there are different database structures like MySQL and Oracle, many databases share SQL as a there primary language."],
["Indexing Databases", "Sequential scans when dealing with thousands of entries can be very slow. Instead, indexing allows for very quick access by allowing you to call an entry by it's reference rather than scanning through the entire database."],
["ACID", "ACID is an acronym for things good database transactions should strive for. Atomicity, all parts of a transaction succeed or fail together, no partial commands and all parts should update. Consistency, database should always be consistent. Isolation, no transaction should interfere with others and all computations should be seperate. Durability, once a transaction occurs, it won't be lost. You can't do all of these perfectly and there will be tradeoffs."]
]

Lesson12 = [
["Truthy and Falsy", "Truthy is a term used to refer to anything that would count as being true. This includes True, non-zero numbers, 'strings', objects, arrays and functions. Falsy is opposite and refers to False, 0, ''(empty strings), undefined, null and NaN (not a number)."],
["JSON", "JSON stands for JavaScript Object Notation and is a method of structuring javascript. It helps not only when reading javascript but also allows for linters which are advanced error checkers. It is easy to make mistakes and obvious mistakes can be picked up by most text editors. However, a JSON linter will check for all errors in a particular structure and will make sure that it functions properly. As an add on, never evalute JSON. It can run a program that could cause serious harm."],
["API", "An API is how you communicate with other programs on the internet. XML is one example of the possible language used and it is stricter than HTML. Attempting to parse HTML can lead to a lot of errors as HTML can still function with large errors."],
["Saving Queries", "Queries can be saved and this is helpful in reducing program run time. Repeating repeating queries when you just need the same data as before is unnecessary so saving the data can save time."],
["Recursion", "Recursion is an important concept in the field of algorithms. Recursive algorithms work towards a base case and make recursive calls until reaching that case."],
["Parellel Computing", "Parellel Computing is process of splitting up tasks so that instead of doing a then b you do a and b at the same time."]
]

note = [Lesson0, Lesson1, Lesson2, Lesson3, Lesson4, Lesson5, Lesson6, Lesson7, Lesson8, Lesson9, Lesson10, Lesson11, Lesson12]