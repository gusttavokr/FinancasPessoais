from datetime import datetime

def formatarData(data):
    if isinstance(data, str):
        try:
            data = datetime.strptime(data, "%Y-%m-%d").date()
        except ValueError:
            return data  
    return data.strftime('%d/%m/%Y')
