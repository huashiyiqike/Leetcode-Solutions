<backquote><pre>
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
</backquote></pre>

Start by creating the dependency graph. Use your data structure to keep record of the number of incoming edges(for the deletion of the node if it equals 0, namely free courses) and the outgoing neighbors(for traversing). Then we create a stack or a queue to traverse. Put the free courses in first and removing its outgoing dependencies.Again keep record of the number of the deleted nodes while traversing. If all nodes can be deleted, that means we can find a way to take all courses.