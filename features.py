"""
Toolkit of methods for calculating stats of a piece
"""

from math import log2
import gzip

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

def gzipEntropy(currentPiece):
    notes = [note.midi_note if note.midi_note is not None else 0
                for measure in currentPiece
                    for note in measure]
    
    rawBytes = bytes()
    for note in notes:
        rawBytes += note.to_bytes(1, byteorder='big')

    compressed = gzip.compress(rawBytes)
    
    return len(compressed) / len(rawBytes)