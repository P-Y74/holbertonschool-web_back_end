export default function appendToEachArrayValue(array, appendString) {
  let newArray = []
  for (let value of array) {
    let modifiedValue = appendString + value
    newArray.push(modifiedValue)
  }

  return newArray;
}
