import json
import numpy as np

valid_brick_types = [3001, 3020, 3024]
valid_colors = [192, 28]

#load in the json dataset
def load_dataset(filepath):
    with open(filepath, 'r') as f:
        dataset = json.load(f)
    return dataset

#preprocess the dataset
def preprocessed_data(dataset):
    inputs = []
    outputs = []

    for tree_name, steps in dataset.items():
        for i in range(len(steps) - 1):
            current_step = steps[i]
            next_step = steps[i+1]
            
            input_vector = encode_step(current_step)
            output_vector = encode_step(next_step)

            inputs.append(input_vector)
            outputs.append(output_vector)

    return np.array(inputs), np.array(outputs)

def encode_step(step):
    brick_type = int(step['brick_type'])
    color = int(step['color'])
    position = step['position']
    orientation = step['orientation']
    step_num = step['step']
    return [brick_type, color, step_num] + position + orientation

def decode_step(step):
    step_num = int(round(float(step[0])))
    brick_type = min(valid_brick_types, key=lambda x: abs(x - float(step[1])))
    color = min(valid_colors, key=lambda x: abs(x - float(step[2])))
    position = [round(float(step[3]), 2), round(float(step[4]), 2), round(float(step[5]), 2)]
    orientation = [round(float(val), 2) for val in step[6:15]]
    return {
        "step": step_num,
        "brick_type": brick_type,
        "color": color,
        "position": position,
        "orientation": orientation
    }
