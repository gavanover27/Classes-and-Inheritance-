class Book:
    """Book class"""
    def __init__(self, title, author, publisher, releaseYear, pageCount):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._releaseYear = releaseYear
        self._pageCount = pageCount

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def publisher(self):
        return self._publisher

    @property
    def releaseYear(self):
        return self._releaseYear
    
    @property
    def pageCount(self):
        return self._pageCount

    @title.setter
    def title(self, new_title):
        self. _title = new_title

    @author.setter
    def author(self, new_author):
        self._author = new_author

    @publisher.setter
    def publisher(self, new_publisher):
        self._publisher = new_publisher

    @releaseYear.setter
    def releaseYear(self, new_releaseYear):
        self._releaseYear = new_releaseYear
    
    @pageCount.setter
    def pageCount(self, new_pageCount):
        self._pageCount = new_pageCount


    def open(self):
        print('Opening')
    
    def close(self):
        print('Closing')
    
    def read(self):
        print('Reading')

    def flippage(self):
        print('Flipping Page')

class Textbook(Book):
    """Textbook class, inheriting from Book"""
    def __init__(self, title, author, publisher, releaseYear, pageCount):
        super().__init__(title, author, publisher, releaseYear, pageCount)
        self.__subject = subject

class Address_Book(Book):
    """Address Book class, inheriting from Book"""
    def write(self):
        print('Writing')