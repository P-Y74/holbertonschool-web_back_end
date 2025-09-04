import readDatabase from '../utils';

export default class StudentsController {
  static async getAllStudents(req, res) {
    const dbPath = process.argv[2];
    try {
      const data = await readDatabase(dbPath);
      const sortedFields = Object.keys(data).sort((a, b) => a.toLowerCase()
        .localeCompare(b.toLowerCase()));
      const lines = ['This is the list of our students'];

      for (const field of sortedFields) {
        const list = data[field];
        const count = list.length;
        lines.push(`Number of students in ${field}: ${count}. List: ${list.join(', ')}`);
      }
      res.status(200).type('text');
      res.send(lines.join('\n'));
    } catch (err) {
      res.status(500).type('text');
      res.send('This is the list of our students\nCannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).type('text');
      res.send('Major parameter must be CS or SWE');
      return;
    }
    const dbPath = process.argv[2];
    try {
      const data = await readDatabase(dbPath);
      const list = data[major] || [];
      res.status(200).type('text');
      res.send(`List: ${list.join(', ')}`);
    } catch (err) {
      res.status(500).type('text');
      res.send('Cannot load the database');
    }
  }
}
