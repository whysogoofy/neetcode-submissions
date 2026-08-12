class Solution {
    /**
     * @param {number[]} arr
     * @param {number} k
     * @param {number} x
     * @return {number[]}
     */

    findClosestElements(arr: number[], k: number, x: number): number[] {
        let left = 0;
        let right = arr.length - k;

        // Binary search to find the optimal starting index of the k-element window
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (x - arr[mid] > arr[mid + k] - x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return arr.slice(left, left + k);
    }
}
