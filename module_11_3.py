import inspect
from pprint import pprint
def introspection_info(obj):
    #print(type(obj))
    intro_dict = {}
    intro_dict['type'] = type(obj)
    intro_dict['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    intro_dict['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    intro_dict['module'] = inspect.getmodule(obj)
    intro_dict['isinstance'] = isinstance(obj, int)

    return intro_dict



number_info = introspection_info(42)
pprint(number_info)
