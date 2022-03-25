from datetime import datetime
from rich import print


class Logger:
    def __init__(self, name: str):
        self.name = name

    def log(self, *objects):
        text = self.get_text(objects)
        print("(%s)[%s]: %s"%(
            datetime.now().strftime("%H:%M:%S"),
            self.name,
            text
        ))

    def warning(self, *objects):
        text = self.get_text(objects)
        print("[yellow](%s)[%s]: %s"%(
            datetime.now().strftime("%H:%M:%S"),
            self.name,
            text
        ))

    def error(self, *objects):
        text = self.get_text(objects)
        print("[red](%s)[%s]: %s"%(
            datetime.now().strftime("%H:%M:%S"),
            self.name,
            text
        ))

    def get_text(self, *objects):
        text = ""
        for object in objects:
            text += str(object) + " "
        return text[:-1]

