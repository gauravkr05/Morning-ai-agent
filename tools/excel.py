import openpyxl

def get_activities_from_excel(file_path='activities.xlsx'):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    
    if sheet is None:
        raise ValueError(f"No active sheet found in {file_path}")

    activities = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip header
        name, duration, distance = row
        activities.append({
            "activity": name,
            "duration": duration,
            "distance": distance
        })

    return activities
