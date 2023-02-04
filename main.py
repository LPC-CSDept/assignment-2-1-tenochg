def main():
    ##################################################
    # Comlete your code here
    ##################################################
    num_males = int(input('Number of Males in class: '))
    num_females = int(input('Number of Females in class: '))
    total_students = num_males + num_females
    percentage_males = (num_males/total_students) * 100
    percentage_females = (num_females/total_students) * 100
    print(f'The total number of students:{total_students:>15}')
    print(f'The Number of Males and Females: {num_males:>10} {num_females:>10}')
    print(f'The Percentage of Males and Females: {percentage_males:>9.2f}%{percentage_females:>9.2f}%')
    pass


if __name__ == '__main__':
    main()
