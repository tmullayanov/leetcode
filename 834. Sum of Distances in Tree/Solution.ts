// Floyd-Warshall. Consumes too much memory and computes for too much time.
function sumOfDistancesInTreeWFI(n: number, edges: number[][]): number[] {
  const distances: number[][] = [];
  for (let i = 0; i < n; i++) {
    distances.push(Array(n).fill(Infinity));
  }

  for (let i = 0; i < n; i++) {
    distances[i][i] = 0;
  }

  for (const [i, v] of edges) {
    distances[i][v] = 1;
    distances[v][i] = 1;
  }

  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        distances[i][j] = Math.min(
          distances[i][j],
          distances[i][k] + distances[k][j]
        );
      }
    }
  }

  return distances.map((row) => row.reduce((acc, v) => acc + v));
}

function sumOfDistancesInTree(n: number, edges: number[][]): number[] {
  const count = Array(n).fill(1);
  const graph = Array(n);
  const result = Array(n).fill(0);

  for (let i = 0; i < n; i++) {
    graph[i] = new Set();
  }

  for (const [lhs, rhs] of edges) {
    graph[lhs].add(rhs);
    graph[rhs].add(lhs);
  }

  function dfs(node: number, parent: number) {
    for (let child of graph[node]) {
      if (child != parent) {
        dfs(child, node);
        count[node] += count[child];
        result[node] += result[child] + count[child];
        /**
         * result[NODE] is correct for subtree with NODE as it's root.
         * result[NODE] + count[NODE] will be correct summand for it's subtree for NODE's parent:
         * it's result[NODE] for getting all distances from NODE subtree + extra edge between NODE and NODE's parent
         * for each vertex inside (which is count[NODE])
         * This way, result[ROOT] is correct for ROOT (starting point)
         */
        console.log(
          `dfs. at node=${node}. result=${JSON.stringify(
            result
          )}, count=${JSON.stringify(count)}}`
        );
      }
    }
  }

  function dfs2(node: number, parent: number) {
    for (let child of graph[node]) {
      if (child != parent) {
        /**
         * if result[NODE] is correct, the result[CHILD] is derived from result[NODE] following this:
         * 1. We have to exclude edge [NODE, CHILD] from the result[NODE] for each vertex in CHILD subtree
         * (and this equals count[CHILD])
         * 2. We have to add edge [NODE, CHILD] for each vertex outside CHILD subtree
         * (and this equals N - count[CHILD])
         * So the final formula is this:
         * result[CHILD] = result[NODE] - count[CHILD] + N - count[CHILD]
         */
        result[child] = result[node] - count[child] + n - count[child];
        dfs2(child, node);
        console.log(
          `dfs2. at node=${node}. result=${JSON.stringify(
            result
          )}, count=${JSON.stringify(count)}}`
        );
      }
    }
  }

  console.log(graph);
  dfs(0, -1);
  console.log('----------');
  dfs2(0, -1);

  return result;
}

const main = () => {
  const tests = [
    {
      n: 6,
      edges: [
        [0, 1],
        [0, 2],
        [2, 3],
        [2, 4],
        [2, 5],
      ],
      expected: [8, 12, 6, 10, 10, 10],
    },
  ];

  for (const { n, edges, expected } of tests) {
    const result = sumOfDistancesInTree(n, edges);
    console.log(`+++\nexpected=[${expected}]\nactual=[${result}]\n+++\n`);
  }
};

main();
