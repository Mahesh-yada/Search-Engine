from wiki import article_titles, ask_search, ask_advanced_search

# 1) 
#
# Function: search
#
# Parameters:
#   keyword - search word to look for in article titles
#
# Returns: list of article titles containing given keyword (case insensitive).
# If the keyword is empty or no results are found, return an empty list.
def search(keyword):
    # If keyword is empty return empty list
    if len(keyword) == 0:
        return []
    # Convert keyword to lower to handle case insensitivity.
    keyword = keyword.lower() 
    # Store all article titles to look for.
    all_article_title = article_titles() 
    # article_with_keyword to return the list of article containing key words. 
    article_with_keyword = []
    # for loop to check if the keyword is in title
    for title in all_article_title:
        if keyword in title.lower():
            article_with_keyword.append(title)

    return article_with_keyword

# 2) 
#
# Function: title_length
#
# Returns 
#
# Parameters:
#   max_length - max character length of article titles
#   titles - list of article titles to search through
#
# Returns: list of article titles from given titles with a length that does
# not exceed max_length number of characters 
def title_length(max_length, titles):
    # If titles is empty or  max_length is 0 or less, return empty list
    if len(titles) == 0 or max_length <= 0:
        return []    
    # matching_article to return list of article titles from given titles with a length that does
    # not exceed max_length number of characters
    matching_article = []

    for title in titles:
        if len(title) <= max_length:
            matching_article.append(title)

    return matching_article

# 3) 
#
# Function: article_count
#
# Parameters:
#   count - max number of returned articles
#   titles - list of article titles to search through
#
# Returns: list of articles in given titles starting from the 
# beginning that do not exceed given count in total. If there are no 
# given article titles, return an empty list regardless of the count.
# If the max is larger than the # of titles, just return all titles.
def article_count(count, titles):
    # If titles is empty or  count is 0 or less, return empty list
    if len(titles) == 0 or count <= 0:
        return []
    # matching_article to return the required articles.
    matching_article = []

    if count >= len(titles):
        return titles
    else:
        for index in range(count):
            matching_article.append(titles[index])
    
    return matching_article


# 4) 
#
# Function: random_article
#
# Parameters:
#   index - index at which article title to return
#   titles - list of article titles to search through
#
# Returns: article title in given titles at given index. If
# index is not valid, return an empty string
def random_article(index, titles):
    # If titles is empty or index is less than 0, return empty list
    if len(titles) == 0 or index < 0 or index >= len(titles):
        return ''
    else:
        return titles[index]
# 5) 
#
# Function: favorite_article
#
# Parameters:
#   favorite - favorite article title
#   titles - list of article titles to search through
#
# Returns: True if favorite article is in the given articles
# (case insensitive) and False otherwise
def favorite_article(favorite, titles):

    # Convert favorite to lower to handle case insensitivity.
    favorite = favorite.lower()

    for title in titles:
        if favorite == title.lower():
            return True
    
    return False
    
# 6) 
#
# Function: multiple_keywords
#
# Parameters:
#   keyword - additional keyword to search
#   titles - article titles from basic search
#
# Returns: searches for article titles from entire list of available
# articles and adds those articles to list of article titles from basic 
# search
def multiple_keywords(keyword, titles):
    # If keyword is empty return empty list
    if len(keyword) == 0:
        return titles
    return titles + search(keyword)

# Prints out articles based on searched keyword and advanced options
def display_result():
    # Stores list of articles returned from searching user's keyword
    articles = search(ask_search())

    # advanced stores user's chosen advanced option (1-5)
    # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
        # value stores max article title length in number of characters
        # Update article titles to contain only ones of the maximum length
        articles = title_length(value, articles)
    if advanced == 2:
        # value stores max number of articles
        # Update article titles to contain only the max number of articles
        articles = article_count(value, articles)
    elif advanced == 3:
        # value stores random number
        # Update articles to only contain the article title at index of the random number
        articles = random_article(value, articles)
    elif advanced == 4:
        # value stores article title
        # Store whether article title is in the search results into a variable named has_favorite
        has_favorite = favorite_article(value, articles)
    elif advanced == 5:
        # value stores keyword to search
        # Updated article titles to contain article titles from the first search and the second search
        articles = multiple_keywords(value, articles)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

    if advanced == 4:
        print("Your favorite article is" + ("" if has_favorite else " not") + " in the returned articles!")

if __name__ == "__main__":
    display_result()
