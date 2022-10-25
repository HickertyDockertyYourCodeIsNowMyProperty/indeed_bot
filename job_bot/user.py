from userDetails import EMAIL, PASSWORD

class User:
    def __init__(self):
        self.username = EMAIL
        self.password = PASSWORD
        self.keywords = None
        self.set_keywords()
        self.set_location()
        self.set_job_type()

    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password

    def set_keywords(self):
        self.keywords = input('enter in key words separated by commands: ').split(',')

    def set_location(self):
        self.location = input('enter in your location to search (optional): ')

    def set_job_type(self):
        self.job_type = input('enter in a job type (optional): ').strip()