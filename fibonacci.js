function* fibonacci() {
  let a = 1;
  let b = 1;

  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}
sequence = fibonacci();
for (let i = 1; i < 10; i++) {
  console.log(sequence.next().value);
}
