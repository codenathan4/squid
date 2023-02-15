class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.peek_item = None
        self.peek_called = False

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peek_called:
            self.peek_item = self.iter.next()
            self.peek_called = True
            
        return self.peek_item

    def next(self):
        """
        :rtype: int
        """
        if self.peek_called:
            self.peek_called = False
        else:
            self.peek_item = self.iter.next()
        
        return self.peek_item

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peek_called and not self.iter.hasNext():
            return True
        else:
            return self.iter.hasNext()
