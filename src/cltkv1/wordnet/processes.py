"""``Process`` to wrap WordNet."""


from dataclasses import dataclass
from typing import Dict, List, Tuple

from boltons.cacheutils import cachedproperty

from cltkv1.core.data_types import Doc, Process, Word
from cltkv1.wordnet.wordnet import WordNetCorpusReader, WordNetICCorpusReader


@dataclass
class WordNetProcess(Process):
    """A ``Process`` type to capture what the
    ``wordnet`` module can do for a
    given language.
    """

    language: str = None

    @cachedproperty
    def algorithm(self):
        """Returns a WordNetCorpusReader appropriate to the Document's language"""
        language = None
        if self.language == "lat":
            language = "lat"
        elif self.language == "grc":
            language = "grk"
        elif self.language == "san":
            language = "skt"
        if language is not None:
            return WordNetCorpusReader(language)

    def run(self):
        """
                Then we would loop through Doc.words. Within that list are
                many Word objects. You
                would look at word.lemma (say) and then in .run() (below) you would create a new key-value pair
                within Word. So
                if Word.lemma = "adversarius" you could add something like Word.synset = [inimicus, perduellis].

                after resolving the lemma, return its Synsets -- via which it is possible access synonyms, etc
                alternatively, and perhaps more intuitive for most use-cases, immediately return the resolved Lemmas
                via this Lemma's Synsets
        """
        pass
