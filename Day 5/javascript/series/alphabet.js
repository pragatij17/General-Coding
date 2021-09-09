// Alphabets: A,B,C,D,E,F,G,H,I….n

var a='';
for(k = 65; k < 91; k++){
    var str=String.fromCharCode(k);
    if(k==90){
        a+=str;
        }
        else{
        a+=str+',';
        }
    }
console.log(a);
