class Node(object):
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.keys = {key}
        self.value = value
        
class AllOne:
    def __init__(self):
        self.value2node = {}
        self.dic = {} 
        self.max = None  
        self.min = None
        
    def inc(self, key: str) -> None:
        if key in self.dic:
            node = self.dic[key]
            value = node.value + 1
            node.keys.remove(key)
            
            if node.next and node.next.value == value:
                node.next.keys.add(key)
            else:
                tnode = Node(key, value)
                self.insert(True, node, tnode)
                if self.max < value:
                    self.max = value
            self.dic[key] =node.next
            
            if len(node.keys) == 0:
                self.delete(node)
        
        else:
            if 1 in self.value2node:
                self.value2node[1].keys.add(key)
                self.dic[key] = self.value2node[1]
            else:
                self.value2node[1] = self.dic[key] = Node(key, 1)
                if self.min: 
                    node = self.value2node[self.min]
                    self.insert(False, node, self.value2node[1])
                self.min = 1
                if self.max==None:
                    self.max=1
        
    def dec(self, key: str) -> None:
        if key not in self.dic:
            return
        node = self.dic[key]
        del self.dic[key]
        node.keys.remove(key)
        value = node.value - 1
        
        if value > 0:
            if node.prev and node.prev.value == value: 
                node.prev.keys.add(key)
            else:
                self.insert(False, node, Node(key, value))
                if self.min > value:
                    self.min = value
                    self.value2node[self.min]=node.prev
            self.dic[key] = node.prev
        
        if len(node.keys) == 0:
            self.delete(node)
        
    def getMaxKey(self) -> str:
        if not self.max:
            return ""
        for key in self.value2node[self.max].keys:
            return key
        
    def getMinKey(self) -> str:
        if not self.min:
            return ""
        for key in self.value2node[self.min].keys:
            return key
        
    def delete(self, n1):
        del self.value2node[n1.value]
        
        if n1.value == self.min:
            if n1.next:
                self.min = n1.next.value
            else:
                self.min = None
        
        if n1.value == self.max:
            if n1.prev:
                self.max = n1.prev.value
            else:
                self.max = None
        
        n1next = n1.next
        n1prev = n1.prev
        
        if n1next:
            n1next.prev = n1prev
        if n1prev:
            n1prev.next = n1next

    def insert(self, nxt, node, new): 
        self.value2node[new.value] = new
        if not self.min:self.min=new.value
        self.min=min(self.min,new.value)
        if not self.max:self.max=new.value
        self.max=max(self.max,new.value)
        
        if nxt:
            nodenxt = node.next
            node.next = new
            new.prev = node
            new.next = nodenxt
            if nodenxt:
                nodenxt.prev = new
        
        else:
            nodeprev = node.prev
            node.prev = new
            new.next = node
            new.prev = nodeprev
            if nodeprev:
                nodeprev.next = node
