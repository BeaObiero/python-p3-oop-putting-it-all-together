
class Book:
    def __init__(self, title, page_count, publication_year):
        self.title = title
        self.page_count = page_count
        self.publication_year = publication_year

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string.")
        self._title = value

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            raise ValueError("page_count must be an integer")
        self._page_count = value

    @property
    def publication_year(self):
        return self._publication_year

    @publication_year.setter
    def publication_year(self, value):
        if not isinstance(value, int):
            raise ValueError("Publication year must be an integer.")
        self._publication_year = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def __str__(self):
        return f"{self.title} ({self.page_count} pages, Published in {self.publication_year})"

    def __repr__(self):
        return f"Book(title={self.title!r}, page_count={self.page_count}, publication_year={self.publication_year})"
