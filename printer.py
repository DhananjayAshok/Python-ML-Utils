import inspect
from .printManager import PrintManager


class Printer:
    def __init__(self, name="", show=True, limit=-1, filename=None):
        self.name = name
        self.show = show
        self.limit = limit
        self.counter = 0
        self.printer = PrintManager(filename)

    def can_print(self):
        return self.counter < self.limit or self.limit < 0 
    
    def print(self, msg):
        if self.can_print():
            self.printer.print(msg)
            self.counter += 1
        return
    
    def print_shape(self, obj, var_name):
        if not self.show:
            return
        shape = None
        details = inspect.getframeinfo(inspect.currentframe().f_back)
        meta_string = f"{details[0]}: line {details[1]}"
        try:
            shape = obj.shape
        except:
            self.printer.print(f"Object {var_name} given to {self.name} at {meta_string} does not have a shape")
            return
        self.print(f"{self.name} | {var_name} | {meta_string} | {shape}")
        return
    
    def print_mean_std_min_max(self, obj, var_name):
        details = inspect.getframeinfo(inspect.currentframe().f_back)
        meta_string = f"{details[0]}: line {details[1]}"
        m, s = None, None
        try:
            m = obj.mean()
            s = obj.std()
            mi = obj.min()
            ma = obj.max()
        except:
            self.printer.print(f"Object {var_name} given to {self.name} at {meta_string} does not have a "
                               f"mean, std, min or max")
            return
        self.print(f"{self.name} | {var_name} | {meta_string} | mean: {m} std: {s} min: {mi} max: {ma}")
        return
    
    def print_has_nans(self, obj, var_name, always_print=False):
        details = inspect.getframeinfo(inspect.currentframe().f_back)
        meta_string = f"{details[0]}: line {details[1]}"
        has_nans = None
        try:
            has_nans = obj.isnan().any()
        except:
            self.printer.print(f"Object {var_name} given to {self.name} at {meta_string} "
                               f"either does not have an isnan() or it's isnan() does not have any()")
            return
        if has_nans or always_print:
            self.print(f"{self.name} | {var_name} | {meta_string} | has nans: {has_nans}")
        return
