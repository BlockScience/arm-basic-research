from cadCAD import configuration

from .psub import psubs
from .state import genesis_state

# Parameters
# Values are lists because they support sweeping.
simulation_config = configuration.utils.config_sim({
    "T": range(100),
    "N": 1,
    'M': {'purchase_fee':[.03]
    }
})

exp = configuration.Experiment()

exp.append_configs(sim_configs=simulation_config,
                   initial_state=genesis_state,
                   partial_state_update_blocks=psubs)