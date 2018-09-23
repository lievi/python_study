# Class Decorator
class Decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("Call method executed this before {}".format(
            self.original_function.__name__))
        return self.original_function(*args, **kwargs)


# Function Decorator
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before {}".format(
            original_function.__name__))
        result = original_function(*args, **kwargs)
        print("This run after")
        return result

    return wrapper_function


@Decorator_class
def display():
    print('display function ran')


@decorator_function
def display_info(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))


display_info('John', 22)
display()
