const fs = require('fs');

function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, 'utf8');
    let lines = data.split('\n');
    lines = lines.filter((line) => line.trim() !== '');
    const students = lines.slice(1);
    const total = students.length;
    console.log(`Number of students: ${total}`);

    const studentsByFields = {};
    students.forEach((line) => {
      const columns = line.split(',');
      const firstname = columns[0];
      const fields = columns[columns.length - 1];

      if (!studentsByFields[fields]) {
        studentsByFields[fields] = [];
      }
      studentsByFields[fields].push(firstname);
    });
    for (const field in studentsByFields) {
      if (Object.prototype.hasOwnProperty.call(studentsByFields, field)) {
        const list = studentsByFields[field];
        const count = list.length;
        console.log(`Number of students in ${field}: ${count}. List: ${list.join(', ')}`);
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;
