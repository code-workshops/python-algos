"""
Builder Pattern
===============

complexity: ??
use case: Modeling

Parts:
 - Consumer
 - Director
 - Builder

Builder Pattern seems to be what we see in ORMs, especially when it comes to
related models. Aside from the Director role, this pattern is all about creating
multiple objects at once and returning the instance to the view.

Also seems similar to what we create when integrating modules/creating APIs.
"""

class Book(object):
    def __init__(self, title):
        self.title = title
        self.author = None
        self.genre = None

    def add_author(self, name):
        self.author = name
        print("Book author set.")


class LibraryBuilder(object):
    """Builder Pattern Example."""

    def __init__(self, name, books=[]):
        self.name = name
        self.books = books

    def add_book(self, name):
        book = Book(name)
        self.books.add(book)
        print("Book added.")


class Librarian(object):
    """Director for the LibraryBuilder."""

    def __init__(self):
        self.builder = None

    def setup_library(self, name, books=None):
        lib = LibraryBuilder(name, books)
        print("Library build complete.")
        return lib

    def add_book(self, book):
        self.builder.add_book = book


"""
Adapter Pattern
===============
(aka, wrapper)

common uses: API integrations

Parts:
    - Target interface (client)
    - Adapter (mapping)
    - Adaptee (new component)

This pattern is about mapping an old component to a new one.

Let's suppose a website had a music player. Users can use a play, pause and
forward skip button. Now suppose we have an audio library that can provide this
utility, but doesn't quite offer a play, puase or skip action.
"""
import abc


class MusicPlayer(metaclass=abc.ABCMeta):
    def __init__(self):
        self._player = AudioPlayer()

    @abstractmethod
    def play(self, track):
        pass


class PlayerAdapter(MusicPlayer):
    def play(self, track):
        self._player.stream_audio(track)


class AudioPlayer:
    def stream_audio(self, track):
        # some logic to play a track


"""
Decorator Pattern
=================

Extends the functionality of an object dynamically. Recursive composition.
"""
