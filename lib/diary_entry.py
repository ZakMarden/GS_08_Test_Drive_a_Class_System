class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self.chunk_start_point = 0

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        self.words = self.contents.split()
        self.word_num = len(self.words)
        return self.word_num

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        return self.word_num / wpm

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        if self.chunk_start_point >= self.word_num:
            self.chunk_start_point = 0
        chunk_size_in_words = wpm * minutes
        chunk_end_point = self.chunk_start_point + chunk_size_in_words
        chunk = " ".join(self.words[self.chunk_start_point:chunk_end_point])
        self.chunk_start_point = chunk_end_point
        return chunk