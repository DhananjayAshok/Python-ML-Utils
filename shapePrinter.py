import inspect

class ShapePrinter:
    def __init__(self, name="", show=True, limit=20):
        self.name = name
        self.show = show
        self.limit = 20
        self.counter = 0
        
    def print(self, object, var_name):
        if not self.show:
            return
        shape = None
        line = inspect.get_frame_info()[1]
        try:
            shape = object.shape
        except:
            print(f"Object {var_name} given to {self.name} at line {line} does not have a shape"
            return
        if self.counter < self.limit:
            print(f"{self.name} | {var_name} | {line} | {shape}")
            self.counter += 1
            return
        return 
        