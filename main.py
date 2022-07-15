import sys

from myapp.app import MyObject


def main():
    my_object_instance = MyObject()

    print("The given number is %d" % (my_object_instance.another_function()))
    sys.exit(0)


if __name__ == "__main__":
    main()
