import csv

# Необходимо заполнить список массами частей самолета
plane_masses = [
    3, 3, 3, 3, 3, 4, 4, 4, 
    4, 4, 4, 4, 4, 4, 5, 5, 
    5, 5, 6, 3, 5, 5, 5, 5, 
    5, 5, 5, 5, 5, 5, 5, 5, 
    5, 5, 4, 4, 3, 3, 3, 3, 
    3, 3, 3, 3, 3, 3, 20, 20, 
    20, 20, 20, 20, 20, 20, 20, 
    20, 2, 2, 2, 2, 2, 2, 2, 2, 
    2, 2, 2, 2, 2, 2, 2, 2, 2, 
    2, 2, 2, 2, 2, 2, 2, 2, 2, 
    2, 2, 5, 5, 5, 5, 5, 5, 5, 
    5, 5, 5, 5, 5, 5, 5, 5, 5]
# Позиция, в которую мы будем добавлять массу
position = 19
# Координата фокуса
x_f = 46

f = open("./file.csv", "w")
writer = csv.writer(f)

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
        write_to_file_data(plane_masses[position], x_c, x_f)
    return plane_masses[position] - initial_mass_positions

def write_to_file_data(current_mass: int, xc: float, xf: float()):
    data = [round(current_mass, 4), round(xc, 3), xf]
    writer.writerow(data)


def main():
    writer.writerow([f"current mass in position {position}", "x_c", "x_f"])
    needed = find_mass()
    print(f"Needed about {needed} to place in position {position}")


if __name__ == "__main__":
    main()