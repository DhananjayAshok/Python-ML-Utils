import inspect
from .printManager import PrintManager


class Printer:
    def __init__(self, name="", show_meta=True, limit=-1, filename=None):
        self.name = name
        self.show_meta = show_meta
        self.limit = limit
        self.counter = 0
        self.printer = PrintManager(filename)

    def can_print(self):
        return self.counter < self.limit or self.limit < 0

    def _get_meta_string(self, details):
        if self.show_meta:
            return f"{details[0]}: line {details[1]}"
        else:
            return ""
    
    def print(self, msg):
        if self.can_print():
            self.printer.print(msg)
            self.counter += 1
        return
    
    def print_shape(self, obj, var_name):
        shape = None
        details = inspect.getframeinfo(inspect.currentframe().f_back)
        meta_string = self._get_meta_string(details)
        try:
            shape = obj.shape
        except:
            self.printer.print(f"Object {var_name} given to {self.name} at {meta_string} does not have a shape")
            return None
        self.print(f"{self.name} | {var_name} | {meta_string} | {shape}")
        return shape
    
    def print_mean_std_min_max(self, obj, var_name):
        details = inspect.getframeinfo(inspect.currentframe().f_back)
        meta_string = self._get_meta_string(details)
        m, s = None, None
        try:
            m = obj.mean()
            s = obj.std()
            mi = obj.min()
            ma = obj.max()
        except:
            self.printer.print(f"Object {var_name} given to {self.name} at {meta_string} does not have a "
                               f"mean, std, min or max")
            return None
        self.print(f"{self.name} | {var_name} | {meta_string} | mean: {m} std: {s} min: {mi} max: {ma}")
        return m, s, mi, ma
    
    def print_has_nans(self, obj, var_name, always_print=False):
        details = inspect.getframeinfo(inspect.currentframe().f_back)
        meta_string = self._get_meta_string(details)
        has_nans = None
        try:
            has_nans = obj.isnan().any()
        except:
            self.printer.print(f"Object {var_name} given to {self.name} at {meta_string} "
                               f"either does not have an isnan() or it's isnan() does not have any()")
            return None
        if has_nans or always_print:
            self.print(f"{self.name} | {var_name} | {meta_string} | has nans: {has_nans}")
        return has_nans

    def print_equal(self, a, b, mean_epsilon=0.001, max_epsilon=0.001, verbose=True):
        """

        Checks if MSE(a, b) is near 0 (both the max and mean of each entry wise comparison)
        a and b must be tensor or vector types i.e they must have a mean and a max operation as well as a - b possible
        """
        details = inspect.getframeinfo(inspect.currentframe().f_back)
        meta_string = self._get_meta_string(details)
        try:
            diff = (a - b) ** 2
            mean_condition = diff.mean() < mean_epsilon
            max_condition = diff.max() < max_epsilon
        except:
            self.printer.print(f"Objects given to {self.name} at {meta_string} "
                               f"either do not have an mean and max or (a-b)**2 failed")
            return
        if mean_condition and max_condition:
            if verbose:
                self.print(f"{self.name} | {meta_string} | True")
            return True
        else:
            if verbose:
                if not mean_condition:
                    self.print(f"{self.name} | {meta_string} | "
                               f"False: mean of (a-b)**2 is {diff.mean()} >= {mean_epsilon}")
                if not max_condition:
                    self.print(f"{self.name} | {meta_string} | False: max of (a-b)**2 is {diff.max()} >= {max_epsilon}")
            return False
