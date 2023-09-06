# keras_manual_training_stopper


## English Documentation

This project offers a straightforward method to manually decide whether to continue or stop training a neural network model in keras after a specified epoch. If the user does not respond within a given timeframe, training will automatically proceed.

### Features

1. After a specified epoch, a terminal window will pop up after each training completion to inquire if you wish to continue the training.
2. Decide within the specified time whether to continue or stop training.
3. If no response is received, training will automatically continue.

### Installation

Before utilizing this project, ensure you have the required library:

```
inputimeout
keras
```

To install the inputimeout library, you can use pip:

```
pip install inputimeout
```

#### Note:

Before using this project, please ensure you have an appropriate version of keras installed.

### Usage

1. Add manual_training_stopper_callback.py and timeout_input_catcher.py to your project.
2. Include the ManualTrainingStopperCallback callback function when training your model.

```python=
from manual_training_stopper_callback import ManualTrainingStopperCallback

model.fit(
    # ... (other training parameters)
    callbacks=[ManualTrainingStopperCallback(model, prompt_after_epoch=15,timeout = 120)]
)
```

### Options

prompt_after_epoch: From which epoch the prompt will start appearing (default is 20).

timeout: Time in seconds to wait for a user response (default is 15 seconds).


## 中文文檔

這個項目提供了一個簡單的方法，可在keras訓練神經網路模型時，在指定epoch後手動選擇是否要繼續訓練或停止訓練,若使用者在時間內沒有回應則繼續進行訓練。

### 功能

1. 在指定的epoch後，每次訓練完成後會跳出終端機視窗詢問是否繼續訓練。
2. 指定的時間內決定是否要繼續訓練或停止。
3. 若無回應，訓練會自動繼續。


### 安裝

在使用此項目之前，請確保您已安裝以下必要的函式庫：

```
inputimeout
keras
```

要安裝inputimeout,可以使用'pip':

```
pip install inputimeout
```

#### 註記

使用此項目前,請自行安裝合適版本的keras

### 使用方法

1. 將 manual_training_stopper_callback.py 和 timeout_input_catcher.py 加入到您的項目中。
2. 在訓練模型時加入 ManualTrainingStopperCallback 這個回呼函式。

```python=
from manual_training_stopper_callback import ManualTrainingStopperCallback

model.fit(
    # ... (其他訓練參數)
    callbacks=[ManualTrainingStopperCallback(model,prompt_after_epoch = 15,timeout = 120)]
)
```

### 選項

prompt_after_epoch: 從第幾個epoch開始彈出提示 (預設為20)。

timeout: 等待使用者回應的時間，單位為秒 (預設為15秒)。