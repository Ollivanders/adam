# ADAM - Automated Documentation Add-on Maker

This project allows you to create contents of your README and other documentation files procedurally.
You may wish to do this for a few reasons:

- In really large files, the markdown can get excessively long and hard to manage
- There is shared content between multiple files e.g. introduction in README.md and INDEX.md
- Things such as the project structure and screenshots for the project should be updated on change. This allows use of hooks to keep documentation on github uptodate

## Contents

- [Quick start](#quick-start)
- [Browser Support](#browser-support)
- [To do](#to-do)
- [Join the community](#join-the-community)
- [License](#license)

## Quick start

an alias for you to run it from anywhere:
```
    alias docgen="python3 <(curl https://raw.githubusercontent.com/Ollivanders/adam/master/main.py)"
```

```
Usage: main.py [OPTIONS]

Options:
  --filename TEXT
  --docs-dir PATH
  --make-copy BOOLEAN
  --make-logo BOOLEAN
  -I, --ignore-dir-in-tree TEXT
  --example-docs BOOLEAN         regenerate example docs even if they exist
  --help                         Show this message and exit.
```

```
# in order to generate a test example to display its use
python3 main.py --filename testRead --docs-dir ./docsTest

# to see other options
python3 main.py 
```

### Additional features
Currently you need svn, this is to get the example docs directory. Fixed in the future.
```
brew install svn
```

To use the ascii logo generator you will need to install:
```
brew install figlet
```
<a href="https://formulae.brew.sh/formula/figlet"> figlet </a>

To use the automated project structure generation:
```
brew install tree
```
<a href="https://formulae.brew.sh/formula/tree"> tree </a>
## Browser Support

You can create a browser support section

| Landing page | Mobile |     |
| ------------ | ------ | --- |


<img src="./docs/images/screenshots/placeholder.png" href="https://google.com" height="256">&nbsp;&nbsp;&nbsp;<img src="./docs/images/screenshots/placeholder.png" href="https://google.com" height="256">

At present, we officially aim to support the last two versions of the following browsers:

<img src="./docs/images/browsers/chrome.png" width="64" height="64"> <img src="./docs/images/browsers/firefox.png" width="64" height="64"> <img src="./docs/images/browsers/safari.png" width="64" height="64">
<img src="./docs/images/browsers/edge.png" width="64" height="64"> <img src="./docs/images/browsers/opera.png" width="64" height="64">

## Project Structure

```.
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── docs
│   ├── contents.md
│   ├── images
│   │   ├── browsers
│   │   │   ├── chrome.png
│   │   │   ├── edge.png
│   │   │   ├── firefox.png
│   │   │   ├── opera.png
│   │   │   └── safari.png
│   │   └── screenshots
│   │       └── placeholder.png
│   ├── logo.txt
│   ├── project_structure.md
│   ├── sections
│   │   ├── acknowledgments.md
│   │   ├── browser_support.md
│   │   ├── introduction.md
│   │   ├── license.md
│   │   ├── quick_start.md
│   │   └── todo.md
│   └── sections_order.json
├── docsTest
│   ├── contents.md
│   ├── images
│   │   ├── browsers
│   │   │   ├── chrome.png
│   │   │   ├── edge.png
│   │   │   ├── firefox.png
│   │   │   ├── opera.png
│   │   │   └── safari.png
│   │   └── screenshots
│   │       └── placeholder.png
│   ├── project_structure.md
│   ├── sections
│   │   ├── acknowledgments.md
│   │   ├── browser_support.md
│   │   ├── introduction.md
│   │   ├── license.md
│   │   ├── quick_start.md
│   │   └── todo.md
│   └── sections_order.json
├── example_docs
│   ├── images
│   │   ├── browsers
│   │   │   ├── chrome.png
│   │   │   ├── edge.png
│   │   │   ├── firefox.png
│   │   │   ├── opera.png
│   │   │   └── safari.png
│   │   └── screenshots
│   │       └── placeholder.png
│   ├── sections
│   │   ├── acknowledgments.md
│   │   ├── browser_support.md
│   │   ├── introduction.md
│   │   ├── license.md
│   │   ├── quick_start.md
│   │   └── todo.md
│   └── sections_order.json
├── generate.sh
├── main.py
└── troubleshooting.md

15 directories, 50 files
```

# To do

With an ever morphing world, the number of potential contexts installation that could be called from increases as with the ambition of this collection.

- automated ascii art for top of project
- integration with automated screenshot capturing tools
- set templates for quick simple documentations e.g. react app, flask API, dotfile project etc.
- INDEX file design alterations and automation
- easier project structure management

## Done but still testing

- none of it, still in alpha phase

## Join the community

#### Sponsors & Backers

## Credits and Thanks

# License

MIT

