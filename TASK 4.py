def log_keystrokes():
    print("Keylogger started... (Type STOP and press Enter to stop)")
    
    log_file = open("keyloger.txt", "a")
    
    typed_keys = ""
    
    while True:
        key = input("Type something: ")  # Works in IDLE
        
        if key.strip().upper() == "STOP":
            print("Keylogger stopped.")
            break

        typed_keys += key + "\n"  # Add newline to separate entries
        log_file.write(key + "\n")
        log_file.flush()

    log_file.close()

log_keystrokes()
