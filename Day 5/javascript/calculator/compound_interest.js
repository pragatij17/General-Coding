// Compound Interest:
// Input: time, rate and principal
// Output: interest

function compoundInterest(p, r, t, n){
    var amount = p * (Math.pow((1 + (r / n)), (n * t)));
    var interest =amount-p;
    return (interest);
}
console.log(compoundInterest(2000,0.08,5,12));