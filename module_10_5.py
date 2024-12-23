from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]
        all_data.extend(lines)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == "__main__":
    # start_1 = datetime.now()
    # for filename in filenames:
    #     read_info(filename)
    # end_1 = datetime.now()
    # print(f"{end_1 - start_1} (линейный)")

    with multiprocessing.Pool(processes=8) as pool:
        start_2 = datetime.now()
        pool.map(read_info, filenames)
    end_2 = datetime.now()
    print(f"{end_2 - start_2} (многопроцессный)")
