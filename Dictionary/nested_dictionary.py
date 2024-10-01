last_login= {
    "01-01-2000": {
        "location": "london",
        "time": "5pm",
        "session_time": "45m"
    },
    "02-01-2000":{
        "location": "london",
        "time": "8pm",
        "session_time": "15m"
    },
}

print(last_login["01-01-2000"]["session_time"])

for key,val in last_login.items():
    print(f"Date ( {key} ) : {val}")

    print("-"*32)

    for key1,val1 in val.items():
        print(f"{key1} : {val1}")
        
    print("-"*32)

