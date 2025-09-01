console.log('Welcome to Holberton School, what is your name?')
process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  process.stdout.write(`Your name is: ${name}\n`)
});
process.stdin.on('end', () => {
  console.log('This important software is now closing');
})
