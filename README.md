# Domain-Checker

Domain Checker is a Python script that checks the availability of domains listed in a file and saves the working domains to another file.

## Features

- Checks domains listed in a file for availability.
- Displays progress with a colorful progress bar.
- Saves the working domains to a specified file.
- Provides estimated time to complete the process.
- Adds a touch of fun with a LOLCat image!

## Requirements

- Python 3.x
- `requests` library
- `tqdm` library
- `colorama` library

You can install the required libraries by running:

pip install -r requirements.txt

## Usage

1. Make sure you have Python installed on your system.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Prepare a file containing a list of domains, with each domain on a separate line.
4. Run the script by executing the following command:

python domain_checker.py

5. Follow the on-screen prompts to provide the input filename containing the list of domains and the output filename to save the working domains.
6. Sit back, relax, and watch the progress as the script checks the domains!
7. Once the process is complete, you'll see the working domains displayed, and you'll have the option to save them to a file.

## Example

$ python domain_checker.py
Enter the filename containing the list of domains: input_domains.txt
Enter the filename to save the working domains: output_domains.txt
Checking domains: 100%|███████████████████████████████████████████████████████████| 10/10 [00:02<00:00, 4.12domain/s]

/_/\
( o.o )

^ <

Working domains:
example.com
subdomain.example.com

Process complete!
Do you want to save the working domains to a file? (y/n): y
Working domains saved to output_domains.txt

Total elapsed time: 2.34 seconds
Estimated time to complete: 10.00 seconds
