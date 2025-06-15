import re
import os
from difflib import SequenceMatcher


def tokenize(text: str) -> list[str]:
    """
    Extract “word” tokens (alphanumeric + apostrophes) from text.
    Converts to lowercase so matching is case-insensitive.
    """
    # [\w']+ matches sequences of letters, digits, underscore, and apostrophe
    return re.findall(r"[\w']+", text.lower())


def calculate_wer(original: str, transcribed: str) -> float:
    """Returns WER as a fraction."""
    # orig_words = original.split()
    # trans_words = transcribed.split()

    orig_words = tokenize(original)
    trans_words = tokenize(transcribed)

    matcher = SequenceMatcher(None, orig_words, trans_words)
    matches = matcher.get_matching_blocks()

    subs = dels = ins = 0
    o_idx = t_idx = 0
    for m in matches:
        # handle the regions between matches
        while o_idx < m.a or t_idx < m.b:
            if o_idx < m.a and t_idx < m.b:
                subs += 1
                o_idx += 1
                t_idx += 1
            elif o_idx < m.a:
                dels += 1
                o_idx += 1
            else:
                ins += 1
                t_idx += 1
        # jump over the matched block
        o_idx = m.a + m.size
        t_idx = m.b + m.size

    # any trailing insertions/deletions
    dels += len(orig_words) - o_idx
    ins  += len(trans_words) - t_idx

    return (subs + dels + ins) / len(orig_words)


def batch_wer_by_levels(
    original_path: str,
    transcripts_dir: str,
    mic_type: str,
    levels=None
):
    # Read the reference once
    with open(original_path, 'r', encoding='utf-8') as f:
        original = f.read()

    # if user passed levels, prepare a set of strings for matching
    if levels is not None:
        level_set = {str(l) for l in levels}
    else:
        level_set = None  # means “auto-detect everything”

    # Pattern captures both xx (level) and yy (index)
    pat = re.compile(rf"Batch_parse_{mic_type}_60_(\d+)_(\d+)\.txt$")

    # Map level → list of WERs
    level2wers: dict[str, list[float]] = {}

    for fn in os.listdir(transcripts_dir):
        m = pat.match(fn)
        if not m:
            continue
        lvl, idx = m.group(1), m.group(2)
        # if user specified levels, skip others
        if level_set is not None and lvl not in level_set:
            continue

        path = os.path.join(transcripts_dir, fn)
        with open(path, 'r', encoding='utf-8') as g:
            transcript = g.read()

        wer_pct = calculate_wer(original, transcript) * 100
        level2wers.setdefault(lvl, []).append(wer_pct)

    # Print out results
    for lvl in sorted(level2wers, key=lambda x: int(x)):
        wers = level2wers[lvl]
        avg  = sum(wers) / len(wers)
        print(f"Noise {lvl:>3}%: {len(wers):>3d} files → avg WER: {avg:6.2f}%")


if __name__ == '__main__':
    MIC_TYPE = 'tws'
    TXT_FILE_PATH = f'data_log/audacity/new_self-talk/{MIC_TYPE}/batch_parsed'
    LEVEL = 100
    batch_wer_by_levels('original.txt', TXT_FILE_PATH, MIC_TYPE, levels=[LEVEL])
