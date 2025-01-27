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
    next_step = model.predict(cur_step)
    generated_steps.append(next_step)
    cur_step = next_step

print('ENCODED STEPS')
for step in generated_steps:
    print(step)

print()
print('DECODED STEPS TO JSON')
decoded_steps = [decode_step(step[0]) for step in generated_steps]
# for step in decoded_steps:
#     print(step)
print(json.dumps(decoded_steps, indent=4))