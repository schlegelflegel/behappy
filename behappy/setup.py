import os
from collections import OrderedDict


beagle1 = "beagle46.local"
beagle2 = None
beagle3 = None

channels_per_box = 6
path_to_config = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'pneumaticbox-python-client'))

EXPERIMENT_SETUP = {
    'state_collector': {
        'active': True,
        'experiment_name': 'finger_test',
        'path_to_save_trajectories': '/path/to_your/Data/' # Optional
    },
    'hand': {
        'pneumatic_boxes': [beagle1, beagle2, beagle3],
        'channels_per_box': channels_per_box,
        'path_to_pneumatic_box_configs': path_to_config,
        'step_time': 0.025, # Time between actuation commands
        'max_flow_rate': 1000, # In mg/s
        'deflation_time': 2.0, # Time the valves are opened when a reset/deflation command is triggered
        'channel_to_hand_mapping':  OrderedDict([
            ('base', ['finger_base']),
            ('tip', ['finger_tip']),
            ('inner_palm', ['inner_palm_big']),
            ('outer_palm', ['outer_palm_big']),
            ('thumb', ['thumb_tip']),
            ('unused', []),
            ('unused', []),
            ('unused', [])
        ]),
        'chamber_max_pressures': {
             "finger_base": 260,
             "finger_tip": 260,
             "thumb_tip": 260,
             "thumb_big": 75,
             "inner_palm_small": 55,
             "outer_palm_small": 60,
             "inner_palm_big": 55,
             "outer_palm_big": 70,
             "thumb_base_1": 260,
             "thumb_base_2": 260,
             "thumb_base_3": 260,
             "between_index_middle": 260,  # TODO
             "between_middle_ring": 260,  # TODO
             "between_ring_pinky": 260,  # TODO
             "palm_carpo": 260,  # TODO
             "unused": 1,
             "empty": 260,
             "single_p10": 60,
             'min_supply_pressure': 270,
             'max_supply_pressure': 320,
        },
        'chamber_max_masses': {
             "finger_base": 80,  # TODO
             "finger_tip": 80,  # TODO
             "thumb_tip": 80,
             "thumb_base_1": 100,
             "thumb_base_2": 100,
             "thumb_base_3": 75,
             "inner_palm_big": 80,  # TODO
             "outer_palm_big": 120,  # TODO
             "between_index_middle": 30,  # TODO
             "between_middle_ring": 30,  # TODO
             "between_ring_pinky": 30,  # TODO
             "palm_carpo": 75,
             "unused": 1,
             "empty": 1
            }  # for 185cm tube length
    }
}
