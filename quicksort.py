def days(life):
    if life == []: 
        return []
    else:
        today = life[0]
        life = life[]
        yesterdays = days([day for day in life[1:] if day < today])
        tomorrows = days([day for day in life[1:] if day >= today])
        return yesterdays + [today] + tomorrows