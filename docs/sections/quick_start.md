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