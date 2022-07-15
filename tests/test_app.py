from myapp.app import multiply_by_two, MyObject


class TestApp:
    def test_multiplication(self):
        res = multiply_by_two(2)
        assert res == 4

    def test_my_class(self):
        my_object_instance = MyObject()
        assert my_object_instance.another_function() == 2