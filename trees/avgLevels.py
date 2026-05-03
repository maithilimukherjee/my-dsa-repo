class Solution(object):
    def averageOfLevels(self, root):
        if not root:
            return []

        res = []

        def bfs(nodes):
            if not nodes:
                return

            level_sum = 0
            next_nodes = []

            for node in nodes:
                level_sum += node.val

                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)

            res.append(level_sum / float(len(nodes)))

            if next_nodes:  
                bfs(next_nodes)

        bfs([root])
        return res
