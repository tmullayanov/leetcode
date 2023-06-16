function countAndSay(n: number): string {
  if (n == 1) {
    return '1';
  }

  const prevSolution = countAndSay(n - 1);
  let curSym = prevSolution[0];
  let curCount = 1;

  let result = '';

  for (let i = 1; i < prevSolution.length; i++) {
    if (prevSolution[i] === curSym) {
      curCount++;
    } else {
      result += String(curCount) + curSym;
      curCount = 1;
      curSym = prevSolution[i];
    }
  }
  result += String(curCount) + curSym;

  return result;
}

const tests: [number, string][] = [
  [1, '1'],
  [2, '11'],
  [3, '21'],
  [4, '1211'],
  [5, '111221'],
  [6, '312211'],
];

for (const [n, au] of tests) {
  const result = countAndSay(n);
  console.log(`n=${n} expected=${au}, got=${result}`);
  console.log(result === au ? 'OK' : 'FAIL');
}
