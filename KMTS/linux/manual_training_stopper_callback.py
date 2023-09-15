import keras
import subprocess
import os
class ManualTrainingStopperCallback(keras.callbacks.Callback):

    def __init__(self,model,prompt_after_epoch=20,timeout=15):
        super(ManualTrainingStopperCallback, self).__init__()
        self.prompt_after_epoch = prompt_after_epoch
        self.model = model
        self.timeout = timeout

    def on_epoch_end(self, epoch, logs={}):
        if epoch < self.prompt_after_epoch:
            return
        module_directory = os.path.dirname(os.path.abspath(__file__))
        tmp_path = os.path.join(module_directory,"input.tmp")
        def delete_file(file_name):
            try:
                os.remove(file_name)
                
            except FileNotFoundError:
                pass
                
            except Exception as e:
                print(f"Error occurred when deleting the temp file:{str(e)}")
        delete_file(tmp_path)
        
        subprocess.run(["start", "cmd", "/c", "python timeout_input_catcher.py",str(self.timeout)],
               shell=True,
               cwd=module_directory,
               capture_output=True)
        def read_file(file_name):
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read()
                return content
            except FileNotFoundError:
                return f"file {file_name} not found"
            except Exception as e:
                return "y"
            

        content = read_file(tmp_path)
        
        if content.lower() == "y":
            pass
        elif content.lower() == "s":
            self.model.stop_training = True
        elif content.lower() == "timeout":
            print("")
            print("No response,continue training.")
        else:
            print("")
            print("invalid input!")