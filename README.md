# ADAM - Automated Documentation Add-on Maker

This project allows you to create contents of your README and other documentation files procedurally.
You may wish to do this for a few reasons:

- In really large files, the markdown can get excessively long and hard to manage
- There is shared content between multiple files e.g. introduction in README.md and INDEX.md
- Things such as the project structure and screenshots for the project should be updated on change. This allows use of hooks to keep documentation on github uptodate

## Table Of Contents

- [Table Of Contents](#table-of-contents)
- [Quick start](#quickstart)
- [Browser Support](#browser-support)
- [Project Structure](#project-structure)
- [Join the community](#jointhecommunity)
- [License](#license)

## Quick start

- Copy the project and copy the contents of docs to your own.
- Alter the contents of sections to build up a README
- Use the docs/readme.sh file to specify the arrays to use in it

```
docs/generate.sh
```

## Browser Support

# Project Structure

```
.
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── docs
│   ├── contents.md
│   ├── generate.sh
│   ├── images
│   │   ├── browsers
│   │   │   ├── chrome.png
│   │   │   ├── edge.png
│   │   │   ├── firefox.png
│   │   │   ├── opera.png
│   │   │   └── safari.png
│   │   └── screenshots
│   ├── logo.txt
│   └── sections
│       ├── acknowledgments.md
│       ├── browser_support.md
│       ├── introduction.md
│       ├── license.md
│       ├── project_structure.md
│       ├── start.md
│       └── todo.md
└── troubleshooting.md

```

## Join the community

#### Sponsors & Backers

## Credits and Thanks

# License

MIT

