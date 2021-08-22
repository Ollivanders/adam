## Quick start

- Copy the project and copy the contents of docs to your own.
- Alter the contents of sections to build up a README
- Use the docs/readme.sh file to specify the arrays to use in it

```
# in order to generate a test example to display its use
python3 main.py --filename testRead --docs-dir ./docsTest

# to see other options
python3 main.py 
```

### Additional features

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