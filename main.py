def num_words(file_contents):
    return len(file_contents.split())

def num_char(file_contents):
    my_dict = {}
    lower_contents = file_contents.lower()
    words = lower_contents.split()
    for word in words:
        for char in word:
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
    return my_dict

def char_report(char_dict):
    char_list = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    output = ""
    for char in char_list:
        if not char[0].isalpha():
            continue
        output += f"\nThe '{char[0]}' character was found {char[1]} times"
    return output

def full_report(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        print(f"--- Begin report of {file_path} ---")
        print(f"{num_words(file_contents)} words found in the document")     
        char_dict = num_char(file_contents)
        print(char_report(char_dict))
        print("--- End report ---")
            

if __name__ == "__main__":
    path_to_file = 'books/frankenstein.txt'
    
    full_report(path_to_file)
        

