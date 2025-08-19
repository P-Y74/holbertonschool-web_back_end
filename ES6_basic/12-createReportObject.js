export default function createReportObject(employeesList) {
  let object = {
    allEmployees: employeesList,
    getNumberOfDepartments() {
      return Object.keys(this.allEmployees).length;
    }
  };
  return object;
}
