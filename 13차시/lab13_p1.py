class AvgList(list):
    
    def computeAvg(self):
        '''Computes the average of a list of numeric types.
        Raises the ValueError exception if a list element is neither
        an 'int' nor a 'float' object.
        '''
        #The format int and non-float are excluded from the list.
        try:
            count = 0
            avg = 0
            #Average the list.
            for i in range(0,len(self)):
                avg += self[i]
                count += 1
            result = avg/count
            #Return result
            return result
        except :
            raise ValueError
