import numpy as np

def calculate(list):
    try:
        my_list = list

        def List2Matrix(my_list):
            return(np.array(my_list).reshape(3,3))

        def MeanCalc(my_matrix):
            return([np.mean(my_matrix,0).tolist(),np.mean(my_matrix,1).tolist(),np.mean(my_matrix,)])

        def VarCalc(my_matrix):
            return([np.var(my_matrix,0).tolist(),np.var(my_matrix,1).tolist(),np.var(my_matrix,)])

        def StdCalc(my_matrix):
            return([np.std(my_matrix,0).tolist(),np.std(my_matrix,1).tolist(),np.std(my_matrix,)])

        def MaxCalc(my_matrix):
            return([np.max(my_matrix,0).tolist(),np.max(my_matrix,1).tolist(),np.max(my_matrix,)])

        def MinCalc(my_matrix):
            return([np.min(my_matrix,0).tolist(),np.min(my_matrix,1).tolist(),np.min(my_matrix,)])

        def SumCalc(my_matrix):
            return([np.sum(my_matrix,0).tolist(),np.sum(my_matrix,1).tolist(),np.sum(my_matrix,)])

        my_matrix = List2Matrix(my_list)
        meanArray = MeanCalc(my_matrix)
        varArray = VarCalc(my_matrix)
        stdArray = StdCalc(my_matrix)
        maxArray = MaxCalc(my_matrix)
        minArray = MinCalc(my_matrix)
        sumArray = SumCalc(my_matrix)
        
        calculations ={
            'mean': meanArray,
            'variance': varArray,
            'standard deviation': stdArray,
            'max': maxArray,
            'min': minArray,
            'sum':  sumArray
        }
        return calculations
    except:
        raise ValueError("List must contain nine numbers.")
