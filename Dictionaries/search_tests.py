from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)

    def test_keyword_to_titles(self):
        input_2D_list = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023, ['canadian', 'canada', 'lee', 'jazz', 'and', 'rock', 'singer',  'smith']], ['French pop music', 'Mack Johnson', 1172208041, 5569, ['french', 'pop', 'music', 'the', 'france', 'and', 'radio']], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']]]
        expected_output = {'canadian': ['List of Canadian musicians'], 'canada': ['List of Canadian musicians'], 'lee': ['List of Canadian musicians'], 'jazz': ['List of Canadian musicians'], 'and': ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], 'rock': ['List of Canadian musicians'], 'singer': ['List of Canadian musicians'], 'smith': ['List of Canadian musicians'], 'french': ['French pop music'], 'pop': ['French pop music'], 'music': ['French pop music'], 'the': ['French pop music', 'Edogawa, Tokyo'], 'france': ['French pop music'], 'radio': ['French pop music'], 'edogawa': ['Edogawa, Tokyo'], 'with': ['Edogawa, Tokyo'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo']}
        self.assertEqual(keyword_to_titles(input_2D_list), expected_output)
        self.assertEqual(keyword_to_titles([[]]), {})
        self.assertEqual(keyword_to_titles([]), {})
        self.assertEqual(keyword_to_titles([['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023, []]]), {})

    def test_title_to_info(self):
        input_2D_list = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023, ['canadian', 'canada', 'lee', 'jazz', 'and', 'rock', 'singer',  'smith']], ['French pop music', 'Mack Johnson', 1172208041, 5569, ['french', 'pop', 'music', 'the', 'france', 'and', 'radio']], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']]]
        expected_output = {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Mack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}
        self.assertEqual(title_to_info(input_2D_list), expected_output)
        self.assertEqual(title_to_info([[]]), {})
        self.assertEqual(title_to_info([]), {})
        self.assertEqual(title_to_info([['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023, []]]), {'List of Canadian musicians': {'author': 'Jack Johnson', 'length': 21023, 'timestamp': 1181623340}})

    def test_search(self):
        self.assertEqual(search('and', {'canadian': ['List of Canadian musicians'], 'canada': ['List of Canadian musicians'], 'lee': ['List of Canadian musicians'], 'jazz': ['List of Canadian musicians'], 'and': ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], 'rock': ['List of Canadian musicians'], 'singer': ['List of Canadian musicians'], 'smith': ['List of Canadian musicians'], 'french': ['French pop music'], 'pop': ['French pop music'], 'music': ['French pop music'], 'the': ['French pop music', 'Edogawa, Tokyo'], 'france': ['French pop music'], 'radio': ['French pop music'], 'edogawa': ['Edogawa, Tokyo'], 'with': ['Edogawa, Tokyo'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo']}), ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'])
        self.assertEqual(search('apple', {'canadian': ['List of Canadian musicians'], 'canada': ['List of Canadian musicians'], 'lee': ['List of Canadian musicians'], 'jazz': ['List of Canadian musicians'], 'and': ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], 'rock': ['List of Canadian musicians'], 'singer': ['List of Canadian musicians'], 'smith': ['List of Canadian musicians'], 'french': ['French pop music'], 'pop': ['French pop music'], 'music': ['French pop music'], 'the': ['French pop music', 'Edogawa, Tokyo'], 'france': ['French pop music'], 'radio': ['French pop music'], 'edogawa': ['Edogawa, Tokyo'], 'with': ['Edogawa, Tokyo'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo']}), [])
        self.assertEqual(search('apple', {}), [])
        self.assertEqual(search('', {}), [])
        self.assertEqual(search('', {'canadian': ['List of Canadian musicians'], 'canada': ['List of Canadian musicians'], 'lee': ['List of Canadian musicians'], 'jazz': ['List of Canadian musicians'], 'and': ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], 'rock': ['List of Canadian musicians'], 'singer': ['List of Canadian musicians'], 'smith': ['List of Canadian musicians'], 'french': ['French pop music'], 'pop': ['French pop music'], 'music': ['French pop music'], 'the': ['French pop music', 'Edogawa, Tokyo'], 'france': ['French pop music'], 'radio': ['French pop music'], 'edogawa': ['Edogawa, Tokyo'], 'with': ['Edogawa, Tokyo'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo']}), [])

    def test_article_length(self):
        self.assertEqual(article_length(21023, ['List of Canadian musicians', 'French pop music'], {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Mack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}), ['List of Canadian musicians', 'French pop music'])
        self.assertEqual(article_length(0, ['List of Canadian musicians', 'French pop music'], {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Mack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}), [])
        self.assertEqual(article_length(21023, [], {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Mack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}), [])
        self.assertEqual(article_length(21023, ['List of Canadian musicians', 'French pop music'], {}), [])
        self.assertEqual(article_length(-2, [], {}), [])

    def test_key_by_author(self):
        self.assertEqual(key_by_author(['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Jack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}), {'Jack Johnson' : ['List of Canadian musicians',  'French pop music'], 'jack johnson' : ['Edogawa, Tokyo']})
        self.assertEqual(key_by_author([], {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Jack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}), {})
        self.assertEqual(key_by_author(['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], {}), {})
        self.assertEqual(key_by_author([], {}), {})
    
    def test_filter_to_author(self):
        self.assertEqual(filter_to_author('jack johnson', ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Jack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}), ['Edogawa, Tokyo'])
        self.assertEqual(filter_to_author('', ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Jack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}), [])
        self.assertEqual(filter_to_author('jack johnson', [], {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Jack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}), [])
        self.assertEqual(filter_to_author('jack johnson', ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], {}), [])
        self.assertEqual(filter_to_author('Jack', ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Jack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}), [])
        self.assertEqual(filter_to_author('', [], {}), [])

    def test_filter_out(self):
        self.assertEqual(filter_out('canada', ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], {'canadian': ['List of Canadian musicians'], 'canada': ['List of Canadian musicians'], 'lee': ['List of Canadian musicians'], 'jazz': ['List of Canadian musicians'], 'and': ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], 'rock': ['List of Canadian musicians'], 'singer': ['List of Canadian musicians'], 'smith': ['List of Canadian musicians'], 'french': ['French pop music'], 'pop': ['French pop music'], 'music': ['French pop music'], 'the': ['French pop music', 'Edogawa, Tokyo'], 'france': ['French pop music'], 'radio': ['French pop music'], 'edogawa': ['Edogawa, Tokyo'], 'with': ['Edogawa, Tokyo'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo']}), ['French pop music', 'Edogawa, Tokyo'])
        self.assertEqual(filter_out('canada', [], {'canadian': ['List of Canadian musicians'], 'canada': ['List of Canadian musicians'], 'lee': ['List of Canadian musicians'], 'jazz': ['List of Canadian musicians'], 'and': ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], 'rock': ['List of Canadian musicians'], 'singer': ['List of Canadian musicians'], 'smith': ['List of Canadian musicians'], 'french': ['French pop music'], 'pop': ['French pop music'], 'music': ['French pop music'], 'the': ['French pop music', 'Edogawa, Tokyo'], 'france': ['French pop music'], 'radio': ['French pop music'], 'edogawa': ['Edogawa, Tokyo'], 'with': ['Edogawa, Tokyo'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo']}), [])
        self.assertEqual(filter_out('', ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], {'canadian': ['List of Canadian musicians'], 'canada': ['List of Canadian musicians'], 'lee': ['List of Canadian musicians'], 'jazz': ['List of Canadian musicians'], 'and': ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], 'rock': ['List of Canadian musicians'], 'singer': ['List of Canadian musicians'], 'smith': ['List of Canadian musicians'], 'french': ['French pop music'], 'pop': ['French pop music'], 'music': ['French pop music'], 'the': ['French pop music', 'Edogawa, Tokyo'], 'france': ['French pop music'], 'radio': ['French pop music'], 'edogawa': ['Edogawa, Tokyo'], 'with': ['Edogawa, Tokyo'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo']}), ['List of Canadian musicians','French pop music', 'Edogawa, Tokyo'])
        self.assertEqual(filter_out('', [], {}), [])

    def test_articles_from_year(self): 
        self.assertEqual(articles_from_year(2007, ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Mack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}), ['List of Canadian musicians', 'French pop music'])
        self.assertEqual(articles_from_year(2001, ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo'], {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Mack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}), [])
        self.assertEqual(articles_from_year(2007, [], {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Mack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}), [])

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_advanced_option_1(self, input_mock):
        keyword = 'soccer'
        advanced_option = 1
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_2(self, input_mock):
        keyword = 'soccer'
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: {'jack johnson': ['Spain national beach soccer team'], 'Burna Boy': ['Will Johnson (soccer)'], 'Mack Johnson': ['Steven Cohen (soccer)']}\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_3(self, input_mock):
        keyword = 'soccer'
        advanced_option = 3
        advanced_response = 'jack johnson'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + advanced_response + "\n\nHere are your articles: ['Spain national beach soccer team']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_4(self, input_mock):
        keyword = 'soccer'
        advanced_option = 4
        advanced_response = 'canada'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + advanced_response + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_6(self, input_mock):
        keyword = 'soccer'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
