movies = ['BAHUBALI', 'RRR'] 
shows = [ 
    { 
        "movie": "RRR", 
        "date": "25-09-2026", 
        "time": "06:00 PM", 
        "screen": "Screen 1", 
        "price": 200 
    }, 
     
    { 
        'movie': "RRR", 
        'date': "25-09-2026", 
        'time': "09:00 PM", 
        'screen': "Screen 2", 
        'price': 250 
    }, 
 
    { 
        "movie": "RRR", 
        "date": "26-09-2026", 
        "time": "08:00 PM", 
        "screen": "Screen 1", 
        "price": 200 
    }, 
 
 
    { 
        "movie": "BAHUBALI", 
        "date": "30-09-2026", 
        "time": "07:00 PM", 
        "screen": "Screen 2", 
        "price": 250 
    } 
]

for show in shows:
    print(show['movie'])
    
