# Simple PDF merger
> CLI app for merging several pdf files

There many ways to merge pdf's, some of them payed and some of them free online, but you don't know what those online options do with your files. Here is a simple script to merge several pdf's using the CLI.
## Requirements
Python
PyPDF2

## USAGE
Just clone this repository in the folder where you have the files. Or just give the full path to the pdf files you want to merge. After the script name type the file names (paths). If not especified the output file is ```merge.pdf```
```bash
python mergepdf.py files_paths --output=file_path
```
### Default merge
It will take all pdfs in folder ```pdfs```and merge them into ```merged.pdf```
```bash
python mergepdf.py --merge
```
or 
```bash
python mergepdf.py -m
```

### Merge several files
```bash
python mergepdf.py merge --output=file_path
```

## EXAMPLE
```bash
python mergepdf.py document1.pdf document1.pdf --ouput=merged.pdf
```

## CODE
The core is taken from the [Real Python Tutorial](https://realpython.com/pdf-python/#how-to-merge-pdfs)
I just added the CLI part

## TODO
- [ ] Add merge pdf files in current folder