def parse_input(text):
    text_lower = text.lower()

    if "remind" in text_lower:
        return {
            "type": "reminder",
            "content": text
        }

    elif "meeting" in text_lower or "calendar" in text_lower:
        return {
            "type": "calendar_event",
            "content": text
        }

    elif "todo" in text_lower or "need to" in text_lower:
        return {
            "type": "task",
            "content": text
        }

    return {
        "type": "note",
        "content": text
    }