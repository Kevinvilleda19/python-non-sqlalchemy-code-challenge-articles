class Article:
    all = []  # Class-level list to store all Article instances

    def __init__(self, author, magazine, title):
        # Validate title is a string and between 5 and 50 characters
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")

        self.author = author  # Author instance
        self.magazine = magazine  # Magazine instance
        self._title = title  # Private title attribute

        # Append the article to the class-level list of articles
        Article.all.append(self)

        # Append the article to the magazine's internal list of articles
        self.magazine._articles.append(self)

    @property
    def title(self):
        """Returns the article's title (immutable)."""
        return self._title

    @property
    def author(self):
        """Returns the author of the article."""
        return self._author

    @author.setter
    def author(self, new_author):
        """Allows changing the article's author."""
        if not isinstance(new_author, Author):
            raise ValueError("Author must be an instance of the Author class.")
        self._author = new_author

    @property
    def magazine(self):
        """Returns the magazine of the article."""
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        """Allows changing the article's magazine."""
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")
        self._magazine = new_magazine


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name

    @property
    def name(self):
        """Returns the author's name."""
        return self._name

    def articles(self):
        """Return all articles written by this author."""
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """Return a unique list of magazines for which the author has contributed."""
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        """Creates and returns a new Article instance and associates it with the author and magazine."""
        # Create a new Article instance. The Article constructor will add it to the magazine's articles.
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        """Returns a unique list of categories of the magazines the author has contributed to."""
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")

        self._name = name
        self._category = category
        self._articles = []  # Store articles for this magazine

    @property
    def name(self):
        """Returns the magazine's name."""
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        """Returns the magazine's category."""
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = new_category

    def articles(self):
        """Return all articles published in this magazine."""
        return self._articles
