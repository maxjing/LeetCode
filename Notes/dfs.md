## Binary Tree Related DFS

### 1. No DFS Helper

**LeetCode 112: Path Sum**

```python
def hasPathSum(self, root: TreeNode, sum: int) -> bool:
  if not root:
    return False
  if root.left is None and root.right is None:
    return root.val == sum
  return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
```

1. start from the root

2. check if root is None, if not do two things:

   - subtract the target value by current node.val sum = sum - node.val
   - Make two recursive calls for both the children of the current node with the new number calculated in the previous step

3. At every step check if node is leaf, and it's value equals to target, if so return true to parent

4. if node is leaf but value not equals to target, return false to parent

   ​       12 								12 -> 7 -> 9 -> return false -> 10 -> 1 ->return true

   ​      /    \

   ​     7     1

      /  \     /

   9    10   5

   

**LeetCode 104: Maximum Depth of Binary Tree**

```python
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
```



---

### 2. Global List

**LeetCode 113: Path Sum II**

```python
def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
  res = []
  self.dfs(root, sum, [],res)
  return res

def dfs(self, node, target, currentPath, res):
  if node is None:
  return
  if node.left is None and node.right is None and node.val == target:
  res.append(currentPath + [node.val])
  self.dfs(node.left, target - node.val, currentPath + [node.val], res)
  self.dfs(node.right, target - node.val, currentPath + [node.val], res)
```



**LeetCode 257:Binary Tree Paths**

```python
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        self.findAllPaths(root, [], paths)
        return paths

    def findAllPaths(self, node, currentPath, paths):
        if node is None:
            return
        currentPath.append(str(node.val))
        if node.left is None and node.right is None:
            paths.append("->".join(currentPath))
        else:
            self.findAllPaths(node.left, currentPath, paths)
            self.findAllPaths(node.right, currentPath, paths)
        del currentPath[-1]
```

Differences from 112 are:

1. need to record the path
2. use global list, and being updated through dfs
3. Normally when return a list of paths, use global list （backtracking）

---

### 3. DFS Helper Contains Return

**LeetCode 543. Diameter of Binary Tree**

```python
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root)
        return self.dfs(root)
    
    def dfs(self, node):
        if node is None:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.res = max(self.res, left + right)
        
        return max(left, right) + 1
       
```

**LeetCode 124. Binary Tree Maximum Path Sum**

```python
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -math.inf
        self.dfs(root)
        return self.res
    
    def dfs(self, node):
        if node is None:
            return 0
        left = max(self.dfs(node.left), 0)
        right = max(self.dfs(node.right), 0)
        self.res = max(self.res, left + right + node.val)
        
        return node.val + max(left, right)
```



Solutions of the two questions are similar, different from 112 and 113

1. there is a return in dfs method
2. 当出现需要判断当前的node作为turning point或者不是的时候，需要2 steps:
   - 判断当前与global res 大小，假设这个node就是终点
   - 如果这个弄的不是终点，那它需要返回给parent，就是最后的return， return给parent

