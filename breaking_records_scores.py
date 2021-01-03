# Completed hackerrank breaking records

def breakingRecords(scores):
    high_score = scores[0]
    low_score = scores[0]
    record_break_high = 0
    record_break_low = 0
    
    for score in scores:
        if score > high_score:
            high_score = score
            record_break_high += 1
        elif score < low_score:
            low_score = score
            record_break_low +=1
    return [record_break_high, record_break_low] 