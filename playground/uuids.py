import uuid

class UUID:
    def __init__(self):
        pass

    def uuid1(self):
        return uuid.uuid1()


if __name__ == '__main__':
    uuids = UUID()
    print(uuids.uuid1())