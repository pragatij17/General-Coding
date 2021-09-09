// Random: 1,11,111,1111,11111,111111...n

var x=0;
var i;
var a = '';
for(i=0;i<=10;i++){
      x=x*10+1;
      if(i==10){
        a+=x;
      }
      else{
        a+=x+",";
      }
}
console.log(a);

