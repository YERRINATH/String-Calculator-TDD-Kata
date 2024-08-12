import re


def add(numbers):
    if not numbers:
        return 0

    # Default delimiters
    delimiter = r'[,\n]'

    # Handle custom delimiters
    if numbers.startswith('//'):
        delimiter_part, numbers = numbers[2:].split('\n', 1)
        if delimiter_part:
            # Check for multiple delimiters with or without special characters
            delimiters = re.findall(r'\[(.*?)\]', delimiter_part)
            if delimiters:
                # Filter out empty delimiters and construct the regex pattern
                delimiters = [d for d in delimiters if d]
                if delimiters:
                    delimiter = '|'.join(map(re.escape, delimiters))
            elif delimiter_part:  # Handle the case of non-bracketed single-character delimiters
                delimiter = re.escape(delimiter_part)

    # Split numbers by the delimiter
    num_list = re.split(delimiter, numbers)

    # Initialize lists for valid numbers and negative numbers
    nums, negatives = [], []

    for num in num_list:
        if num.strip():  # Skip empty strings or whitespace
            number = int(num)
            if number < 0:
                negatives.append(number)
            elif number <= 1000:  # Ignore numbers greater than 1000
                nums.append(number)

    # Raise an error if any negative numbers are found
    if negatives:
        raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negatives))}")

    # Return the sum of the valid numbers
    return sum(nums)
