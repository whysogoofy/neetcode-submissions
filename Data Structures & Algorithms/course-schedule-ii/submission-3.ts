class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {number[]}
     */
    findOrder(numCourses: number, prerequisites: number[][]): number[] {
    // Step 1: Build Adjacency List
    const adj: number[][] = Array.from({ length: numCourses }, () => []);
    for (const [course, prereq] of prerequisites) {
        adj[prereq].push(course); // prereq -> course
    }

    // State array: 0 = Unvisited, 1 = Visiting, 2 = Visited
    const state: number[] = new Array(numCourses).fill(0);
    const result: number[] = [];

    // Step 2: DFS Helper Function
    function hasCycle(node: number): boolean {
        state[node] = 1; // Mark as VISITING (enter call stack)

        for (const neighbor of adj[node]) {
            // Cycle condition: encountered a node currently in active stack
            if (state[neighbor] === 1) return true;
            
            // Unvisited node: recursively visit
            if (state[neighbor] === 0 && hasCycle(neighbor)) return true;
        }

        state[node] = 2;   // Mark as VISITED (exit call stack)
        result.push(node); // Post-order record
        return false;
    }

    // Step 3: Run DFS from every unvisited node
    for (let i = 0; i < numCourses; i++) {
        if (state[i] === 0) {
            if (hasCycle(i)) return []; // Return empty array if any cycle found
        }
    }

    // Step 4: Reverse post-order result to get true topological order
    return result.reverse();
}
}
