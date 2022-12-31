import os
import time

from utils import load_sessions, read_session
from events import *


def main():

    sessions = load_sessions()
    # 7c1e066d0c9c4901921cab117a0b7e73.jsonl
    events = read_session(sessions[0])

    text_buffer = []
    cursor_pos = 0
    cursor_select_flag = False
    cursor_range = None

    for event in events:

        if len(text_buffer) == 0:
            buffer = ""
        else:
            buffer = text_buffer[-1]

        if event["eventName"] == "system-initialize":
            buffer, cursor_pos = system_initialize(event)
        if event["eventName"] in ["cursor-backward", "cursor-forward"]:
            cursor_pos, cursor_select_flag, cursor_range = move_cursor(event)
        if event["eventName"] == "cursor-select":
            cursor_select_flag, cursor_range = cursor_select(event)
        if event["eventName"] == "suggestion-close":
            suggestion_close()
        if event["eventName"] == "suggestion-down":
            suggestion_down()
        if event["eventName"] == "suggestion-get":
            suggestion_get()
        if event["eventName"] == "suggestion-hover":
            suggestion_hover()
        if event["eventName"] == "suggestion-open":
            suggestion_open()
        if event["eventName"] == "suggestion-reopen":
            suggestion_reopen()
        if event["eventName"] == "suggestion-select":
            suggestion_select()
        if event["eventName"] == "suggestion-up":
            suggestion_up()
        if event["eventName"] in ["text-delete", "text-insert"]:
            buffer, cursor_pos, cursor_select_flag, cursor_range = text_change(
                buffer, event, cursor_pos, cursor_select_flag, cursor_range)

        text_buffer.append(buffer)

        # os.system('clear')
        # print(buffer)
        # time.sleep(0.001)

    # print(text_buffer[-1])


if __name__ == "__main__":
    main()
