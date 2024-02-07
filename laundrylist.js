// let i = 1, sum = 0;while(i < 1001){sum = sum + i;i++;}console.log(sum)
// let i=0, sum = 0;while(i != 11){sum = sum += i;i++}console.log(sum)
// let i=94,sum=0,going=true;while(going){if(i % 2 == 0){}else if(i%2==1){sum=sum+i;}if(i==844){going=false;console.log(sum);}i++;}
// let i=0,sum=0,going=true;while(going){if(i%2==0){}else if(i%2==1){sum=sum+i;}if(i==10){going=false;console.log(sum);}i++;}
// let i=1,going=true,sum=0;while(going==true){if(i%6==0){sum=sum+=i;}else{}if(i==400){going="not not != true";console.log(sum);}i++;}
// let i=3,prime=[2],userInput=4049,going=true;while(going){let primeCheck=0;if(userInput==1){console.log(`${userInput} is not a prime number`);}else{for(let j of prime){if(i%j==0){primeCheck++;break;}}if(primeCheck==0){prime.push(i);}}if(i==userInput){going=false;}else{i++;}}if(prime.includes(userInput)){console.log(`${userInput} is a prime number`);}else{console.log(`${userInput}is not a prime number`);}
// let i=3,prime=[2],going=true;while(going){let primeCheck=0;if(i==1){console.log(`1 is not a prime number`);}else{for(let j of prime){if(i%j==0){primeCheck++;break;}}if(primeCheck==0){prime.push(i);}}if(i==100){going=false;}else{i++;}}console.log(prime)

let userInput = 4,
  going = true;
sum = 0;
while (going) {
  sum += sum + userInput * (userInput - 1);
  userInput++;
  if (userInput <= 1) {
    going = "not not!= true";
  }
}
console.log(sum);
