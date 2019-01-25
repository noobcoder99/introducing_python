# works in IDE demo of decorator assignment
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func_name_)
        print('Positioal arguments:',args)
        print('Keyword arguments:', kwargs)
        result = func(*args,**kwargs)
        print('Result:', result)
        return result
        return new_function
