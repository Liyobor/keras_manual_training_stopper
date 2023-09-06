from inputimeout import inputimeout, TimeoutOccurred
import sys




def write_to_file(file_name, content):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Content has been written to {file_name}.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {str(e)}")


if __name__ == "__main__":
    timeout = 15

    if len(sys.argv) > 1:
        parameter = sys.argv[1]
        timeout = int(parameter)
        
    try:
        c = inputimeout(prompt="Enter y to continue training,Enter s to stop training:", timeout=timeout)
    except TimeoutOccurred:
        c = 'timeout'
    write_to_file("input.tmp", c)