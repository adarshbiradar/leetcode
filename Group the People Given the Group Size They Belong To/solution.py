from itertools import islice
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        output = dict()
        groups = groupSizes
        output_str = set(groups)
        for i in output_str:
            output[i]=[]
        for i in range(len(groups)):
            output[groups[i]].append(i)
        result = []
        for key in output:
            if(len(output[key])<=key):
                result.append(output[key])
            else:
                Input = iter(output[key])
                length_to_split = [key for i in range(len(output[key])//key)]
                lst = [list(islice(Input, elem)) 
                        for elem in length_to_split]
                print(lst)
                result.extend(lst)


        return result
    


        
