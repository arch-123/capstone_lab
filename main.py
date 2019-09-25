import add
import divide
import multiply
import sub
import sys


input_1 = int(sys.argv[1])
input_2 = int(sys.argv[2])

print("1: Addition\n 2: Subtraction \n3: Multiply \n4: Divide")
	
process = int(sys.argv[3])

if process == 1:
        add.add(input_1, input_2)
elif process == 2:
        sub.subtract(input_1, input_2)
elif process == 3:
        multiply.multiply(input_1, input_2)
elif process == 4:
        divide.divide(input_1, input_2)
else:
        print("Please select between 1 to 4 only")
                
                
        
		
