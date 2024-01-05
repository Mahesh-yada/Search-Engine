from search import search, article_length, unique_authors, most_recent_article, favorite_author, title_and_author, refine_search, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        expected_search_soccer_results = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(search('soccer'), expected_search_soccer_results)

    def test_search(self):
        expected_search_canadian_results = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['2009 in music', 'RussBot', 1235133583, 69451], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]

        self.assertEqual(search(''), [])
        self.assertEqual(search('canadian'), expected_search_canadian_results)
        self.assertEqual(search('ball'), [])

    def test_article_length(self):
        metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(article_length(0, metadata), [])
        self.assertEqual(article_length(10, metadata), [])
        self.assertEqual(article_length(5000000, metadata), metadata)

    def test_unique_authors(self):
        metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 4144],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(unique_authors(0, metadata), [])
        self.assertEqual(unique_authors(2, metadata), [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 4144]])
        self.assertEqual(unique_authors(200, metadata), [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 4144],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562]])

    def test_most_recent_article(self):
        metadata1 = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 4144],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        metadata2 = [
            ['Spain national beach soccer team', 'jack johnson', 1246308670, 4144],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 4144],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(most_recent_article([]), [])
        self.assertEqual(most_recent_article(metadata1), ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 4144])
        self.assertEqual(most_recent_article(metadata2), ['Spain national beach soccer team', 'jack johnson', 1246308670, 4144])

    def tests_favorite_author(self):
        metadata1 = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 4144],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(favorite_author('jack johnson', []), False)
        self.assertEqual(favorite_author('jack johnson', metadata1), True)
        self.assertEqual(favorite_author('Jack johnson', metadata1), True)
        self.assertEqual(favorite_author("What's up", metadata1), False)

    def test_title_and_author(self):
        metadata1 = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 4144],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        metadata2 = [
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(title_and_author([]), [])
        self.assertEqual(title_and_author(metadata1), [('Spain national beach soccer team', 'jack johnson'), ('Ken Kennedy (computer scientist)', 'Mack Johnson'), ('Will Johnson (soccer)', 'Burna Boy'), ('Steven Cohen (soccer)', 'Mack Johnson')])
        self.assertEqual(title_and_author(metadata2), [('Will Johnson (soccer)', 'Burna Boy'), ('Steven Cohen (soccer)', 'Mack Johnson')])

    def tests_refine_search(self):
        metadata = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['2009 in music', 'RussBot', 1235133583, 69451], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]

        self.assertEqual(refine_search('', metadata ), [])
        self.assertEqual(refine_search('canadian', metadata ), metadata)
        self.assertEqual(refine_search('canadian', [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['2009 in music', 'RussBot', 1235133583, 69451], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['2007 in music', 'Bearcat', 1169248845, 45652]]), [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['2009 in music', 'RussBot', 1235133583, 69451], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['2007 in music', 'Bearcat', 1169248845, 45652]])

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 1
        advanced_response = 3000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advance_option_2(self, input_mock):
        keyword = 'soccer'
        advanced_option = 2
        advanced_response = 3000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advance_option_3(self, input_mock):
        keyword = 'soccer'
        advanced_option = 3

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advance_option_4(self, input_mock):
        keyword = 'soccer'
        advanced_option = 4
        advanced_response = 'jack johnson'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\nYour favorite author is in the returned articles!\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advance_option_5(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 'jack johnson'

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: [('Spain national beach soccer team', 'jack johnson'), ('Will Johnson (soccer)', 'Burna Boy'), ('Steven Cohen (soccer)', 'Mack Johnson')]\n"

        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_advance_option_6(self, input_mock):
        keyword = 'soccer'
        advanced_option = 6
        advanced_response = 'jack johnson'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advance_option_7(self, input_mock):
        keyword = 'soccer'
        advanced_option = 7

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\n"

        self.assertEqual(output, expected)

if __name__ == "__main__":
    main()
