import inspect
from .printManager import PrintManager

class ShapePrinter:
    def __init__(self, name="", show=True, limit=20, filename=None):
        self.name = name
        self.show = show
        self.limit = 20
        self.counter = 0
        self.printer = PrintManager(filename)
        
    def print(self, object, var_name):
        if not self.show:
            return
        shape = None
        details = inspect.getframeinfo(inspect.currentframe().f_back)
        meta_string = f"{details[0]}: line {details[1]}"
        try:
            shape = object.shape
        except:
            self.printer.print(f"Object {var_name} given to {self.name} at {meta_string} does not have a shape")
            return
        if self.counter < self.limit:
            self.printer.print(f"{self.name} | {var_name} | {meta_string} | {shape}")
            self.counter += 1
            return
        return 
        
