"""You have a background class that sends out notification to users. You want to implement a singleton pattern
ensuring that only a single instance is created for the class.
"""


class BackgroundWorker:
    _instance = None

    @staticmethod
    def getInstance():
        if BackgroundWorker._instance is None:
            BackgroundWorker()
        else:
            return BackgroundWorker._instance

    def __init__(self):
        if BackgroundWorker._instance != None:
            raise Exception("BackgroundWorker instance already exists")
        else:
            BackgroundWorker._instance = self
        self.message = None
        self.user = None

    def sendMessage(self, message, user):
        self.message = message
        self.user = user
        print(f'Sending {message} to {user}')


notification = BackgroundWorker()
notification.sendMessage("Hello", "User")

