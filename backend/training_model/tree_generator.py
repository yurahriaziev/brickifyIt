import json

dataset = {
    "tree_1": [
        {"step": 1, "brick_type": "3001", "color": "192", "position": [0, 0, 0], "orientation": [1, 0, 0, 0, 1, 0, 0, 0, 1]},
        {"step": 2, "brick_type": "3001", "color": "192", "position": [0, 0, 1], "orientation": [1, 0, 0, 0, 1, 0, 0, 0, 1]},
        {"step": 3, "brick_type": "3020", "color": "192", "position": [1, 0, 2], "orientation": [1, 0, 0, 0, 1, 0, 0, 0, 1]},
        {"step": 4, "brick_type": "3024", "color": "28", "position": [1, 0, 3], "orientation": [1, 0, 0, 0, 1, 0, 0, 0, 1]},
    ],
    "tree_2": [
        {"step": 1, "brick_type": "3001", "color": "192", "position": [0, 0, 0], "orientation": [1, 0, 0, 0, 1, 0, 0, 0, 1]},
        {"step": 2, "brick_type": "3001", "color": "192", "position": [0, 0, 1], "orientation": [1, 0, 0, 0, 1, 0, 0, 0, 1]},
        {"step": 3, "brick_type": "3020", "color": "192", "position": [-1, 0, 2], "orientation": [1, 0, 0, 0, 1, 0, 0, 0, 1]},
        {"step": 4, "brick_type": "3024", "color": "28", "position": [-1, 0, 3], "orientation": [1, 0, 0, 0, 1, 0, 0, 0, 1]},
    ],
    "tree_3": [
        {"step": 1, "brick_type": "3001", "color": "192", "position": [0, 0, 0], "orientation": [1, 0, 0, 0, 1, 0, 0, 0, 1]},
        {"step": 2, "brick_type": "3001", "color": "192", "position": [0, 0, 1], "orientation": [1, 0, 0, 0, 1, 0, 0, 0, 1]},
        {"step": 3, "brick_type": "3020", "color": "192", "position": [0, 1, 2], "orientation": [1, 0, 0, 0, 1, 0, 0, 0, 1]},
        {"step": 4, "brick_type": "3024", "color": "28", "position": [0, 1, 3], "orientation": [1, 0, 0, 0, 1, 0, 0, 0, 1]},
    ],
    "tree4": [
        {
            "step": 1,
            "brick_type": 3001,
            "color": 28,
            "position": [0.0, 0.0, 0.0],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        },
        {
            "step": 2,
            "brick_type": 3001,
            "color": 28,
            "position": [0.0, 0.0, 1.0],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        },
        {
            "step": 3,
            "brick_type": 3020,
            "color": 192,
            "position": [0.0, 0.5, 2.0],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        }
    ],
    "tree5": [
        {
            "step": 1,
            "brick_type": 3001,
            "color": 28,
            "position": [0.0, 0.0, 0.0],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        },
        {
            "step": 2,
            "brick_type": 3001,
            "color": 28,
            "position": [0.0, 0.0, 1.0],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        },
        {
            "step": 3,
            "brick_type": 3001,
            "color": 28,
            "position": [0.5, 0.0, 2.0],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        },
        {
            "step": 4,
            "brick_type": 3001,
            "color": 28,
            "position": [-0.5, 0.0, 2.0],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        }
    ],
    "tree6": [
        {
            "step": 1,
            "brick_type": 3001,
            "color": 28,
            "position": [0.0, 0.0, 0.0],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        },
        {
            "step": 2,
            "brick_type": 3001,
            "color": 28,
            "position": [0.0, 0.0, 1.0],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        },
        {
            "step": 3,
            "brick_type": 3020,
            "color": 28,
            "position": [0.0, 0.5, 2.0],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        },
        {
            "step": 4,
            "brick_type": 3020,
            "color": 192,
            "position": [-0.5, 0.5, 2.0],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        }
    ],
    "tree7": [
        {
            "step": 1,
            "brick_type": 3001,
            "color": 192,
            "position": [0.0, 0.0, 0.0],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        },
        {
            "step": 2,
            "brick_type": 3001,
            "color": 192,
            "position": [0.0, 0.0, 1.0],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        },
        {
            "step": 3,
            "brick_type": 3024,
            "color": 28,
            "position": [0.5, 0.0, 2.0],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        },
        {
            "step": 4,
            "brick_type": 3024,
            "color": 28,
            "position": [-0.5, 0.0, 2.0],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        }
    ]
}

with open('tree_dataset.json', 'w') as f:
    json.dump(dataset, f, indent=4)