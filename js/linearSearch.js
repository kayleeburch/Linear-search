const arrayToSearchThrough = [];
for (let i = 1; i <= 1000; i++) {
    arrayToSearchThrough.push(i);
}

function linearSearch(valueToFind, arrayToSearchThrough) {
    let result = []
    for(let i = 0; i < arrayToSearchThrough.length; i++) {
        if(arrayToSearchThrough[i] === valueToFind) {
            result.push(i)
        }
    }
    console.log(result)
};

linearSearch("n", ["b", "a", "n", "a", "n", "a", "s"])


