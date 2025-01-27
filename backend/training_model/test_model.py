from tensorflow.keras.models import load_model
import numpy as np
from data_pipeline import decode_step
import json

model = load_model('/Users/yuriihriaziev/Documents/Programming/brickifyIt/backend/training_model/tree_mode.keras')
print('MODEL LOADED IN SUCCESSFULLY')

init_step = np.array([1, 3001, 192, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], dtype=np.float32)
init_step = init_step.reshape(1,1,-1)

generated_steps = []
cur_step = init_step

for _ in range(5):
    cur_step = cur_step.reshape(1,1,-1)
    step_output, brick_output = model.predict(cur_step)
    print(f"Step output shape: {step_output.shape}")

    if len(step_output.shape) == 1:
        step_num = int(step_output[0])
    elif len(step_output.shape) == 2:
        step_num = np.argmax(step_output, axis=-1)[0]
    else:
        raise ValueError(f"Unexpected step_output shape: {step_output.shape}")

    decoded_brick = decode_step(brick_output[0])
    decoded_brick['step'] = step_num
    generated_steps.append(decoded_brick)

    next_input = [step_num] + list(brick_output[0])
    cur_step = np.array(next_input, dtype=np.float32).reshape(1,1,-1)

# helper func to convert numpy data types to python ints or floats
def make_serializable(data):
    if isinstance(data, dict):
        return {key: make_serializable(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [make_serializable(value) for value in data]
    elif isinstance(data, np.ndarray):
        return data.tolist()
    elif isinstance(data, (np.int64, np.int32)):
        return int(data)
    elif isinstance(data, (np.float64, np.float32)):
        return float(data)
    else:
        return data

print('ENCODED STEPS')
for step in generated_steps:
    print(step)

serializable_steps = make_serializable(generated_steps)
print()
print('DECODED STEPS TO JSON')
print(json.dumps(serializable_steps, indent=4))