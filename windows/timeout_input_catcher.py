from inputimeout import inputimeout, TimeoutOccurred



def write_to_file(file_name, content):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Content has been written to {file_name}.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {str(e)}")


if __name__ == "__main__":
    try:
        c = inputimeout(prompt="Enter y to continue training,Enter s to stop training:", timeout=15)
    except TimeoutOccurred:
        c = 'timeout'
    write_to_file("command.txt", c)