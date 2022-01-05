#!/usr/bin/python

#from ExtractData import ExtractData
#from PTP import PTP

# extractData = ExtractData("DataProblem/easy/PTP-RAND-1_4_2_16.json")
# problem_instance = PTP(extractData.getMaxWaitTime(), extractData.getPatients(), extractData.getLocations(),
#                        extractData.getVehicles())
def has_duplicates(lst):
    return len(lst) != len(set(lst))
    

def countWays(n,k):

    counter = 0 
    times = 0# Initialize result
    # Generate all possible quadruplet 
    # and increment counter when sum of
    # a quadruplet is equal to n
    vector_rez = []
    for x_1 in range(1, n):
        for x_2 in range(x_1, n):
            for x_3 in range(x_2, n):
                for x_4 in range(x_3, n):
                    for x_5 in range(x_4,n):
                        for x_6 in range(x_5,n):
                            for x_7 in range(x_6,n):
                                for x_8 in range(x_7,n):
                                    if x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7+x_8 == n:
                                        vector_rez.append(x_1)
                                        vector_rez.append(x_2)
                                        vector_rez.append(x_3)
                                        vector_rez.append(x_4)
                                        vector_rez.append(x_5)
                                        vector_rez.append(x_6)
                                        vector_rez.append(x_7)
                                        vector_rez.append(x_8)
                                        #print(vector_rez)
                                        if not has_duplicates(vector_rez):
                                            print(vector_rez ,"\n")
                                            times = times + 1
                                        
                                        
# Driver Code
if __name__ == "__main__":

    n = 2000 
    countWays(n,15)