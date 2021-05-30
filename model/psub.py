from .model.helper_functions import *


psubs = [
    {
        'label': 'Update Time Attached',
        'policies': {
        },
        'variables': {
            'brokers': update_time_attached
        }
    },
    {
        'label': 'Payments',
        'policies': {
            'payment_amt': payment_amt  # how much is paid in.
        },
        'variables': {
            'unallocated_funds': payment_to_unallocated
        },
    }
]