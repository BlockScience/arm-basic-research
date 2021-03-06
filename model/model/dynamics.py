import numpy as np
from .items import Item
from .helper_functions import gen_context, is_for_sale, quadratic_form

def create_items(params, step, sL, s):
    
    items = s['items']
    
    new_item_id = len(items)
    new_item = Item(new_item_id)

    value = {new_item_id:new_item}
    key = 'new_items'
    return {key: value}

def track_items(params, step, sL, s, inputs):
    """
    grab the new items from inputs and append them to the state 'items'
    """
    items = s['items']
    #print(items)
    
    new_items = inputs['new_items']

    for k in new_items.keys():
        items[k] = new_items[k]
    
    key = 'items'
    value = items

    #print(items)
    return key, value

def buy_encounter(params, step, sL, s):
    """
    agent buys from ARM
    """
    model = s['model']
    context_matrix = gen_context()
    items = s['items']
    best_item = None
    best_gap = 0

    for k in is_for_sale(items):
        i = items[k]
        x = i.attributes
        private_price = quadratic_form(x,context_matrix)
        #print(private_price)
        arm_price = model.predict(x)*(1+params['purchase_fee'])
        #print(arm_price)
        if private_price >= arm_price:
            gap = private_price-arm_price
            if gap > best_gap:
                best_gap = gap
                best_item = k
    
    if best_item==None:
        return {}
    
    else:
        return{'item_id':best_item}

def into_reserve(params, step, sL, s, inputs):

    #inputes from sell_encounter
    price = 0
    if 'item_id' in inputs.keys():
        purchased_item_id = inputs['item_id']
        model = s['model']    
        items = s['items']
        purchased_item = items[purchased_item_id]
        price = model.predict(purchased_item.attributes)*(1+params['purchase_fee'])
        print("item "+str(purchased_item_id)+" was purchased from ARM for "+str(price))
    else:
        print("no purchase from ARM this round")


    key = 'reserve'
    value = s['reserve']+price

    return key, value

def sell_encounter(params, step, sL, s):
    """
    agent sells to ARM
    """
    model = s['model']
    context_matrix = gen_context()
    items = s['items']
    best_item = None
    best_gap = 0
    best_price = 0
    
    for k in is_for_sale(items, flip=True):
        i = items[k]
        x = i.attributes
        private_price = quadratic_form(x,context_matrix)
        #print(private_price)
        arm_price = model.predict(x)*(1-params['purchase_fee'])
        #print(arm_price)
        if private_price <= arm_price:
            gap = arm_price-private_price
            if gap > best_gap:
                best_gap = gap
                best_item = k

                best_price = arm_price
    
    if best_price>s['reserve']:
        best_item=None

    if best_item==None:
        return {}
    
    else:
        return{'item_id':best_item}

def outof_reserve(params, step, sL, s, inputs):

    #inputs from buy_encounter
    price = 0
    if 'item_id' in inputs.keys():
        purchased_item_id = inputs['item_id']
        model = s['model']
        items = s['items']
        purchased_item = items[purchased_item_id]
        price = model.predict(purchased_item.attributes)*(1-params['purchase_fee'])

        print("item "+str(purchased_item_id)+" was sold to ARM for "+str(price))
    else:
        print("no sale to ARM this round")

    key = 'reserve'
    value = s['reserve']-price

    return key, value





def update_model(params, step, sL, s, inputs):

    model = s['model']

    if 'item_id' in inputs.keys():
    
        purchased_item_id = inputs['item_id']
        
        items = s['items']
        purchased_item = items[purchased_item_id]
        
        ### as written this is tautological: needs rework
        x = purchased_item.attributes
        y = model.predict(purchased_item.attributes)
        model.update(x, y)

    key = 'model'
    value = model

    return key, value

def update_items(params, step, sL, s, inputs):
     
    items = s['items']
    #print(items.keys())
    #print(inputs)   
    if 'item_id' in inputs.keys():
        current_item_id = inputs['item_id']
        #print(current_item_id)
        #print(items[current_item_id].for_sale)
        items[current_item_id].swap()

    key = 'items'
    value = items

    return key, value

