from flask import jsonify
   
def remove_nestings(items, output): 
    for i in items: 
        if type(i) == list: 
            remove_nestings(i, output) 
        else: 
            output.append(i)

    return output

def get_values(items): 
    output = [] 
    new_list = remove_nestings(items, output) 
    
    return jsonify({'result': new_list})