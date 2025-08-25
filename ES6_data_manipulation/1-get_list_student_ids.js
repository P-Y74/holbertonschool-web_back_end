export default function getListStudentIds(arr = []) {
  if (!Array.isArray(arr)) {
    return [];
  }
  else {
    return arr.map(student => student.id);
  }
}
