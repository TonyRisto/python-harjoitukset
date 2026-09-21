class Release:
    def __init__(self, releaseName):
        self.releaseName = releaseName

    def printResults(self):
        print(f"Julkaisun nimi: {self.releaseName}")

class Book(Release):
    def __init__(self, releaseName, writer, pages):
        self.writer = writer
        self.pages = pages
        super().__init__(releaseName)

    def printResults(self):
        super().printResults()
        print(f"Kirjoittaja: {self.writer}\nSivuja: {self.pages}")

class Magazine(Release):
    def __init__(self, releaseName, chiefEditor):
        self.chiefEditor = chiefEditor
        super().__init__(releaseName)

    def printResults(self):
        super().printResults()
        print(f"Päätoimittaja: {self.chiefEditor}")

magazine = Magazine("Aku Ankka", "Aki Hyyppä")
book = Book("Hytti n:o 6", "Rosa Liksom", 200)

magazine.printResults()
book.printResults()
