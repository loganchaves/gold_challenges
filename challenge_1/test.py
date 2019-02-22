import unittest
import cafe 

class Testcafe (unittest.TestCase):

    def test_cafe_add_menu_item_should_add_item_to_menu_list(self):
        self.number = 'number'
        self.name = 'name'
        self.description = "des"
        self.ingredients = 'jan'

        cafe.add_menu_item(self.number, self.name, self.description, self.ingredients)
        actual = len(cafe.menu_list)
        expected = 1

        self.assertEqual(actual, expected)
    def test_cafe_show_item_should_show_items_in_menu(self):
        actual = len(cafe.show_item())
        excepted = 1


        self.assertEqual(actual, excepted)
    def test_delete_item_should_delete_item(self):
        self.number = '1'
        self.name = 'hi'
        self.description = 'd'
        self.ingredients = 'i'

        cafe.add_menu_item(self.number, self.name, self.description, self.ingredients)

        self.assertTrue(cafe.delete_item(self.number))