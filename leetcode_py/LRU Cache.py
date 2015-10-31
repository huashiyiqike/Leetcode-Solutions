class LRUCache:
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        val = self.cache[key]
        del self.cache[key]
        self.cache[key] = val
        return val

    def set(self, key, value):
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


from collections import defaultdict

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def front_push(self, node):
        if self.head:
            node.next = self.head
            self.head.pre = node
        else:
            self.tail = node
        self.head = node

    def delete(self, node):
        if node.pre:
            node.pre.next = node.next
        if node.next:
            node.next.pre = node.pre
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.pre


class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.pre = None


class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.queue = LinkedList()
        self.dict = defaultdict(Node)
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        if key in self.dict:
            self.queue.delete(self.dict[key])
            self.dict[key].pre, self.dict[key].next = None, None  # can be moved to List operation
            self.queue.front_push(self.dict[key])
            return self.dict[key].val
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.dict:
            self.queue.delete(self.dict[key])
        else:
            if len(self.dict) == self.capacity:
                del self.dict[self.queue.tail.key]
                self.queue.delete(self.queue.tail)
        self.dict[key] = Node(key, value)
        self.queue.front_push(self.dict[key])


class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.pre = None
        self.next = None


class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.dicts = {}
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        res = -1
        tmphead = self.dicts.get(key)
        if tmphead != None:
            res = tmphead.val
            self.movetohead(tmphead)

        return res

    def movetohead(self, tmphead):
        if self.head != tmphead:
            tmphead.pre.next = tmphead.next
            if self.tail != tmphead:
                tmphead.next.pre = tmphead.pre
            else:
                self.tail = self.tail.pre
            tmphead.next = self.head
            self.head.pre = tmphead
            self.head = tmphead

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        tmphead = self.dicts.get(key)
        if tmphead != None:
            tmphead.val = value
            self.movetohead(tmphead)

        else:
            tmphead = Node(key, value)

            if len(self.dicts) == self.capacity:
                print self.dicts.pop(self.tail.key).val
                if self.tail.pre:
                    self.tail.pre.next = None
                    self.tail = self.tail.pre
                else:
                    self.tail = tmphead

            if self.head != None:
                tmphead.next = self.head
                self.head.pre = tmphead
                self.head = tmphead
            else:
                self.head = tmphead
                self.tail = tmphead

            self.dicts[key] = tmphead


if __name__ == "__main__":
    a = LRUCache(3)
    a.set(7, 7)
    a.set(0, 0)
    a.set(1, 1)
    a.set(2, 2)
    a.get(0)
    a.set(3, 3)
    a.set(0, 0)
    a.set(4, 4)
