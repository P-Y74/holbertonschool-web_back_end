export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this._name;
  }
  set name(nameValue) {
    if (typeof (nameValue) !== "string") throw new TypeError('Name must be a string');
    this._name = nameValue;
  }

  get length() {
    return this._length;
  }
  set length(lengthValue) {
    if (typeof (lengthValue) !== "number") throw new TypeError('Length must be a number');
    this._length = lengthValue;
  }

  get students() {
    return this._students;
  }
  set students(studentsValue) {
    if (!Array.isArray(studentsValue)) throw new TypeError('Student must be an array');
    this._students = studentsValue;
  }
}
