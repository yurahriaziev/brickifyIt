import tensorflow as tf
from tensorflow.keras import Sequential, Input
from tensorflow.keras.layers import LSTM, Dense

from data_pipeline import load_dataset, preprocessed_data

#model
def build_model(input_dim, output_dim):
    model = Sequential([
        Input(shape=(None, input_dim)),
        LSTM(128, return_sequences=False),
        Dense(output_dim, activation="linear")
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

input_dim = 15
output_dim = 15

model = build_model(input_dim, output_dim)
model.summary()


''' Training model and validating results '''
dataset = load_dataset('tree_dataset.json')
inputs, outputs = preprocessed_data(dataset)
inputs = inputs.reshape((inputs.shape[0], 1, inputs.shape[1]))
outputs = outputs.reshape((outputs.shape[0], 1, outputs.shape[1]))

model.fit(inputs, outputs, epochs=50, batch_size=8)
try:
    model.save('tree_mode.keras')
    print('Model saved.')
except Exception as e:
    print(f'Error saving model, {str(e)}')