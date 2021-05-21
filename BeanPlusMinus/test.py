class WatchNode:
  def __init__(self,count, tok):
    self.count = count
    self.tok = tok



def main():
    global globalVariable 
    globalVariable = WatchNode(10,4)


if __name__ == "__main__":
    main()
    
globalVariable = None
print(globalVariable.tok)