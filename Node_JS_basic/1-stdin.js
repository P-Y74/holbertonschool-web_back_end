console.log('Welcome to Holberton School, what is your name?')
process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  process.stdout.write('Your name is: ')
  console.log(`${name}`);
});
process.stdin.on('end', () => {
  console.log('This important software is now closing');
})
process.on('SIGINT', () => {
  console.log('This important software is now closing');
  process.exit();
})
