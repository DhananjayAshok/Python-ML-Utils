
class PrintManager:
      def __init__(self, filename=None):
          self.filename = filename
          
      def file_write(self, msg):
          with open(self.filename, "a+") as f:
              f.write(msg)
          return
      
      def print(self, msg):
          if self.filename is not None:
              return self.file_write(msg + "\n")
          else:
              print(f"{msg}")
          return
