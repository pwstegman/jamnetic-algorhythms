"""
Toolkit of methods for calculating stats of a piece
"""

from math import log2

def shannonEntropy(currentPiece):
    # Calculate Shannon entropy
    counts = {}
    total = 0

    for measure in currentPiece:
        for note in measure:
            total += 1
            if note.midi_note in counts:
                counts[note.midi_note] += 1
            else:
                counts[note.midi_note] = 1

    entropy = 0
    for key in counts:
        frequency = counts[key] / total
        entropy -= frequency * log2(frequency)

    return entropy