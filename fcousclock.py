import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds
    
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes_left = remaining_time // 60
        seconds_left = remaining_time % 60
        time_left = f"{minutes_left:02d}:{seconds_left:02d}"
        
        print(f"Focus Timer: {time_left}", end="\r")
        time.sleep(1)
    
    print("Focus Timer: 00:00")
    print("Time's up! You can take a break now.")

# 设置专注时长为25分钟（默认）
focus_timer(25)
print("good!")good
