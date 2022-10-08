import os


def safe_mkdir(path):
    if os.path.exists(path):
        return 1
    else:
        try:
            os.makedirs(path)
            return 0
        except:
            return -1


