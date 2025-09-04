import fs from 'fs';

export default function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      const studentsByFields = {};
      students.forEach((line) => {
        const columns = line.split(',');
        const firstname = columns[0];
        const field = columns[columns.length - 1];

        if (!studentsByFields[field]) {
          studentsByFields[field] = [];
        }
        studentsByFields[field].push(firstname);
      });
      resolve(studentsByFields);
    });
  });
}
