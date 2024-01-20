import heapq


def minimize_costs(_cables):
    # Перетворюємо список кабелів у min-heap
    heapq.heapify(_cables)

    total_cost = 0

    while len(_cables) > 1:
        # Об'єднуємо два найменші кабелі
        cable1 = heapq.heappop(_cables)
        cable2 = heapq.heappop(_cables)
        combined_length = cable1 + cable2

        # Додаємо витрати на з'єднання до загальних витрат
        total_cost += combined_length

        # Додаємо об'єднаний кабель до min-heap
        heapq.heappush(_cables, combined_length)

    return total_cost


if __name__ == '__main__':
    cables = [1, 2, 4, 10]
    result = minimize_costs(cables)

    print(f"Мінімальні загальні витрати: {result}")  # 27
