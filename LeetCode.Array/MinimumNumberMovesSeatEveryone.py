def minMoveToSeat(self, seat: list[int], students: list[int]) -> int:
     seats.sort()    # Ordenar la lista de asientos
     students.sort() # Ordenar la lista de estudiantes
     result = 0
     for i in range(len(seats)):
            result += abs(seats[i] - students[i]) # Calcular el valor absoluto de la diferencia entre el asiento y el estudiante correspondiente
     return resul



# Example usage
seat_example1 = [3,1,5]
students_example1 = [2,7,4]

seat_example2 = [10]
students_example2 = [5]

seat_example3 = [1, 1, 1, 1]
students_example3 = [1, 1, 1, 1]

print(minMoveToSeat(seat_example1, students_example1)) # output 4
