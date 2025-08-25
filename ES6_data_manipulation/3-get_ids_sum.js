export default function getStudentIdsSum(arr = []) {
  if (!Array.isArray(arr)) {
    return [];
  }
  else {
    return arr.reduce((accumulator, currentValue) => {
      return accumulator + currentValue.id
    }, 0);
  }
}
