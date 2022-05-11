import EventLoop
import sys
import FileHandler
import app


def main():
    app.app.run("0.0.0.0", 5000)

if __name__ == '__main__':
    main()

