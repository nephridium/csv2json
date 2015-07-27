import argparse, os
parser = argparse.ArgumentParser(
    description='Converts a CSV file to JSON',
    epilog='To avoid ambiguity put the list following flags -u, -n, -r and -a into quotes. ' +
           'Alternatively, supply infile (and optional outfile) before listing the flags.'
)
parser.add_argument("infile", default='data.csv', nargs='?', help='Input file name, default: data.csv')
parser.add_argument("outfile", nargs='?', help='Output file name, default: [infile_basename].json')
parser.add_argument('-S', '--separator', default=',', help='CSV separator used, default ","')
parser.add_argument('-H', '--headerline', type=int, default=0, help='Header line to use as column names')
parser.add_argument('-c', '--columns', type=int, help='Number of columns to crop to')
parser.add_argument('-u', '--usecols', nargs='+', help='List of names of columns to use')
parser.add_argument('-n', '--names', nargs='+', help='Column names to use')
parser.add_argument('-N', '--nrows', type=int, default=None, help='Number of rows to read')
parser.add_argument('-s', '--skiprows', type=int, default=None, help='Number of rows to skip before reading')
parser.add_argument('-r', '--userows', nargs='+', default=None, help='List of rows to use')
parser.add_argument('-a', '--append', nargs='+', help='Names of columns to append')
parser.add_argument('-p', '--printdata', action='store_true', help='Print formatted data when done')

args = parser.parse_args()

infile = args.infile
if not os.path.isfile(infile):
    print('File "%s" does not exist, aborting. Use --help to show command syntax and command line options.' % infile)
    exit()

outfile = args.outfile
if outfile is None:
    outfile = os.path.splitext(infile)[0] + '.json'

print("Converting %s -> %s [sep=%s, header=%s]" %
      (infile, outfile, args.separator, args.headerline))
if args.usecols is not None:
    print("Only using columns: %s" % (' '.join(args.usecols),))


import pandas as pd
if args.usecols is None:
    try:
        df = pd.read_csv(
            infile, sep=args.separator, header=args.headerline,
            nrows=args.nrows, skiprows=args.skiprows,
            engine='python'
        )
    except Exception:
        print('Could not read CSV data from "%s":\n' % infile)
        raise

else:
    try:
        df = pd.read_csv(
            infile, sep=args.separator, header=args.headerline,
            usecols=args.usecols,
            nrows=args.nrows, skiprows=args.skiprows,
            engine='python'
        )
    except Exception:
        print('Could not read CSV data from "%s":\n' % infile)
        raise

# crop columns
if args.columns:
    df = df[df.columns[:args.columns]]

# remove empty rows
df.dropna(how='all')

# only keep certain rows if given
if args.userows is not None:
    print("Only keeping rows: %s" % (' '.join(args.userows),))
    df = df[df.index.isin([int(row) for row in args.userows])]

# append columns if given
if args.append is not None:
    for additional_column in args.append:
        print('Adding column: %s' % additional_column)
        df[additional_column] = ''

# Change column names if given
if args.names is not None:
    df.columns = args.names

df.to_json(outfile, orient='records')

if args.printdata:
    print(df)
