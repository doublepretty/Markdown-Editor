all_commands = ['plain', 'bold', 'italic', 'header', 'link',
                'inline-code', 'ordered-list', 'unordered-list', 'new-line', "!help", "!done"]
formatted_text = ""


def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")


def print_formatted_text():
    print(formatted_text)


def update_formatted_text(_text):
    global formatted_text
    formatted_text += _text


def format_header():
    while True:
        input_level = int(input("Level:"))
        if input_level < 1 or input_level > 6:
            print("The level should be within the range of 1 to 6.")
        else:
            break
    input_text = input("Text:")
    update_formatted_text(f"{'#' * input_level} {input_text}\n")
    print_formatted_text()


def format_new_line():
    update_formatted_text("\n")
    print_formatted_text()


def format_plain():
    input_text = input("Text:")
    update_formatted_text(f"{input_text}")
    print_formatted_text()


def format_link():
    input_label = input("Label:")
    input_url = input("URL:")
    update_formatted_text(f"[{input_label}]({input_url})")
    print_formatted_text()


def format_bold():
    input_text = input("Text:")
    update_formatted_text(f'**{input_text}**')
    print_formatted_text()


def format_italic():
    input_text = input("Text:")
    update_formatted_text(f'*{input_text}*')
    print_formatted_text()


def format_inline_code():
    input_text = input("Text:")
    update_formatted_text(f'`{input_text}`')
    print_formatted_text()


def format_list(order_type="ordered"):
    while True:
        input_row = int(input("Number of rows:"))
        if input_row <= 0:
            print("The number of rows should be greater than zero")
        else:
            break
    for index in range(1, input_row + 1):
        input_text = input(f"Row #{index}:")
        update_formatted_text(f"{str(index) + '.' if order_type == 'ordered' else '*'} {input_text}\n")
    print_formatted_text()


def done():
    file = open('output.md', 'w')
    file.write(formatted_text)
    file.close()


def run():
    while True:
        formatter = input("Choose a formatter:")
        if formatter in all_commands:
            if formatter == '!help':
                print_help()
            elif formatter == '!done':
                done()
                break
            elif formatter == "header":
                format_header()
            elif formatter == "plain":
                format_plain()
            elif formatter == "new-line":
                format_new_line()
            elif formatter == "link":
                format_link()
            elif formatter == "bold":
                format_bold()
            elif formatter == "italic":
                format_italic()
            elif formatter == "inline-code":
                format_inline_code()
            elif formatter == 'ordered-list':
                format_list("ordered")
            elif formatter == 'unordered-list':
                format_list("unordered")
            else:
                pass
        else:
            print("Unknown formatting type or command")


run()
