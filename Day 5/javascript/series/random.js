// Random: A, BB, CCC, DDDD, EEEEE, FFFFF….n

let string = "";
for (let i = 1; i <= 5; i++) {
  for (let j = 0; j < i; j++) {
    string += String.fromCharCode((i - 1) + 65);
  }
  string += ",";
}
console.log(string);