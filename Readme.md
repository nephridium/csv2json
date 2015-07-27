```
usage: json2csv.py [-h] [-S SEPARATOR] [-i] [-I INDEXLABEL]
                   [-u USECOLS [USECOLS ...]] [-n NAMES [NAMES ...]]
                   [-a APPEND [APPEND ...]] [-p]
                   [infile] [outfile]

Converts a JSON file to CSV

positional arguments:
  infile                Input file name, default: data.json
  outfile               Output file name, default: [infile_basename].csv

optional arguments:
  -h, --help            show this help message and exit
  -S SEPARATOR, --separator SEPARATOR
                        CSV separator used, default ","
  -i, --index           Write row names (index)
  -I INDEXLABEL, --indexlabel INDEXLABEL
                        Label for index column
  -u USECOLS [USECOLS ...], --usecols USECOLS [USECOLS ...]
                        List of names of columns to use
  -n NAMES [NAMES ...], --names NAMES [NAMES ...]
                        Column names to use
  -a APPEND [APPEND ...], --append APPEND [APPEND ...]
                        Names of columns to append
  -p, --printdata       Print formatted data when done

To avoid ambiguity put the list following flags -u, -n, and -a into quotes.
Alternatively, supply infile (and optional outfile) before listing the flags.
```

```
usage: csv2json.py [-h] [-S SEPARATOR] [-H HEADERLINE] [-c COLUMNS]
                   [-u USECOLS [USECOLS ...]] [-n NAMES [NAMES ...]]
                   [-N NROWS] [-s SKIPROWS] [-r USEROWS [USEROWS ...]]
                   [-a APPEND [APPEND ...]] [-p]
                   [infile] [outfile]

Converts a CSV file to JSON

positional arguments:
  infile                Input file name, default: data.csv
  outfile               Output file name, default: [infile_basename].json

optional arguments:
  -h, --help            show this help message and exit
  -S SEPARATOR, --separator SEPARATOR
                        CSV separator used, default ","
  -H HEADERLINE, --headerline HEADERLINE
                        Header line to use as column names
  -c COLUMNS, --columns COLUMNS
                        Number of columns to crop to
  -u USECOLS [USECOLS ...], --usecols USECOLS [USECOLS ...]
                        List of names of columns to use
  -n NAMES [NAMES ...], --names NAMES [NAMES ...]
                        Column names to use
  -N NROWS, --nrows NROWS
                        Number of rows to read
  -s SKIPROWS, --skiprows SKIPROWS
                        Number of rows to skip before reading
  -r USEROWS [USEROWS ...], --userows USEROWS [USEROWS ...]
                        List of rows to use
  -a APPEND [APPEND ...], --append APPEND [APPEND ...]
                        Names of columns to append
  -p, --printdata       Print formatted data when done

To avoid ambiguity put the list following flags -u, -n, -r and -a into quotes.
Alternatively, supply infile (and optional outfile) before listing the flags.
```
