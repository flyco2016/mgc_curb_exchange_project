class _const:
    class ConstError(TypeError):
        pass
    
    class ConstCaseError(ConstError):
        pass
    
    def __setattr__(self, name, value):
            if (name in self.__dict__.keys()):
                raise self.ConstError("Can't change const {name}".format(name=name))
            if not name.isupper():
                raise self.ConstCaseError("const name {name} is not all uppercase".format(name=name))
            self.__dict__[name] = value

import sys

sys.modules[__name__] = _const()