import sys


try: # opening first file.

    with open(sys.argv[1], "r") as f:

        operands = f.readlines()

except IOError:

    try: # checks if second is file valid after printing error message.
        
        print("IOError: cannot open {}".format(sys.argv[1]))
        f = open(sys.argv[2], "r")
    
    except IOError:

        print("IOError: cannot open {}".format(sys.argv[2]))
    
    except IndexError:

        print("IndexError: number of input files less than expected.")
        
except IndexError:

    print("IndexError: number of input files less than expected.")

except:

    print("kaBOOM: run for your life!")

else:

    try: # opening second file.
        
        with open(sys.argv[2], "r") as f:

            comparison_data = f.readlines()
    
    except IndexError:

        print("IndexError: number of input files less than expected.")

    except IOError:

        print("IOError: cannot open {}".format(sys.argv[2]))

    except:

        print("kaBOOM: run for your life!")
    
    else:
        
        for i in range(len(operands)): # Going through operands.

            try:

                printed_string = "------------\n"
                given_numbers = [float(k) for k in operands[i].split()] # tries to change every element into a floating number gives value error when failed.
                
                if len(given_numbers) < 4: # checks number of elements raises IndexError if it is less than 4

                    raise(IndexError)

                #first four lines of code reformats operands into 4 different information and rounds them up to closest intager
                should_be_divisable = int(given_numbers[0]) if given_numbers[0] % 1 < 5 else int(given_numbers[0]) + 1
                should_not_be_divisable = int(given_numbers[1]) if given_numbers[1] % 1 < 5 else int(given_numbers[1]) + 1
                lower_limit = int(given_numbers[2]) if given_numbers[2] % 1 < 5 else int(given_numbers[2]) + 1
                upper_limit = int(given_numbers[3]) if given_numbers[3] % 1 < 5 else int(given_numbers[3]) + 1
                fiting_numbers = []
                test_numbers = comparison_data[i].split()

                if should_be_divisable == 0 or should_not_be_divisable == 0: # checks for zero division error. while this part is completely unnecessary it is more elegant in my opinion.

                    raise(ZeroDivisionError)

                for j in range(lower_limit,upper_limit+1): # finds which numbers in range checks all the conditions.

                    if j % should_be_divisable == 0 and j % should_not_be_divisable != 0:

                        fiting_numbers.append(str(j))

                printed_string += "My results:\t\t"
                
                for j in fiting_numbers: # prints numbers which fits all of the conditions

                    printed_string += j + " "
                
                printed_string = printed_string[:-1] + "\nResults to compare:\t"

                for j in test_numbers: # prints the numbers given by comparison_data.txt file
                    printed_string += j + " "
                
                printed_string = printed_string[:-1] + "\n"

                if test_numbers == fiting_numbers:
                    printed_string += "Goool!!!"

                else:
                    raise(AssertionError)

            except ValueError:
                
                printed_string += "ValueError: only numeric input is accepted.\nGiven input: " + operands[i][:-1]

            except IndexError:

                printed_string += "IndexError: number of operands less than expected.\nGiven input: " + operands[i][:-1]

            except ZeroDivisionError:

                printed_string += "ZeroDivisionError: You can’t divide by 0.\nGiven input: " + operands[i][:-1]

            except AssertionError:

                printed_string += "AssertionError: results don’t match."

            except:

                print("kaBOOM: run for your life!")
                
            finally:

                print(printed_string)

finally:

    print("\n˜ Game Over ˜")