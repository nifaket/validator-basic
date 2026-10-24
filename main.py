
# ---- допустимые границы (константы) ----
Q_RANGE = (0.0, 1000.0) # дебит жидкости, м³/сут
W_RANGE = (0.0, 100.0) # обводнённость, %
P_RANGE = (0.0, 100.0) # пластовое давление, МПа
H_RANGE = (500.0, 4000.0) # глубина, м
def input_bounded(prompt: str, name: str, lo: float, hi: float) -> float:
    while True:
        raw = input(prompt).strip().replace(",", ".")
        if raw == "":
            print(f"[пропуск] Пустая строка. Поле '{name}' обязательно.")
            continue
        try:
             value = float(raw)
        except ValueError:
            print(f"[ошибка] '{raw}' — не число. Введите число.")
            continue
        # проверка границ через if-elif-else
        if value < lo:
            print(f"[ошибка] {name} = {value:g} меньше минимума {lo:g}.")
            continue
        elif value > hi:
            print(f"[ошибка] {name} = {value:g} больше максимума {hi:g}.")
            continue
        else:
            return value
def classify_well(w_pct: float) -> str:
    """Классификация скважины по обводнённости (if-elif-else)."""
    if w_pct < 5:
        return "нефтяная (маловодная)"
    elif w_pct < 30:
        return "условно-безводная"
    elif w_pct < 80:
        return "обводнённая"
    else:
        return "водяная (эксплуатация нерациональна)"
def main() -> None:
    print("ВАЛИДАТОР ПАРАМЕТРОВ СКВАЖИНЫ")
    print("=" * 32)
    q = w = p = h = None
    while True:
        print()
        print("МЕНЮ")
        print("1 — ввод параметров")
        print("2 — классификация скважины")
        print("3 — сводка")
        print("5 — справка")
        print("0 — выход")
        choice = input("Выбор: ").strip()
        match choice:
            case "1":
                q = input_bounded("Дебит жидкости Qж, м³/сут: ", "Qж", *Q_RANGE)
                w = input_bounded("Обводнённость W, %: ", "W", *W_RANGE)
                if w==100:
                    print('W = 100 (чистая вода): убедитесь, что классификация не падает')
                    continue
                p = input_bounded("Пластовое давление W, МПа: ", "Pпл", *P_RANGE)
                h = input_bounded("Глубина H, м: ", "H", *H_RANGE)
                if p>80:
                    print('ПРЕДУПРЕЖДЕНИЕ:аномально высокое давление, проверьте данные')
                print("[ok] Параметры приняты.")
            case "2":
                if w is None:
                    print("[предупреждение] Сначала введите параметры (пункт 1).")
                else:
                    print(f"Обводнённость {w:.1f}% -> {classify_well(w)}")
            case "3":
                if q is None:
                    print("[предупреждение] Сначала введите параметры (пункт 1).")
                else:
                    print(f"Qж={q:.2f} м³/сут | W={w:.2f}% | "f"Pпл={p:.2f} МПа | H={h:.0f} м")
            case '5':
                print('команда 1 просит ввести все необходимые данные(Qж,W,H)')
                print('команда 2 показывает обводненость скважины и рациональность эксплуатации')
                print('команда 3 показывает сводку данных которые ввели')
                print('команда 0 выход из меню')

            case "0":
                print("Выход.")
                break
            case _:
                print("[ошибка] Неизвестный пункт меню.")
if __name__ == "__main__":
 main()
