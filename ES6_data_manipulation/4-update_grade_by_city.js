export default function updateStudentGradeByCity(arr = [], city, newGrades) {
  if (!Array.isArray(arr)) {
    return [];
  }
  else {
    return arr.filter(student => student.location === city).map(student => {
      const gradeObj = newGrades.find(ng => ng.studentId === student.id);

      return {
        ...student,
        grade: gradeObj ? gradeObj.grade : ('N/A')
      };
    });
  }
}
