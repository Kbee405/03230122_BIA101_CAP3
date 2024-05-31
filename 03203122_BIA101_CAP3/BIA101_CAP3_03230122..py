#Github Repo link
#https://github.com/Kbee405/03230122_BIA101_CAP3.git

#Kinley Bidha
#BBI A
#03230122 

# Reference: 
# https://docs.python.org/3/tutorial/inputoutput.html #reading-and-writing-files
# https://docs.python.org/3/library/stdtypes.html#str.strip
# https://docs.python.org/3/tutorial/datastructures.html  #list-comprehensions
# https://docs.python.org/3/library/os.path.html    #os.path.exists
# https://docs.python.org/3/library/__main__.html

#Solution
#Solution score: 475853

# This line imports the os module, which provides a way to interact with the operating system.
import os

# This is a class definition for the fileSumAnalyzer class.
class FileSumAnalyzer:
# This is the constructor method, which is called when an object of this class is created.
    def __init__(self, file_path):
# It takes a file_path as a argument and initializes the object's file_path attribute with it.
       self.file_path = file_path
# It also calls the analyze_file method and stores its result in the sum_result attribute.
       self.sum_result = self.analyze_file()

# This method analyzes the contents of the file specified by the file_path attribute.
    def analyze_file(self):
    
    # It initializes the sum_value variable to 0.    
        sum_value = 0

     # It opens the file in read mode and assigns the file object to file_handler.
        with open(self.file_path, 'r') as file_handler:
           # It iterates over each line in the file.
           
            for line_content in file_handler:
        # it removes any leading or  trailing whitespace characters from the line.
                line_content = line_content.strip()
    # if the line is not empty, ir calls the exact_number method and adds the result to the sum_value variable.
                if line_content:
                    sum_value += self.extract_number(line_content)
     # After iterating over all lines, it return the sum_value   
        return sum_value
 # This method takes a line of text as input and returns a number based on the following rules:
    def extract_number(self, line_content):
# It creates a list of digits present in the line using a list comprehension.
        digit_list = [int(char) for char in line_content if char.isdigit()]
# It creates a list of digits present in the line using a list comprehension.
        if len(digit_list) >= 2:
            return digit_list[0] * 10 + digit_list[-1]
 # If the list has fewer than two digits, it returns 0.       
        return 0

    def display_result(self):
        print(f"Sum of numbers in file {self.file_path}: {self.sum_result}")

def execute_analysis(file_path):
    if os.path.exists(file_path):
        analyzer = FileSumAnalyzer(file_path)
        analyzer.display_result()
    else:
        print(f"File {file_path} not found.")
# This is a special block of code that runs when the script is executed directly (not imported as a module).
if __name__ == "__main__":
# It sets the file_path variable to "03203122_BIA101_CAP3/112.txt".
    file_path = "03203122_BIA101_CAP3/112.txt"
    
    execute_analysis(file_path)
