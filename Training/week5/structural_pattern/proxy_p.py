class RealSubject:
    def request(self):
        print("RealSubject: Handling request")

class Proxy:
    def __init__(self):
        self._real_subject = RealSubject()

    def request(self):
        print("Proxy: Checking access")
        self._real_subject.request()

if __name__ == "__main__":
    proxy = Proxy()
    proxy.request()