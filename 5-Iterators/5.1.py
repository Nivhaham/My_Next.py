# yonatan the katan.
import winsound


def main():
    freqs = {"la": 220,
             "si": 247,
             "do": 261,
             "re": 293,
             "mi": 329,
             "fa": 349,
             "sol": 392,
             }
    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    list_of_notes = notes.split('-')
    print(list_of_notes)
    for tav_and_freq in list_of_notes:
        list_tav_and_freq = tav_and_freq.split(',')
        print(list_tav_and_freq)
        frequency = freqs[list_tav_and_freq[0]]
        duration = list_tav_and_freq[1]
        duration = int(duration)
        winsound.Beep(frequency, duration)


if __name__ == '__main__':
    main()
