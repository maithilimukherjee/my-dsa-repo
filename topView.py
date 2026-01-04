def topView(root):
    if root is None:
        return
        
    q = [(root, 0)]      # queue for bfs: (node, horizontal distance)
    mp = {}              # map: hd -> first visible node
    
    while q:
        node, hd = q.pop(0)
        
        if hd not in mp:
            mp[hd] = node.info
        
        if node.left:
            q.append((node.left, hd - 1))
                
        if node.right:
            q.append((node.right, hd + 1))
      
    for key in sorted(mp):
        print(mp[key], end=" ")
