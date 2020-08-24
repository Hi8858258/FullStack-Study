# Python 数据结构

## 一. 二叉树

```python
class Node():
    '''节点类'''
    def __init__(self,value):
        self.value = value
        self.lchild = None
        self.rchild = None
```

```python
class Tree()：
	'''二叉树'''
     def __init__(self):
        self.root = None
     def add(self,item)：
    	node = None(item)
        queue = [self.root]
        
        cur_node = queue.pop[0]
        if cur_node.lchild is None:
            cur_node.lchild = node
            return
        else:
            queue.append(cur_node.lchild)
```

