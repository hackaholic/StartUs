import sys
import collections


def openFile(filename):
  try:
    f = open(filename, "r")
    return f
  except Exception as e:
    print(e)
    usage()
    sys.exit(1)

def ipRequestCount(filename):
  f = openFile(filename)
  my_dict = collections.defaultdict(int)
  for line in f:
    my_dict[line.split(" ", 1)[0]] += 1
  f.close()

  return sorted(my_dict.items(), key=lambda x: x[-1], reverse=True)

def display(count, k=10):
  print("{:<20}{}".format("IP Address", "Count"))
  for i,x in enumerate(count):
    if i<k:
      print("{:<20}{}".format(x[0], x[1]))
    else: break

def usage():
  myStr = """
  Usage: python3 ipRequestCount.py filename <top_n>
  exmple: python3 ipRequestCount.py access.log 10
  """
  print(myStr)

def main():
  if len(sys.argv) > 1:
    count = ipRequestCount(sys.argv[1])
    if len(sys.argv) == 3: display(count, int(sys.argv[2]))
    else: display(count)
  else:
    print("Please Provide the access.log")
    usage()

if __name__ == "__main__":
  main()
