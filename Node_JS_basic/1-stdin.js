console.log('Welcome to Holberton School, what is your name?')
process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  process.stdout.write('Your name is: ')
  console.log(`${name}`);
  console.log('This important software is now closing')
  process.exit()
});

