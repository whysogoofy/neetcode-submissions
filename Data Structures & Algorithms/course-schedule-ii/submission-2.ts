class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {number[]}
     */

    // BFS Solution: Kahn’s Algorithm
    // Core Concept
    // Kahn’s algorithm works on the concept of in-degrees. The in-degree of a course is the number of prerequisites required before you can take it.

    // If a course has inDegree === 0, it means you can take it right now—there are no unmet prerequisites blocking you.

    // Once you "take" a course, you remove it from consideration and decrease the inDegree of all courses that depended on it.

    // If a dependent course's inDegree drops to 0, it is now ready to be taken, so you add it to your queue.

    findOrder(numCourses: number, prerequisites: number[][]): number[] {
        // Step 1: Build the Graph
        const adj: number[][] = Array.from({ length: numCourses }, () => []);
        const inDegree: number[] = new Array(numCourses).fill(0);

        for (const [course, prereq] of prerequisites) {
            adj[prereq].push(course); // Directed edge: prereq -> course
            inDegree[course]++;       // 'course' has one more prerequisite
        }

        // Step 2: Initialize Queue with 0-indegree nodes
        const queue: number[] = [];
        for (let i = 0; i < numCourses; i++) {
            if (inDegree[i] === 0) {
                queue.push(i);
            }
        }

        const result: number[] = [];
        let head = 0; // Pointer for O(1) dequeueing

        // Step 3: Process the Queue (BFS)
        while (head < queue.length) {
            const current = queue[head++];
            result.push(current); // Take the course

            // Reduce in-degree for all courses dependent on 'current'
            for (const neighbor of adj[current]) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] === 0) {
                    queue.push(neighbor); // Fully ready now!
                }
            }
        }

        // Step 4: Check for Cycles
        return result.length === numCourses ? result : [];
    }
}


// Execution Trace ExampleLet’s trace numCourses = 4, prerequisites = [[1,0], [2,0], [3,1], [3,2]]Graph Setup:Edges: 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3inDegree array: [0, 1, 1, 2] (Course 0 needs 0 prereqs; Course 3 needs 2)queue: [0] (Course 0 has inDegree == 0)result: []Loop Iteration 1:Dequeue 0. result becomes [0].Neighbors of 0 are 1 and 2.Decrement inDegree[1] from 1 to 0 $\rightarrow$ Push 1 to queue.Decrement inDegree[2] from 1 to 0 $\rightarrow$ Push 2 to queue.queue: [0, 1, 2], inDegree: [0, 0, 0, 2]Loop Iteration 2:Dequeue 1. result becomes [0, 1].Neighbor of 1 is 3.Decrement inDegree[3] from 2 to 1.inDegree[3] is not 0 yet, so don't push to queue.queue: [0, 1, 2], inDegree: [0, 0, 0, 1]Loop Iteration 3:Dequeue 2. result becomes [0, 1, 2].Neighbor of 2 is 3.Decrement inDegree[3] from 1 to 0 $\rightarrow$ Push 3 to queue.queue: [0, 1, 2, 3], inDegree: [0, 0, 0, 0]Loop Iteration 4:Dequeue 3. result becomes [0, 1, 2, 3]. No neighbors.Finish: result.length (4) matches numCourses (4) $\rightarrow$ Return [0, 1, 2, 3].
