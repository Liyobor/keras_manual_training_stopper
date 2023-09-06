from inputimeout import inputimeout, TimeoutOccurred
import sys

DEFAULT_TIMEOUT = 15
def write_to_file(file_name, content):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
        # print(f"Content has been written to {file_name}.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {str(e)}")

def get_user_input(timeout=DEFAULT_TIMEOUT) -> str:
    try:
        return inputimeout(prompt="Enter y to continue training,Enter s to stop training:", timeout=timeout)
    except TimeoutOccurred:
        return 'timeout'
    except Exception as e:
        return "error"

if __name__ == "__main__":
    timeout = DEFAULT_TIMEOUT
    if len(sys.argv) > 1:
        parameter = sys.argv[1]
        timeout = int(parameter)
        
    user_input = get_user_input(timeout=timeout)
    write_to_file("input.tmp", user_input)