const readline = require('readline');
const MAX_CHAR=256

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});



ing = chr => {
    return chr.charCodeAt(0)
}

score = chr => {
    if (ing(chr) >= ing('a') && ing(chr) <= ing('z')){
        return ing(chr) - ing('a') + 1
    }
    else {
        return ing(chr) - ing('A') + 27
    }
}
sum=0
num=0
tot_sum=0
grp = [

            'NGWdQgDDHGJgQLznzzsJFFzvzB',
'twRCpZVjVWqVSqVwwjtZfrrfntfvznBssBncfLrc',
 'jRRwCqwCZhlhZRpSZpjSqWwqmDMQdMmHPQQMHGdlHdTldNGd',
]
times=0
rl.on('line', (line) => {
    console.log(num)
    if (!num) {
    console.log("times")
    console.log(++times)
        console.log(grp)
        if (grp.length > 0) {            
        console.log((commonCharacters(grp,3)[0]))
        console.log(score(commonCharacters(grp,3)[0]))
        arr=commonCharacters(grp,3)
        
        for (g of arr[0]) {
            tot_sum=tot_sum+score(g)
        }
        grp=[]
        console.log(tot_sum)
        }
    }
    seen = []
            grp.push(line)
    n=line.length/2
    compartment1= line.substring(0,n);

    compartment2 = line.substring(n,line.length);
    for (i=0;i<n;i++) {
        for (j=0;j<n;j++) {
            if (ing(compartment1.charAt(i)) == ing(compartment2.charAt(j)) && !seen.includes(compartment1.charAt(i))) {
                sum = sum + score(compartment1.charAt(i))
                seen.push(compartment1.charAt(i))
            }
        }
    }
    num=(num+1)%3
});

rl.once('close', () => {
    console.log(tot_sum)
     // end of input
 });

function commonCharacters(strings, n) {
     
    // primary array for common characters
    // we assume all characters are seen before.
    let prim = new Array(MAX_CHAR).fill(true)
     
    // for each strings
    for(let i = 0; i < n; i++){
         
        // secondary array for common characters
        // Initially marked false
        let sec = new Array(MAX_CHAR).fill(false)
 
        // for every character of ith strings
        for(let j = 0; j < strings[i].length; j++){
 
            // if character is present in all
            // strings before, mark it.
            if (prim[strings[i].charCodeAt(j)])
                sec[strings[i].charCodeAt(j)] = true
        }
 
        // copy whole secondary array
        // into primary
        for(let i = 0; i < MAX_CHAR; i++){
            prim[i] = sec[i]
        }
    }
 
    list = []
    // displaying common characters
    for(let i = 0; i < 256; i++){
        if (prim[i]) {
            list.push(String.fromCharCode(i)," ")
        }
    }

    return list
}
