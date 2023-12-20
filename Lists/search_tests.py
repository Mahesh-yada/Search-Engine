from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        # Storing into a variable so don't need to copy and paste long list every time
        # If you want to store search results into a variable like this, make sure you pass a copy of it when
        # calling a function, otherwise the original list (ie the one stored in your variable) might be
        # mutated. To make a copy, you may use the .copy() function for the variable holding your search result.
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(search('dog'), expected_dog_search_results)

    def test_search(self):
        self.assertEqual(search(''), [])
        expected_Dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(search('Dog'), expected_Dog_search_results)
        self.assertEqual(search('abcdefghijklmnopqrstuvwxyz'), [])
        self.assertEqual(search('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), [])
       
    def test_title_length(self):
        self.assertEqual(title_length(0, ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston']), [])
        self.assertEqual(title_length(8, []), [])
        self.assertEqual(title_length(8, ['Edogawa', 'Tokyo', 'Kevin Cadogan']), ['Edogawa', 'Tokyo'])
        self.assertEqual(title_length(2, ['Edogawa', 'Tokyo', 'Kevin Cadogan']), [])
        self.assertEqual(title_length(5, ['Edogawa', 'Tokyo', 'Kevin Cadogan']), ['Tokyo'])

    def test_article_count(self):
        self.assertEqual(article_count(8, []), [])
        self.assertEqual(article_count(8, ['Edogawa', 'Tokyo', 'Kevin Cadogan']), ['Edogawa', 'Tokyo', 'Kevin Cadogan'])
        self.assertEqual(article_count(0, ['Edogawa', 'Tokyo', 'Kevin Cadogan']), [])
        self.assertEqual(article_count(2, ['Edogawa', 'Tokyo', 'Kevin Cadogan']), ['Edogawa', 'Tokyo'])

    def test_random_article(self):
        self.assertEqual(random_article(8, []), '')
        self.assertEqual(random_article(8, ["apple", "Ball", "cat"]), '')
        self.assertEqual(random_article(0, ["apple", "Ball", "cat"]), "apple")
        self.assertEqual(random_article(-1, ["apple", "Ball", "cat"]), "")

    def test_favorite_article(self):
        self.assertEqual(favorite_article('apple', ["apple", "Ball", "cat"]), True)
        self.assertEqual(favorite_article('Apple', ["apple", "Ball", "cat"]), True)
        self.assertEqual(favorite_article("apple", []), False)
        self.assertEqual(favorite_article("", ["apple", "Ball", "cat"]), False)
        
    def test_multiple_keywords(self):
        self.assertEqual(multiple_keywords("dog", ["apple", "ball", "cat"]), ["apple", "ball", "cat",'Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)'])
        self.assertEqual(multiple_keywords("abcdefghijklmnopqrstuvwxrz", ["apple", "ball", "cat"]), ["apple", "ball", "cat"])
        self.assertEqual(multiple_keywords("dOg", ["apple", "ball", "cat"]), ["apple", "ball", "cat",'Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)'])
        self.assertEqual(multiple_keywords("dog", []), ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)'])
        self.assertEqual(multiple_keywords("abcdefghijklmnopqrstuvwxrz", []), [])
        self.assertEqual(multiple_keywords("DOG", []), ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)'])
        self.assertEqual(multiple_keywords("", ["apple", "ball", "cat"]), ["apple", "ball", "cat"])
    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'dog'
        advanced_option = 6

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced1(self, input_mock):
        keyword = 'dog'
        advanced_option = 1
        advanced_option1 = 10
        output = get_print(input_mock, [keyword, advanced_option, advanced_option1])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_option1) + '\n' + "\nHere are your articles: ['Guide dog', 'Endoglin', 'Sun dog']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced2(self, input_mock):
        keyword = 'dog'
        advanced_option = 2
        advanced_option2 = 4
        output = get_print(input_mock, [keyword, advanced_option, advanced_option2])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_option2) + '\n' + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced3(self, input_mock):
        keyword = 'dog'
        advanced_option = 3
        advanced_option3 = 3
        output = get_print(input_mock, [keyword, advanced_option, advanced_option3])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_option3) + '\n' + "\nHere are your articles: Black dog (ghost)\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced4(self, input_mock):
        keyword = 'cat'
        advanced_option = 4
        advanced_option4 = "Guide"
        output = get_print(input_mock, [keyword, advanced_option, advanced_option4])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + advanced_option4 + '\n' + "\nHere are your articles: ['Voice classification in non-classical music']" + "\nYour favorite article is not in the returned articles!"+ '\n'
        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)
        
    @patch('builtins.input')
    def test_advanced5(self, input_mock):
        keyword = 'dog'
        advanced_option = 5
        advanced_option5 = 'Black'
        output = get_print(input_mock, [keyword, advanced_option, advanced_option5])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_option5) + '\n' + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'Black dog (ghost)']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
