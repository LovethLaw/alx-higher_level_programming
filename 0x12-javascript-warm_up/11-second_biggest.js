#!/usr/bin/node
const num = process.argv;
const newArray = [];

if (num.length === 3 || num[2] === undefined) {
  console.log(0);
} else {
  function iterateArray (num) {
    // check the length of the array

    let i;
    // loops through and append it value to a new array
    for (i = 2; i < num.length; i++) {
      newArray.push(Number(num[i]));
    }
  }

  // sorts the array of numbers
  function sortArray (num) {
    const sorted = num.slice().sort((a, b) => a - b);
    return sorted;
  }
  // returns the second bigest number in the list
  function secondBigest (sortedArray) {
    let i, least;
    for (i = 0; i < sortedArray.length - 1; i++) {
      least = i;
    }
    console.log(sortedArray[least]);
  }
  iterateArray(num);
  const sort = sortArray(newArray);
  secondBigest(sort);
}
