from time import perf_counter
from .printManager import PrintManager

class Profiler:
  def __init__(self, name=None, show=True, filename=None):
      self.name = name
      self.show = show
      self.printer = PrintManager(filename)
      self.t = perf_counter()
  
  def step(self, msg=None):
      if not self.show:
        return
      interval = perf_counter() - self.t
      if msg is not None:
          to_print = f"{msg} | {interval}s"
          if self.name is not None:
              to_print = f"{self.name} | " + to_print
          self.printer.print(to_print)
      self.t = perf_counter()
      return
