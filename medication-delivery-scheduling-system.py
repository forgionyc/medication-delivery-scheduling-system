# Define a function named readData that reads data from a CSV file.
def readData():
    with open("data.csv", 'r') as datafile:

        # Read the first line from the CSV file, which is assumed to contain column headers.
        line = datafile.readline()

        # Remove the newline character and split the line into a list of column headers.
        encabezado = line.rstrip('\n').split(',')

        # Create an empty list to store the data rows.
        matriz = []

        # Create a list of 32 empty strings to store branch names based on branch IDs.
        sucursales = [' '] * 32

        # Read the next line from the CSV file.
        linea = datafile.readline()

        # Start a loop to read and process each data row in the CSV file.
        while linea:

            fila = linea.rstrip('\n').split(',')

            sucursales[int(fila[5])-1] = fila[3] + " " + fila[4]

            matriz.append(fila)

            linea = datafile.readline()
    # Return the processed data: matriz (list of data rows), sucursales (list of branch names),
    # and encabezado (list of column headers).
    return matriz, sucursales, encabezado

def main():
    patients, city_name, columns = readData()

    i_gender = columns.index('gender')
    i_branch = columns.index('id_branch')
    i_ps = columns.index('systolic_pressure')
    i_pd = columns.index('diastolic_pressure')
    i_mq = columns.index('medicine_quantity')
    men = 0
    women = 0
    len_pacientes = len(patients)
    cant_med = 0

    main_input = int(input())

    for i in range(len_pacientes):
        if int(patients[i][i_branch]) == main_input:
            delivery = False
            sis, dia = int(patients[i][i_ps]), int(patients[i][i_pd])
            if sis < 91 and dia < 63:
                delivery = True
            elif 162 <= sis < 188 and 105 <= dia < 119:
                delivery = True
            elif 188 <= sis < 201 and 119 <= dia < 126:
                delivery = True
            elif 201 <= sis < 214 and 126 <= dia < 146:
                delivery = True
            elif sis >= 214 and dia >= 146:
                delivery = True
            elif sis >= 152 and dia < 77:
                delivery = True
            else:
                delivery= False

            if delivery:
                if patients[i][i_gender]=="m":
                    men += 1
                else :
                    women += 1

                cant_med += int(patients[i][i_mq])

    print(f"{main_input} {city_name[main_input-1]}")
    print("scheduled patients")
    print(f'male {men}')
    print(f"female {women}")
    print(f'total {men + women}')
    print('scheduled medicine quantity')
    print('mean {:.2f}'.format(cant_med/(men+women)))
    print(f"total {cant_med}")

if __name__=='__main__':
    main()