#!/usr/bin/node
// Get the command line arguments
const args = process.argv.slice(2);

// Check if exactly two arguments are passed
if (args.length === 2)
{
    // Print the arguments in the specified format
    console.log(`${args[0]} is ${args[1]}`);
}
