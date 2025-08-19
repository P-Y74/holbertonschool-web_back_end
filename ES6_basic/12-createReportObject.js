export default function createReportObject(employeesList) {
  let object = {
    allEmployees: employeesList,
    getNumberOfDepartments() {
      return Object.keys(employeesList).length;
    },
  };
  return object;
}
