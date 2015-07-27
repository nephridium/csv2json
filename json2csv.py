import argparse, os
parser = argparse.ArgumentParser(
    description='Converts a JSON file to CSV',
    epilog='To avoid ambiguity put the list following flags -u, -n, and -a into quotes. ' +
           'Alternatively, supply infile (and optional outfile) before listing the flags.'
)
parser.add_argument("infile", default='data.json', nargs='?', help='Input file name, default: data.json')
parser.add_argument("outfile", nargs='?', help='Output file name, default: [infile_basename].csv')
parser.add_argument('-S', '--separator', default=',', help='CSV separator used, default ","')
parser.add_argument('-i', '--index', action='store_true', help='Write row names (index)')
parser.add_argument('-I', '--indexlabel', help='Label for index column')
parser.add_argument('-u', '--usecols', nargs='+', help='List of names of columns to use')
parser.add_argument('-n', '--names', nargs='+', help='Column names to use')
parser.add_argument('-a', '--append', nargs='+', help='Names of columns to append')
parser.add_argument('-p', '--printdata', action='store_true', help='Print formatted data when done')

args = parser.parse_args()

infile = args.infile
if not os.path.isfile(infile):
    print('File "%s" does not exist, aborting. Use --help to show command syntax and command line options.' % infile)
    exit()

outfile = args.outfile
if outfile is None:
    outfile = os.path.splitext(infile)[0] + '.csv'

print("Converting %s -> %s [sep=%s]" %
      (infile, outfile, args.separator))
if args.usecols is not None:
    print("Only using columns: %s" % (' '.join(args.usecols),))


import pandas as pd
try:
    df = pd.read_json(infile)
except ValueError:
    print('Could not read JSON data from "%s":\n' % infile)
    raise

# Append columns if given
if args.append is not None:
    for additional_column in args.append:
        print('Adding column: %s' % additional_column)
        df[additional_column] = ''

# Change column names if given
if args.names is not None:
    df.columns = args.names

# Convert
if args.usecols is None:
    df.to_csv(outfile, index=args.index, index_label=args.indexlabel, sep=args.separator)
else:
    df.to_csv(outfile, index=args.index, index_label=args.indexlabel, sep=args.separator, columns=args.usecols)

if args.printdata:
    print(df)
