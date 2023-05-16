# Необходимо заполнить список массами частей самолета
plane_masses = []
# Позиция, в которую мы будем добавлять массу
position = 0
# Координата фокуса
x_f = 0

def find_center_masses() -> int:
    denom = sum(plane_masses)
    nomin = 0
    for i in range (0, len(plane_masses)):
        nomin += plane_masses[i] * i
    return nomin/denom

def find_mass() -> int:
    initial_mass_position = plane_masses[position]
    x_c = find_center_masses()
    print(x_c)
    while True:
        print(f"xc {x_c} xf {x_f}")
        if(x_c <= x_f + 0.0001 and x_c >= x_f - 0.0001):
            return plane_masses[position]
        plane_masses[position] += 0.001
        x_c = find_center_masses()

    return plane_masses[position] - initial_mass_positions


def main():
    needed = find_mass()
    print(f"Needed about {needed} to place in position {position}")


if __name__ == "__main__":
    main()