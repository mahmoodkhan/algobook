class Geek():
    """
    This class overloads bitwise operation
    """
    def __init__(self, value):
        self.value = value

    def __and__(self, obj):
        print("And operator overloaded")
        if isinstance(obj, Geek):
            return self.value & obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __or__(self, obj):
        print("Or operator overloaded")
        if isinstance(obj, Geek):
            return self.value | obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __xor__(self, obj):
        print("Xor operator overloaded")
        if isinstance(obj, Geek):
            return self.value ^ obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __lshift__(self, obj):
        print("lshift operator overloaded")
        if isinstance(obj, Geek):
            return self.value << obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __rshift__(self, obj):
        print("rshift operator overloaded")
        if isinstance(obj, Geek):
            return self.value >> obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __invert__(self):
        print("Invert operator overloaded")
        return ~self.value


class Misc:
    def convert_int_to_binary_array(self, num: int):
        return [int(bit) for bit in bin(num)[2::]]

    def convert_int_to_binary_array2(self, x: int):
        """
        1. iterate until x is zero
        2. on each iteration, if the first first bit of x is 1 then add 1 else add 0
        .. x & 1 means if the first bit of x is 1 then the result of x & 1 will be 1 otherwise 0
        3. add the result of each x & 1 to the zeroth index of the array because we shift the bits to the right.
        """
        binary_array = []
        while x:
            binary_array.insert(0, x & 1)
            x = x >> 1
        return binary_array

    def convert_int_to_binary_array3(self, x: int):
        # return [(x >> bit) & 1 for bit in range(x.bit_length())][::-1]
        return [(x >> bit) & 1 for bit in range(x.bit_length() -1, -1, -1)]


if __name__ == "__main__":
    # a = Geek(10)
    # b = Geek(12)
    # print(a & b)
    # print(a | b)
    # print(a ^ b)
    # print(a << b)
    # print(a >> b)
    # print(~a)
    # ..............................

    a = Misc()
    print(a.convert_int_to_binary_array(8))
    print(a.convert_int_to_binary_array2(8))
    print(a.convert_int_to_binary_array3(8))
