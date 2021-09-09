// Fibonacci Series: 1,1,2,3,5,8...n

var n1 = 0, n2 = 1, nextTerm;
for (var i = 1; i <= 10; i++) {
    console.log(n1);
    nextTerm = n1 + n2;
    n1 = n2;
    n2 = nextTerm;
}