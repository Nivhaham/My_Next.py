class MusicNotes():
    def __init__(self):
        self.music_note = [[55, 61.74, 65.41, 73.42, 82.41, 87.31, 98],
                           [110, 123.48, 130.82, 146.84, 164.82, 174.62, 196],
                           [220, 246.96, 261.64, 293.68, 329.64, 349.24, 392],
                           [440, 493.92, 523.28, 587.36, 659.28, 698.48, 784],
                           [880, 987.84, 1046.56, 1174.72, 1318.56, 1396.96, 1568]
                           ]
        self.internal_index = 0
        self.external_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # print(len(self.music_note[0]))
        if self.external_index >= len(self.music_note):
            raise StopIteration
        if self.internal_index >= len(self.music_note[0]) - 1:
            self.external_index += 1
            self.internal_index = 0
        if self.external_index >= len(self.music_note):
            return self.music_note[len(self.music_note) - 1][len(self.music_note[0]) - 1]
        self.internal_index += 1

        return self.music_note[self.external_index][self.internal_index - 1]


def main():
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
        print(freq)


if __name__ == '__main__':
    main()
