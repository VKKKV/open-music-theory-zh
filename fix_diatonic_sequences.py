#!/usr/bin/env python3
"""Fix inline examples for diatonic-harmony/14-diatonic-sequences.md"""
import re

path = "/home/kita/code/open-music-theory-zh/src/diatonic-harmony/14-diatonic-sequences.md"
with open(path, "r", encoding="utf-8") as f:
    original = f.read()

lines = original.split("\n")

# Mapping: which iframe/image goes before which "例 N." line
# The key is a unique substring that identifies the "例 N." line
insertions = {
    '例 1.': [
        '<iframe src="https://musescore.com/user/32728834/scores/26074258/embed" width="100%" height="240" frameborder="0" allowfullscreen allow="autoplay"></iframe>',
    ],
    '例 2.': [
        '[![两个潜在的模式](../Graphics/app/uploads/sites/12/2025/07/Diatonic_Sequences_Patterns_Illustration.png)](https://viva.pressbooks.pub/app/uploads/sites/12/2025/07/Diatonic_Sequences_Patterns_Illustration.png)',
    ],
    '例 3.': [
        '<iframe src="https://musescore.com/user/32728834/scores/26074177/embed" width="100%" height="240" frameborder="0" allowfullscreen allow="autoplay"></iframe>',
    ],
    '例 4.': [
        '<iframe src="https://musescore.com/user/32728834/scores/26074216/embed" width="100%" height="240" frameborder="0" allowfullscreen allow="autoplay"></iframe>',
    ],
    '例 5.': [
        '<iframe src="https://musescore.com/user/32728834/scores/26074285/embed" width="100%" height="240" frameborder="0" allowfullscreen allow="autoplay"></iframe>',
    ],
    '例 6.': [
        '<iframe src="https://musescore.com/user/32728834/scores/26074351/embed" width="100%" height="240" frameborder="0" allowfullscreen allow="autoplay"></iframe>',
    ],
    '例 7.': [
        '<iframe src="https://musescore.com/user/32728834/scores/26074324/embed" width="100%" height="240" frameborder="0" allowfullscreen allow="autoplay"></iframe>',
    ],
    '例 8.': [
        '<iframe src="https://musescore.com/user/32728834/scores/26074309/embed" width="100%" height="240" frameborder="0" allowfullscreen allow="autoplay"></iframe>',
    ],
}

# Build new content
new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    
    # Check if this line starts with "例 N."
    matched_key = None
    for key in insertions:
        if line.strip().startswith(key):
            matched_key = key
            break
    
    if matched_key:
        # Insert content before this line
        for insert_line in insertions[matched_key]:
            new_lines.append("")
            new_lines.append(insert_line)
            new_lines.append("")
        new_lines.append(line)
    else:
        new_lines.append(line)
    
    i += 1

# Now remove moved MuseScore iframes from the bottom "🎵 音频与互动示例" section
# Keep: YouTube video, Spotify playlist, original link
final_lines = []
in_audio_section = False
for line in new_lines:
    if '音频与互动示例' in line:
        in_audio_section = True
        final_lines.append(line)
        continue
    
    if in_audio_section:
        # Check for section end markers
        if line.strip().startswith('*原文'):
            in_audio_section = False
            final_lines.append(line)
            continue
            
        # Skip MuseScore iframes (moved inline)
        if 'musescore.com' in line:
            continue
        # Keep YouTube
        if 'youtube.com' in line:
            final_lines.append(line)
            continue
        # Keep playlist
        if '章节播放列表' in line or 'spotify.com' in line:
            final_lines.append(line)
            continue
        # Skip blank lines (excess spacing)
        if line.strip() == '':
            continue
    
    final_lines.append(line)

# Remove excess consecutive blank lines (max 2)
cleaned = []
empty_run = 0
for line in final_lines:
    if line == '':
        empty_run += 1
        if empty_run <= 2:
            cleaned.append(line)
    else:
        empty_run = 0
        cleaned.append(line)

output = "\n".join(cleaned)

with open(path, "w", encoding="utf-8") as f:
    f.write(output)

print("Done! File written.")
print(f"Lines: {len(lines)} -> {len(cleaned)}")
