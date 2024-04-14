This project implements a versatile search engine capable of retrieving relevant articles based on user queries. The search engine operates in three modes: List search, 2D lists search, and Dictionaries search, each offering different functionalities and outputs based on the structure of the data.

Features:

List Search:

Searches article titles and lists.
Basic search functionality.
Advanced options include:
Restricting maximum article title length.
Specifying the number of articles to retrieve.
Getting a random article.
Checking if a favorite article is in the results.
Searching for multiple keywords.

2D Lists Search:

Searches article metadata using 2D lists.
More detailed search with metadata.
Advanced options include:
Restricting maximum article title length.
Specifying the number of articles to retrieve.
Getting a random article.
Checking if a favorite article is in the results.
Retrieving only title and author information.
Searching for multiple keywords.

Dictionaries Search:

Searches article metadata using dictionaries.
Efficient search with structured data.
Advanced options include:
Retrieving the articles' metadata.
Restricting maximum article title length.
Retrieving only titles and timestamp information.
Checking if a favorite author wrote any articles in the results.
Searching for multiple keywords.

Project Structure:

search.py: Main script to perform searches in each part.

list_search.py: Contains functions for list search functionality.

2d_lists_search.py: Contains functions for 2D lists search functionality.

dictionaries_search.py: Contains functions for dictionaries search functionality.

data/: Directory containing sample data files for testing.

README.md: Project documentation and usage instructions.

Usage:

Run search.py.
Input a search word.
Choose a search mode (List, 2D Lists, Dictionaries).
Depending on the mode, respond to the advanced options prompts accordingly.

Contributing:

Contributions, suggestions, and bug reports are welcome.
Fork the repository, make your changes, and submit a pull request.

License:

This project is licensed under the MIT License.
