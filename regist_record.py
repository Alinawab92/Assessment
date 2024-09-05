class Regist_Record:
    def __init__(self):
        # Store the history and positions
        self.history = []

    def add_record(self, position):
        self.history.append(position)

    def get_status(self):
        if self.history:
            return f"Current Position: {self.history[-1]}"  # Last added position is the current one
        else:
            return "No position assigned"

    def show_history(self):
        if self.history:
            return f"Position History: {', '.join(self.history)}"
        else:
            return "No position history available"
