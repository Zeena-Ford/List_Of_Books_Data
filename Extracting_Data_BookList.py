from typing import List
from load_data import book_category_dictionary
book_dictionary = book_category_dictionary("google_books_dataset.csv")

def get_books_by_publisher(dictionary:dict, the_publisher:str) -> int: 
    
    """
    Preconditions: The number of books published by the publisher is an positive integer value. The dictionary parameter is the
    function call: 'book_category_dictionary('google_books_dataset.csv')'.
    
    Returns the number of books published by the given publishers
        
    >>> get_books_by_publisher(book_category_dictionary('google_books_dataset.csv'), 'DC Comics')
    The Publisher DC Comics has published the following books:
    Book 1 : Watchmen (2019 Edition) by Alan Moore
    1

    >>> get_books_by_publisher(book_category_dictionary('google_books_dataset.csv'), 'AMACOM')
    The Publisher AMACOM has published the following books:
    Book 1 : Marketing (The Brian Tracy Success Library) by Brian Tracy
    Book 2 : Management (The Brian Tracy Success Library) by Brian Tracy
    Book 3 : Business Strategy (The Brian Tracy Success Library) by Brian Tracy
    Book 4 : Personal Success (The Brian Tracy Success Library) by Brian Tracy
    Book 5 : The Essentials of Finance and Accounting for Nonfinancial Managers by Edward Fields
    5
    
    
    >>> get_books_by_publisher(book_category_dictionary('google_books_dataset.csv'), 'Kensington Publishing Corp.')
    The Publisher Kensington Publishing Corp. has published the following books:
    Book 1 : Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    Book 2 : Antiques Knock-Off by Barbara Allan
    2
    
    >>> get_books_by_publisher(book_category_dictionary('google_books_dataset.csv'), 'Non-existent Publisher')
    The Publisher Non-existent Publisher has published the following books:
    Sorry, that publisher does not exist
    0
    """
 
   
    #print('The Publisher', the_publisher, 'has published the following books:')
    dictvalues = dictionary.values()  
    
    title_set = set()
    publisher_counter = 0 
    for items in dictvalues:
        for n in items:
            if (the_publisher == n.get('publisher')) and (n.get('title') not in title_set):  
                title_set.add(n.get('publisher'))
                title_set.add(n.get('title'))
                
                
                if the_publisher in title_set:
                    publisher_counter+=1
                    #print('Book', publisher_counter,':', str(n.get('title')), 'by', str(n.get('author')))
                  
                    
    
    if the_publisher not in title_set:
        print("Sorry, that publisher does not exist") 
        
   
    return publisher_counter




def get_all_categories_for_book_title(dictionary2:dict, book_titles:str) -> int:
    
    """
    Preconditions: The number of books published by the publisher is a positive integer value. The dictionary2 parameter is the
    function call: 'book_category_dictionary('google_books_dataset.csv')'.
    
    Returns the number of categories associated with the given title. 
    
    >>> get_all_categories_for_book_title(book_category_dictionary('google_books_dataset.csv'), 'After Anna') 
    The book title After Anna belongs to the following categories:
    Category 1 : Fiction
    Category 2 : Thrillers
    Category 3 : Mystery
    Category 4 : Adventure
    The number of categories that belongs to that book:
    4
    
    >>> get_all_categories_for_book_title(book_category_dictionary('google_books_dataset.csv'), 'Book by Zeena')
    The book title Book by Zeena belongs to the following categories:
    That book title does not exist
    The number of categories that belongs to that book:
    0
    
    >>> get_all_categories_for_book_title(book_category_dictionary('google_books_dataset.csv'), "Final Option: 'The best one yet'")
    The book title Final Option: 'The best one yet' belongs to the following categories:
    Category 1 : Fiction
    Category 2 : Thrillers
    Category 3 : Mystery
    Category 4 : Crime
    The number of categories that belongs to that book:
    4
    """
    
    
    values_dict = dictionary2.values()   
     
    number_categories = 0
    storing_titles = set()
    
    #print("The book title", book_titles, "belongs to the following categories:")
    for i in values_dict:
        for n in i:
            
            
            all_titles = (n.get('title'))
            
            if book_titles == all_titles:
                number_categories += 1
                the_category = (n.get('category'))
                #print('Category', number_categories,':',the_category)
                storing_titles.add(all_titles)
                    
                  
    
    if book_titles not in storing_titles:
        print("That book title does not exist") 
    
    #print("The number of categories that belongs to that book:")
    return number_categories  

