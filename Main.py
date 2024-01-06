from Data import Data, ScheduleTable
from GeneticAlgorithm import POPULATION_SIZE, GeneticAlgorithm
from Population import Population
from Print import print_available_data, print_current_population, print_stats
from constants import TIMES, get_id,get_days,get_start_time,get_end_time

def main():
    # يجب استخدام معلومات اتصال بقاعدة البيانات الخاصة بك
    db_url = "postgresql://postgres:123456789@localhost:5432/DB"
    
    data = Data(db_url)
    print_available_data(data)

    generation_number = 0
    conflicts = []
    
    population = Population(POPULATION_SIZE, data)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    print_current_population(population, generation_number)

    geneticAlgorithm = GeneticAlgorithm(data, TIMES)

    while population.get_schedules()[0].get_fitness() != 1.0:
        generation_number += 1
        population = geneticAlgorithm.evolve(population)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        print_current_population(population, generation_number)
        conflicts.append(population.get_schedules()[0].get_number_of_conflicts())

    # حفظ الجدول النهائي في قاعدة البيانات
    final_schedule = population.get_schedules()[0]
    for lecture in final_schedule.get_lectures():
        new_schedule_row = ScheduleTable(
            doctor_name=lecture.get_docent().get_name(),
            course_name=lecture.get_course().get_name(),
            room_number=lecture.get_room().get_number(),
            time_slot = get_start_time(lecture.get_meeting_time()) + "_" + get_end_time(lecture.get_meeting_time()),
            day=get_days(lecture.get_meeting_time())

        )
        data.session.add(new_schedule_row)

    data.session.commit()
    data.close_session()

    print_stats(generation_number, conflicts, data)

if __name__ == '__main__':
    main()