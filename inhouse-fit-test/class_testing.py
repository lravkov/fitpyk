# Define a function that adds two numbers
def add(x, y, z):
    return x + y + z


# Define a class that allows the add() function to be used with different argument names
class Adder:
    def __init__(self, x, y_name, z_name):
        self.y_name = y_name
        self.z_name = z_name

    def __call__(self, x, **kwargs):
        y = kwargs.get(self.y_name, 0)
        z = kwargs.get(self.z_name, 0)
        return add(x, y, z)


if __name__ == '__main__':
    x_val = 2

    # Create an Adder instance with argument names 'a' and 'b'
    my_adder = Adder(x_val, 'a', 'b')

    # Call the Adder instance like a function with arguments 'a' and 'b'
    result = my_adder(x=x_val, a=2, b=3)
    print(result)  # Output: 7

    your_adder = Adder(x_val, 'c', 'd')

    result2 = your_adder(x=x_val, c=1, d=5)
    print(result2)  # Output: 8
