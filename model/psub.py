from model.model.dynamics import create_items
from .model.helper_functions import *
from .model.dynamics import buy_encounter, create_items, into_reserve, outof_reserve, sell_encounter, track_items, update_items, update_model


psubs = [
    {
        'label': 'new items appear',
        'policies': {
            'create_items': create_items
        },
        'variables': {
            'items': track_items
        }
    },
    {
        'label': 'sell items to ARM',
        'policies': {
            'sell': sell_encounter  # how much is paid in.
        },
        'variables': {
            'items': update_items,
            'model': update_model,
            'reserve': outof_reserve
        },
    },
    {
        'label': 'buy items from ARM',
        'policies': {
            'sell': buy_encounter  # how much is paid in.
        },
        'variables': {
            'items': update_items,
            'model': update_model,
            'reserve': into_reserve
        }
    }
]