#
# Parallel corpus language-ID based filter
#

import argparse


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  #parser.add_argument('file', help="file to read")
  #parser.add_argument('-c','--column',help="project a specific column", type=int)
  #parser.add_argument('-n','--number',help="output top N features", type=int)
  #parser.add_argument('-v','--value',help="output the value used for ranking", action="store_true")
  #parser.add_argument('-p','--printfeat',help="print the actual feature (default is to print repr)", action="store_true")
  #parser.add_argument('--output', "-o", default=sys.stdout, type=argparse.FileType('w'), help = "write to OUTPUT")
  args = parser.parse_args()