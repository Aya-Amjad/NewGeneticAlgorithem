TIMES = [
            ["MT1", ["Sunday", "Tuesday", "Thursday"], "08:00", "09:00"],
            ["MT2", ["Sunday", "Tuesday", "Thursday"], "09:00", "10:00"],
            ["MT3", ["Sunday", "Tuesday", "Thursday"], "10:00", "11:00"],
            ["MT4", ["Sunday", "Tuesday", "Thursday"], "11:00", "12:00"],
            ["MT5", ["Sunday", "Tuesday", "Thursday"], "12:00", "13:00"],
            ["MT6", ["Sunday", "Tuesday", "Thursday"], "13:00", "14:00"],
            ["MT7", ["Monday", "Wednesday"], "08:00", "09:30"],
            ["MT8", ["Monday", "Wednesday"], "09:30", "11:00"],
            ["MT9", ["Monday", "Wednesday"], "11:00", "12:30"],
            ["MT10", ["Sunday"], "08:00", "10:00"],
            ["MT11", ["Sunday"], "10:00", "12:00"],
            ["MT12", ["Sunday"], "12:00", "14:00"],
            ["MT13", ["Monday"], "08:00", "10:00"],
            ["MT14", ["Monday"], "10:00", "12:00"],
            ["MT15", ["Monday"], "12:00", "14:00"],
            ["MT16", ["Tuesday"], "08:00", "10:00"],
            ["MT17", ["Tuesday"], "10:00", "12:00"],
            ["MT18", ["Tuesday"], "12:00", "14:00"],
            ["MT19", ["Wednesday"], "08:00", "10:00"],
            ["MT20", ["Wednesday"], "10:00", "12:00"],
            ["MT21", ["Wednesday"], "12:00", "14:00"],
            ["MT22", ["Thursday"], "08:00", "10:00"],
            ["MT23", ["Thursday"], "10:00", "12:00"],
            ["MT24", ["Thursday"], "12:00", "14:00"],
            ["MT25", ["Sunday", "Tuesday"], "08:00", "09:00"],
            ["MT26", ["Sunday", "Tuesday"], "09:00", "10:00"],
            ["MT27", ["Sunday", "Tuesday"], "10:00", "11:00"],
            ["MT28", ["Sunday", "Tuesday"], "11:00", "12:00"],
            ["MT29", ["Sunday", "Tuesday"], "12:00", "13:00"],
            ["MT30", ["Sunday", "Tuesday"], "13:00", "14:00"],
            ["MT31", ["Tuesday", "Thursday"], "08:00", "09:00"],
            ["MT32", ["Tuesday", "Thursday"], "09:00", "10:00"],
            ["MT34", ["Tuesday", "Thursday"], "10:00", "11:00"],
            ["MT35", ["Tuesday", "Thursday"], "11:00", "12:00"],
            ["MT36", ["Tuesday", "Thursday"], "12:00", "13:00"],
            ["MT37", ["Tuesday", "Thursday"], "13:00", "14:00"],
            ["MT38", ["Sunday", "Thursday"], "08:00", "09:00"],
            ["MT39", ["Sunday", "Thursday"], "09:00", "10:00"],
            ["MT40", ["Sunday", "Thursday"], "10:00", "11:00"],
            ["MT41", ["Sunday", "Thursday"], "11:00", "12:00"],
            ["MT42", ["Sunday", "Thursday"], "12:00", "13:00"],
            ["MT43", ["Sunday", "Thursday"], "13:00", "14:00"],
            ["MT44", ["monday", "wednesday"], "08:00", "09:00"],
            ["MT45", ["monday", "wednesday"], "09:00", "10:00"],
            ["MT46", ["monday", "wednesday"], "10:00", "11:00"],
            ["MT47", ["monday", "wednesday"], "11:00", "12:00"],
            ["MT48", ["monday", "wednesday"], "12:00", "13:00"],
            ["MT49", ["monday", "wednesday"], "13:00", "14:00"]
            ]
valid_day_combinations = {
    0: [["Sunday"], ["Monday"], ["Tuesday"], ["Wednesday"], ["Thursday"]],
    1: [["Sunday"], ["Monday"], ["Tuesday"], ["Wednesday"], ["Thursday"]],
    2: [["Sunday", "Tuesday"], ["Sunday", "Thursday"], ["Tuesday", "Thursday"],["monday", "wednesday"]],
    3: [["Sunday", "Tuesday", "Thursday"], ["Monday", "Wednesday"]],
    4: [["Sunday", "Tuesday", "Thursday"], ["Monday", "Wednesday"]]
}
def get_id(meeting_time):
    return meeting_time[0]

def get_days(meeting_time):
    return meeting_time[1]

def get_start_time(meeting_time):
    return meeting_time[2]

def get_end_time(meeting_time):
    return meeting_time[3]