# File objects

# Auto closes file if exceptions are thrown and closes file afterwards
with open('text.txt', 'r+') as f:  # r = read, r+ = read and write, w = write
    with open('test_copy.txt', 'w') as wf:
        with open('pic.jpg', 'rb') as img_f, open('picCopied.jpg', 'wb') as w_img_f:
            f_contents = f.read()  # If a very large file, f.readlines() or f.readline() is far more appropriate
            print(f_contents, end="\n\n")

            # Set the file pointer back to the start
            f.seek(0, 0)

            pre_letter = False

            for line in f:
                print(line, end="")
                for ch in line:
                    if ch == 'A' or ch == 'B':
                        pre_letter = True
                    elif pre_letter == True and ch == '.':
                        print("This line has a sub-section!")
                        pre_letter = False
                    else:
                        pre_letter = False
                        
            f.seek(0, 0)
            size_to_read = 10
            print()

            f_contents = f.read(size_to_read)

            while len(f_contents) > 0:
                print(f_contents, end="*")  # Astrix is there to show how file increments through parts
                f_contents = f.read(size_to_read)  # When the end is reached, f.read will return an empty string

            print("Position in the file: ", f.tell())
            f.seek(0, 0)

            # Write to file test
            for line in f:
                wf.write(line)  # Will write to where specified.

            # Copying a large picture file
            chunk_size = 4096
            rf_chunk = img_f.read(chunk_size)
            while len(rf_chunk) > 0:
                w_img_f.write(rf_chunk)
                rf_chunk = img_f.read(chunk_size)



