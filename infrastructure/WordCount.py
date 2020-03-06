from mrjob.job import MRJob

class MRWordCounter(MRJob):
    def mapper(self, key, line):
        line = line.strip()
        (words) = line.split(' ')
        for word in words:
            yield word, 1

    def reducer(self, word, occurences):
        yield word, sum(occurences)

if __name__ == '__main__':
    MRWordCounter.run()
