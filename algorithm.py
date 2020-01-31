import heapq


class Algorithm(object):

    def __init__(self, startvertex, targetvertex):
        self.startvertex = startvertex
        self.targetvertex = targetvertex

    def calculateShortestPath(self, vertexList):

        queue = []
        self.startvertex.minDistance = 0
        heapq.heappush(queue, self.startvertex)

        while len(queue) > 0:

            actualVertex = heapq.heappop(queue)

            for edge in actualVertex.adjacenciesList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    heapq.heappush(queue, v)

    def getShortestPath(self):

        print("Shortest path to target is:", self.targetvertex.minDistance)

        node = self.targetvertex

        while node is not None:
            if node.name == "A":
                print(f"{node.name}", end="")
                break
            print(f"{node.name} -> ", end="")
            node = node.predecessor
