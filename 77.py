### generation 


geneology_object =  {
    'husband': 'Craig', 
    'wife': 'Janet',
    'children': {
        'Chris': {
            'husband': 'Chris', 
            'wife': 'Jesse',
            'children': {
                'Rebecca': {
                    'husband': 'Doug', 
                    'wife': 'Rebecca',
                }
            }
        },
        'Wonda': {
            'husband': 'Kevin', 
            'wife': 'Wonda',
            'children': {
                'Sally': {}
            }
        }
    }
}
"""
get_generations_down(geneology_object, 'Chris') 1
get_generations_down(geneology_object, 'Sally') 2
"""
def get_generations_down_helper(geneology_object, search_name, generations=0):
    gen = None
    for index,(key,value) in enumerate(geneology_object.items()):
        # print("gen: {},key: {}, value: {}".format(generations,key,value))
        # print("gen: {},key: {}, value: {}, index: {} ,len: {}, obj:{}".format(generations,key,value,index,len(geneology_object),geneology_object))
        if gen is not None:
            return gens
        if  (search_name == value or search_name == key ):
            gen = generations
        elif isinstance(value,dict) and key == "children":
            # many children
            gen =  get_generations_down_helper(value,search_name,generations=generations+1)
        elif isinstance(value,dict):
            gen =  get_generations_down_helper(value,search_name,generations=generations)
    return gen

def get_generations_down(geneology_object, search_name, generations=0):    
    gen = get_generations_down_helper(geneology_object, search_name, generations)
    if gen:
        return gen
    else:
        assert False

if __name__ == '__main__':
    assert get_generations_down(geneology_object, 'Jesse') == 1
    assert get_generations_down(geneology_object, 'Sally') == 2
    assert get_generations_down(geneology_object, 'Doug') == 2
    


    # i change something


             

