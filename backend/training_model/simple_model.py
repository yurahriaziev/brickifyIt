import tensorflow as tf
from tensorflow.keras import Sequential, Input
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.losses import MeanSquaredError, SparseCategoricalCrossentropy # for accurate step predictions

from data_pipeline import load_dataset, preprocessed_data

#model
def build_model(input_dim, output_dim):
    input_layer = Input(shape=(None, input_dim))
    lstm_output = LSTM(128)(input_layer)

    step_output = Dense(10, activation='softmax', name='step_output')(lstm_output)
    brick_output = Dense(output_dim, activation='linear', name='brick_output')(lstm_output)

    model = tf.keras.Model(inputs=input_layer, outputs=[step_output, brick_output])

    model.compile(
            optimizer='adam',
            loss={
                'step_output':SparseCategoricalCrossentropy(),
                'brick_output':MeanSquaredError()
            },
            metrics={
                'step_output':'accuracy',
                'brick_output':'mse'
            }
        )

    return model

input_dim = 15
output_dim = 14

model = build_model(input_dim, output_dim)
model.summary()


''' Training model and validating results '''
dataset = load_dataset('tree_dataset.json')
inputs, step_outputs, brick_outputs = preprocessed_data(dataset)
inputs = inputs.reshape((inputs.shape[0], 1, inputs.shape[1]))
step_outputs = step_outputs.reshape((step_outputs.shape[0], 1))
brick_outputs = brick_outputs.reshape((brick_outputs.shape[0], 1, -1))

model.fit(inputs, {'step_output':step_outputs, 'brick_output':brick_outputs}, epochs=10000, batch_size=32)
try:
    model.save('tree_mode.keras')
    print('Model saved.')
except Exception as e:
    print(f'Error saving model, {str(e)}')