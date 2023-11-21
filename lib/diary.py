class Diary:
    def __init__(self):
        self.entries_list = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.entries_list.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.entries_list

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        return sum([x.count_words() for x in self.entries_list])

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        return self.count_words() / wpm

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        words_can_read = wpm * minutes
        entries_not_over = [x for x in self.entries_list if x.count_words() <= words_can_read]
        return max(entries_not_over, key = lambda x: x.count_words())
        pass