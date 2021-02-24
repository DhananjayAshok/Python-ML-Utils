from time import perf_counter

class Profiler:
  def __init__(self, name=None, show=True):
      self.name = name
      self.show = show
      self.t = perf_counter()
  
  def step(self, msg=None):
      if not self.show:
        return
      interval = perf_counter() - self.t
      if msg is not None:
          to_print = f"{msg} | {interval}s"
          if self.name is not None:
              to_print = f"{self.name} | " + to_print
          print(f"{msg} | {interval}s")
      self.t = time.time()
      return
