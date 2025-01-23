function findCommonElements(arr1, arr2) {
    let commonElements = [];


    for (let i = 0; i < arr1.length; i++) {
        // Check if the current element of arr1 is in arr2
        if (arr2.includes(arr1[i])) {
            // If it is, push it to the commonElements array
            commonElements.push(arr1[i]);
        }
    }

    if (commonElements.length > 0) {
        console.log("Common elements:", commonElements);
    } else {
        console.log("No common elements found.");
    }
}

let array1 = [1, 2, 3, 4, 5];
let array2 = [3, 4, 5, 6, 7];

findCommonElements(array1, array2);
