//to check if given number is even or odd

let n= prompt("enter the value");
n=Number(n);    
if(n%2==0) console.log('even');
else    console.log('odd');

//check which one is greatest among three
let input=prompt('enter the three values')
let [a,b,c]=input.split(' ').map((value)=>Number(value));

if ((a>b) & (a>c) ) console.log(`${a} is greater`);
else if (b>c)   console.log(`${b} is greater`);
else console.log(`${c} is greater`); 

//arrange three in ascending order 

let input1=prompt('enter the three values')
let [a1,b1,c1]=input.split(' ').map((value)=>{Number(value)});

if ((a1>b1) && (a1>c1))
    {
        if(b1>c1) console.log(`${c},${b},${a}`)
        else console.log(`${b},${c},${a}`)
    }
else if ((b1>c1) && (b1>a1))
    {
        if(a1>c1)   console.log(`${c},${a},${b}`);
        else console.log(`${a},${c},${b}`);
    }
else
{
    if(a1>b1)   console.log(`${b},${a},${c}`);
    else    console.log(`${a},${b},${c}`);
}
