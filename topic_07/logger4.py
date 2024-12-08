class Logger:
    def log_action(self, message):
        with open("calculator_log.txt", "a") as log_file:
            log_file.write(message + "\n")
