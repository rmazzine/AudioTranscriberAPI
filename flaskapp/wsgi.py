import sys
sys.path.append('../')  # Must have a best solution

from flaskapp.app import app as application

if __name__ == "__main__":
    application.run()