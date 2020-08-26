#------------------------------------------#
# Title: LAB06_C.py
# Desc: simple demonstrator for classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
#------------------------------------------#
import sys
import pickle

# -- DATA -- #
strFileInput = 'numbers.dat'
strFileOutput = 'results.dat'

# -- PROCESSING -- #
class SimpleMath:
    """A collection of simple math processing functions """

    @staticmethod
    def get_sum(val1 = 0.0, val2 = 0.0):
        """Function for adding two values


        Args:
            val1: the first number to add
            val2: the second number to add


        Returns:
            A float corresponding to the sum of val1 and val2
        """
        return float(val1 + val2)

    @staticmethod
    def get_diffference(val1 = 0.0, val2 = 0.0):
        """Function for subtracting two values


        Args:
            val1: the number to subtract from
            val2: the number to subtract


        Returns:
            A float corresponding to the difference of val1 and val2
        """
        return float(val1 - val2)

    @staticmethod
    def get_product(val1 = 0.0, val2 = 0.0):
        """Function for multiplying two values


        Args:
            val1: the first number to multiply
            val2: the second number to multiply


        Returns:
            A float corresponding to the product of val1 and val2
        """
        return float(val1 * val2)

    @staticmethod
    def get_quotient(val1 = 0.0, val2 = 0.0):
        """Function for dividing two values


        Args:
            val1: the number to divide
            val2: the number to divide by


        Returns:
            A float corresponding to the quotient of val1 and val2
        """
        return float(val1 / val2)

class IO:
    """A collection of the Input / Output operations """

    @staticmethod
    def read_file(fileName):
        """
        function to read in two numbers from file fileName and return these

        Args:
            fileName (string): file name to read the numbers from

        Returns:
            numA (int): first number in file fileName.
            numB (int): second number in file fileName.

        """

        with open(fileName, 'rb') as fileObj:
            data = pickle.load(fileObj) #note: load() loads one line of data
        return data

    @staticmethod
    def write_file(fileName, results):
        """
        function to write the math results to file fileName

        Args:
            fileName (string): file Name to write the results to.
            results (list): The results

        Returns:
            None.

        """

        with open(fileName, 'wb') as fileObj:
            pickle.dump(results, fileObj)
            

    @staticmethod
    def IO(strFileInput):
        try:
            print(IO.read_file(strFileInput))
            print(IO.read_file(strFileInput))
        except:
            pass
        print("please input two numbers to replace current numbers")
        num1 = input('num1: ')
        num2 = input('num2: ')
        num1 = int(num1)
        num2 = int(num2)
        with open(strFileInput, 'wb') as fileObj:
            pickle.dump(num1, fileObj)
        with open(strFileInput, 'ab') as fileObj:
            pickle.dump(num2, fileObj)
        pass

    @staticmethod
    def calc(strFileInput,strFileOutput):
        print('Basic Math script. Calculating the Sum, Difference, Product and Quotient of two numbers.')
        intNumA, intNumB = IO.read_file(strFileInput)
        lstResults = []
        lstResults.append(SimpleMath.get_sum(intNumA, intNumB))
        lstResults.append(SimpleMath.get_diffference(intNumA, intNumB))
        lstResults.append(SimpleMath.get_product(intNumA, intNumB))
        lstResults.append(SimpleMath.get_quotient(intNumA, intNumB))
        IO.write_file(strFileOutput, lstResults)

        # TODO add code to save results to file

# -- PRESENTATION (Input/Output) -- #


    
strArg = str(sys.argv[1])

if strArg == 'IO':
    IO.IO(strFileInput)
    pass
elif strArg == 'calc':
    IO.calc(strFileInput,strFileOutput)
    pass





