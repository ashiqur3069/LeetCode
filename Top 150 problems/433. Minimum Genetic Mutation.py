class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        bank = set(bank)
        if endGene not in bank:
            return -1
        queue = deque([(startGene, 0)])
        visited = {startGene}
        while queue:
            gene, level = queue.popleft()
            if gene == endGene:
                return level
            for i in range(len(gene)):
                for letter in 'ACGT':
                    new_gene = gene[:i] + letter + gene[i+1:]
                    if new_gene not in visited and new_gene in bank:
                        queue.append((new_gene, level+1))
                        visited.add(new_gene)
        return -1
