from wiki import article_metadata, ask_search, ask_advanced_search
# 1) 
#
# Function: search
#
# Parameters:
#   keyword - search word to look for in article metadata's relevant keywords
#
# Returns: list of metadata for articles in which the article is relevant to
#   the keyword. Relevance is determined by checking the metadata's "relevant
#   keywords" list for a case-insensitive match with the keyword parameter. #   The returned list should not include the "relevant keywords" list for each
#   article metadata.
#   
#   If the user does not enter anything, return an empty list
def search(keyword):
# If keyword is empty return empty list
     if len(keyword) == 0:
        return []
# metadata contains all article Metadata from wiki.article_metadata()
     metadata = article_metadata() 
# article_with_keyword to accumulate data if keyword is found.
     article_with_keyword = []

     for data in metadata:
        for mata_key in data[4]:
            if mata_key.lower() == keyword.lower():
                article_with_keyword.append(data[:4])

     return article_with_keyword
# 2) 
#
# Function: article_length
#
# Parameters:
#   max_length - max character length of articles
#   metadata - article metadata to search through
#
# Returns: list of article metadata from given metadata with articles not
#   exceeding max_length number of characters
def article_length(max_length, metadata):
# If max_length is less than zero, it return an empty list.
     if max_length <= 0:
        return []

# article_with_keyword to accumulate data.
     article_with_keyword = []

     for data in metadata:
        if max_length >= data[3]:
            article_with_keyword.append(data[:4])

     return article_with_keyword
# 3) 
#
# Function: unique_authors
#
# Parameters:
#   count - max number of unique authors to include in the results
#   metadata - article metadata
#
# Returns: list of article metadata containing a maximum of `count` results,
#   each with a unique author. If two or more articles have the same author, 
#   include the first in the results and skip the others. Two authors are 
#   considered the same if they are a case-insensitive match. If count is 
#   larger than the number of unique authors, return all articles with the 
#   duplicate authors removed.
def unique_authors(count, metadata):
# If count is less than zero, it return an empty list.
     if count <= 0:
        return []

# article_with_keyword to accumulate data. seen_authors, a set to store unique authors.
     article_with_keyword = []
     seen_authors = []

     for data in metadata:
# author contains the name of author in each data.
        author = data[1].lower()
        if author not in seen_authors:
            seen_authors.append(author)
            article_with_keyword.append(data[:4])
        if count == len(article_with_keyword):
            return article_with_keyword

     return article_with_keyword  

# 4) 
#
# Function: most_recent_article
#
# Parameters:
#   metadata - article metadata
#
# Returns: article metadata of the article published most recently according
#   to the timestamp. Note this should return just a 1D list representing
#   a single article.
def most_recent_article(metadata):
# if metadata is empty, return empty list.
    if len(metadata) == 0:
        return []
# most_recent_timestamp contains the first data's timestamp for the comparision purposes.
# most_recent_index contains the index of largest timespan upto that point. 
    most_recent_timestamp = metadata[0][2]
    most_recent_index = 0

    for index in range(1, len(metadata)):
        current_timestamp = metadata[index][2]
        if current_timestamp > most_recent_timestamp:
            most_recent_timestamp = current_timestamp
            most_recent_index = index

    return metadata[most_recent_index]
# 5) 
#
# Function: favorite_author
#
# Parameters:
#   favorite - favorite author title
#   metadata - article metadata
#
# Returns: True if favorite author is in the given articles (case 
#   insensitive), False otherwise
def favorite_author(favorite, metadata):

    for data in metadata:
        if favorite.lower() == data[1].lower():
            return True

    return False

# 6) 
#
# Function: title_and_author
#
# Parameters:
#   metadata - article metadata
#
# Returns: list of Tuples containing (title, author) for all of the given 
#   metadata.
def title_and_author(metadata):
#title_and_author to return the required field.   
    title_and_author = []
    for data in metadata:
        title_and_author.append((data[0], data[1]))

    return title_and_author
# 7) 
#
# Function: refine_search
#
# Parameters:
#   keyword - additional keyword to search
#   metadata - article metadata from basic search
#
# Returns: searches for article metadata from entire list of available
#   articles using keyword. Returns the article metadata that is returned in 
#   in *both* the additional search and the basic search. The results should
#   be in the same order that they were returned in the basic search. Two
#   articles can be considered the same if both their author and article title
#   match exactly.
def refine_search(keyword, metadata):
# If keyword is empty return empty list
    if len(keyword) == 0:
        return []
# common_metadata to return the required data.
    common_metadata = []
# metadata contain the seach result.
    metadata_main = search(keyword)

    for index in range(len(metadata)):
        for inner_index in range(len(metadata_main)):
            if metadata[index][1] == metadata_main[inner_index][1] and metadata[index][2] == metadata_main[inner_index][2]:
                common_metadata.append(metadata[index])
                
    return common_metadata

# Prints out articles based on searched keyword and advanced options
def display_result():
    # Stores list of articles returned from searching user's keyword
    articles = search(ask_search())

    # advanced stores user's chosen advanced option (1-7)
    # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
        # value stores max article title length in number of characters
        # Update article metadata to contain only ones of the maximum length
        articles = article_length(value, articles)
    if advanced == 2:
        # value stores max number of unique authors
        # Update article metadata to contain only the max number of authors
        articles = unique_authors(value, articles)
    elif advanced == 3:
        # Update articles to only contain the most recent article
        articles = most_recent_article(articles)
    elif advanced == 4:
        # value stores author
        # Store whether author is in search results into variable named 
        # has_favorite
        has_favorite = favorite_author(value, articles)
    elif advanced == 5:
        # Update article metadata to only contain titles and authors
        articles = title_and_author(articles)
    elif advanced == 6:
        # value stores keyword to search
        # Update article metadata to contain only article metadata
        # that is contained in both searches
        articles = refine_search(value, articles)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

    if advanced == 4:
        print("Your favorite author is" + ("" if has_favorite else " not") + " in the returned articles!")

if __name__ == "__main__":
    display_result()
