#!/usr/bin/env ruby

# Check if there is exactly one argument
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <input>"
  exit 1
end

# Extract the input from the command-line argument
input = ARGV[0]

# Define the regular expression pattern
pattern = /School/

# Use the match method to find the first occurrence of the pattern in the input
match = input.match(pattern)

# Output the result or an empty string if no match is found
puts match ? match[0] : ""
