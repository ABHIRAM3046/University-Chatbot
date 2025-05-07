import json
import boto3

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
student_table = dynamodb.Table('StudentRecords')
timetable_table = dynamodb.Table('Timetable')

def lambda_handler(event, context):
    """Main handler to route Lex intents."""
    intent_name = event['sessionState']['intent']['name']
    
    if intent_name == "CheckAttendanceMarks":
        return get_student_record(event)
    
    elif intent_name == "GetTimeTable":
        return get_timetable(event)
    
    else:
        return unknown_intent_response(intent_name)

def get_student_record(event):
    """Fetch student details from DynamoDB and return formatted response."""
    try:
        slots = event['sessionState']['intent'].get('slots', {})
        student_id = slots.get('StudentID', {}).get('value', {}).get('interpretedValue')

        if not student_id:
            return build_lex_response(event, "Failed", "⚠️ **Error:** Missing Student ID. Please provide a valid Student ID.")
        
        response = student_table.get_item(Key={'Student_id': "RA2211028010179"})
        
        if 'Item' in response:
            student = response['Item']
            marks = "\n".join([f"📖 {subject}: {score}%" for subject, score in student.get('Marks', {}).items()])
            
            message = (
                f"📌 Student Information\n"
                f"👤 Name: {student['Name']}\n"
                f"🆔 Student ID: {student['Student_id']}\n\n"
                f"📚 Academic Performance\n"
                f"📅 Attendance: {student.get('Attendance', 'N/A')}%\n"
                f"📝 Marks:\n{marks if marks else 'No marks available'}\n\n"
                f"✅ Keep up the good work! Let me know if you need more info."
            )
            
            return build_lex_response(event, "Fulfilled", message)
        
        else:
            return build_lex_response(event, "Failed", "⚠️ **Error:** Student ID not found. Please check and try again!")
    
    except Exception as e:
        return build_lex_response(event, "Failed", f"❌ **System Error:** {str(e)}. Please try again later.")

def get_timetable(event):
    """Retrieve timetable from DynamoDB for a specific day or full week."""
    try:
        slots = event['sessionState']['intent'].get('slots', {})
        day_requested = slots.get('Day', {}).get('value', {}).get('interpretedValue')
        
        if day_requested:
            response = timetable_table.get_item(Key={'Day': day_requested})
            if 'Item' in response:
                message = format_day_schedule(response['Item'])
            else:
                message = f"⚠️ No timetable found for **{day_requested}**."
        else:
            response = timetable_table.scan()
            days = response.get('Items', [])
            message = format_timetable(days)

        return build_lex_response(event, "Fulfilled", message)

    except Exception as e:
        return build_lex_response(event, "Failed", f"❌ **System Error:** {str(e)}. Please try again later.")

def format_timetable(days):
    """Formats the full timetable for Lex response."""
    if not days:
        return "⚠️ No timetable data available."
    
    formatted_schedule = [format_day_schedule(day) for day in days]
    return "\n\n".join(formatted_schedule)

def format_day_schedule(day_item):
    """Formats a single day's schedule."""
    day_name = day_item.get('Day', 'Unknown Day')
    slots = day_item.get('Slots', [])

    if not slots:
        return f"📅 **{day_name}**: No scheduled classes."

    slot_entries = [f"⏰ {slot.get('Hour', 'Unknown Time')} - {slot.get('Course', 'Unknown Course')}" for slot in slots]
    return f"📅 **{day_name}**\n" + "\n".join(slot_entries)

def build_lex_response(event, state, message):
    """Builds a structured Lex response."""
    return {
        "sessionState": {
            "dialogAction": {"type": "Close"},
            "intent": {
                "name": event['sessionState']['intent']['name'], 
                "state": state
            }
        },
        "messages": [{"contentType": "PlainText", "content": message}]
    }

def unknown_intent_response(intent_name):
    """Handles unknown intents."""
    return {
        "sessionState": {
            "dialogAction": {"type": "Close"},
            "intent": {"name": intent_name, "state": "Failed"}
        },
        "messages": [{"contentType": "PlainText", "content": f"❌ **Error:** Intent '{intent_name}' not recognized."}]
    }
