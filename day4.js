


//find min and max from the given array 

let values= prompt("enter the values seperated by comma's")
arr=values.split(' ').map(Number)
console.log(arr)
console.log(arr.length)
min=max=arr[0]
for (let i=0;i<arr.length;i++){
    if (arr[i]>max) max=arr[i]
    if(arr[i]<min)  min=arr[i]
}
console.log('min is ',min,'max is',max)





//find min and max from a given number 

let n= prompt('enter the values n ')
n=Number(n)

//  console.log(n,typeof(n))
// // b=Math.floor(n%10);
// // console.log(b)
// // n=Math.floor(n%10)
// // console.log(n)

min=9;
max=0;

while (n!=0){
    temp=Math.floor(n%10);
    if (temp>max)   max=temp
    if(temp<min)    min=temp
    n=Math.floor(n/10)   
}

console.log('min is',min,'max is',max)





//print sum of values in an array 

let values=prompt("enter the values seperated by spaces")
let arr=values.split(' ').map(Number)
// console.log(arr)

let sum=0
for (let i=0;i<arr.length;i++)  sum+=arr[i]
console.log(sum)



