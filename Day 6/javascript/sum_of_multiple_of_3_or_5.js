// # Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17.

number = 17;
let sum = 0;
for (let i = 1; i <= number; i++) {
    if(i%3==0 || i%5==0)
        sum += i;
}
console.log('The sum of natural numbers:', sum);   