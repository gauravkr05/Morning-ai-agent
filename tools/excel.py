import openpyxl

def get_activities_from_excel(file_path='activities.xlsx'):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    
    if sheet is None:
        raise ValueError(f"No active sheet found in {file_path}")

    activities = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  
        if not row or all(cell is None for cell in row):
            continue  # skip empty rows
        try:
            name, duration, distance, activity_type = row[:4]  
            activities.append({
                "name": name,
                "duration": duration,
                "distance": distance,
                "type": activity_type
            })
        except Exception as e:
            print(f"⚠️ Skipped row due to error: {e}")
            continue

    return activities