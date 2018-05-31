import threading
from threading import Thread


class PrintJSFilesThread(Thread):
    def __init__(self,url,filename):
        super().__init__()
        self.url = url
        self.filename = filename

    def run(self):
        # gets data from url and processes it
        pass


while True:
    url = input("Enter website url [end to stop ]: ")
    if url == "end":
        break

    filename = input("Enter filename : ")
    t = PrintJSFilesThread(url,filename)
    t.start()

