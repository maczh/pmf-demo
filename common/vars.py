from pmf.core import app as PMFApp
class GlobalVars:
    app: PMFApp.App = None
    
    def __init__(self):
        self.app = None
    
    
global_vars = GlobalVars()
