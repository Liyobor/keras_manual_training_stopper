from keras.layers import Input, Dense
from keras.models import Model
import numpy as np
# if system is windows
from KMTS.windows.manual_training_stopper_callback import ManualTrainingStopperCallback
# if system is linux
# from KMTS.linux.manual_training_stopper_callback import ManualTrainingStopperCallback



# Number of training samples
num_samples = 1000

# Generating random training data
x_train = np.random.rand(num_samples, 32)
y_train = np.random.rand(num_samples, 1)

x_train.shape, y_train.shape


input_tensor = Input(shape=(32,))
x = Dense(64, activation='relu')(input_tensor)
output_tensor = Dense(1)(x)
model = Model(inputs=input_tensor, outputs=output_tensor)
model.compile(optimizer='adam', loss='mean_squared_error')
# ManualTrainingStopperCallback(model,prompt_after_epoch = 15,timeout = 120)

model.fit(
    x=x_train,
    y = y_train,
    epochs=50,
    callbacks=[ManualTrainingStopperCallback(model,prompt_after_epoch = 15,timeout = 120)]
)
